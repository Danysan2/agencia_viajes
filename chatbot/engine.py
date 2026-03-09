"""Motor principal del chatbot de agencia de viajes."""
from typing import Optional, Tuple
from loguru import logger

from services import SheetsClient, WhatsAppService
from models import Cliente, Sesion
from config.constants import *


class ChatbotEngine:
    """Motor del chatbot conversacional para agencia de viajes."""
    
    def __init__(self):
        """Inicializa el motor del chatbot."""
        self.sheets = SheetsClient()
        self.whatsapp = WhatsAppService()
    
    def procesar_mensaje(self, telefono: str, mensaje: str) -> str:
        """
        Procesa un mensaje entrante y retorna la respuesta.
        
        Args:
            telefono: Número de teléfono del usuario
            mensaje: Texto del mensaje
        
        Returns:
            Respuesta del chatbot
        """
        mensaje = mensaje.strip().lower()
        
        # Verificar si es comando para volver al menú
        if mensaje in ['menu', 'menú', 'inicio', 'hola', 'volver']:
            self.sheets.eliminar_sesion(telefono)
            sesion = Sesion(telefono=telefono, estado=ESTADO_INICIO)
            self.sheets.crear_sesion(sesion)
            return self._menu_principal()
        
        # Obtener o crear sesión
        sesion_data = self.sheets.get_sesion(telefono)
        
        if sesion_data is None:
            # Nueva sesión - mostrar bienvenida
            sesion = Sesion(telefono=telefono, estado=ESTADO_INICIO)
            self.sheets.crear_sesion(sesion)
            return self._menu_principal()
        
        sesion, row_index = sesion_data
        
        # Procesar según el estado actual
        if sesion.estado == ESTADO_INICIO:
            return self._procesar_menu_principal(telefono, mensaje, sesion, row_index)
        elif sesion.estado == ESTADO_VER_DESTINOS:
            return self._procesar_seleccion_destino(telefono, mensaje, sesion, row_index)
        elif sesion.estado == ESTADO_VER_HOTELES:
            return self._procesar_seleccion_hotel(telefono, mensaje, sesion, row_index)
        
        # Estado desconocido - resetear
        self.sheets.eliminar_sesion(telefono)
        return self._menu_principal()
    
    def _menu_principal(self) -> str:
        """Retorna el menú principal de bienvenida."""
        return """✈️ ¡Hola! Bienvenido a *Viajes Colombia Tours* 🇨🇴

Es un gusto tenerte aquí. Somos tu agencia de confianza para descubrir los destinos más increíbles de nuestro país.

¿En qué te podemos ayudar hoy? Elige una opción:

1️⃣ Conocer nuestros destinos en Colombia
2️⃣ Información sobre nosotros
3️⃣ Hablar con un asesor
4️⃣ Ver promociones y ofertas especiales

Responde con el número de la opción."""
    
    def _procesar_menu_principal(
        self,
        telefono: str,
        mensaje: str,
        sesion: Sesion,
        row_index: int
    ) -> str:
        """Procesa la selección del menú principal."""
        if mensaje not in ['1', '2', '3', '4']:
            return "Opción inválida. Por favor responde con un número del 1 al 4."
        
        if mensaje == '1':
            # Ver destinos
            sesion.estado = ESTADO_VER_DESTINOS
            sesion.datos_temp = {}
            self.sheets.actualizar_sesion(sesion, row_index)
            return self._mostrar_destinos()
        
        elif mensaje == '2':
            # Información sobre nosotros
            self.sheets.eliminar_sesion(telefono)
            return self._mostrar_informacion_agencia()
        
        elif mensaje == '3':
            # Contactar asesor
            self.sheets.eliminar_sesion(telefono)
            return self._contactar_humano()
        
        elif mensaje == '4':
            # Ver promociones
            self.sheets.eliminar_sesion(telefono)
            return self._mostrar_promociones()
        
        return "Opción inválida."
    
    def _mostrar_destinos(self) -> str:
        """Muestra los destinos disponibles."""
        return """🗺️ ¡Excelente elección! Colombia tiene destinos increíbles para ti.

¿A cuál de estos lugares te gustaría viajar?

1️⃣ Bogotá 🏛️
2️⃣ Medellín 🌸
3️⃣ Cartagena 🏖️
4️⃣ Arauca 🌾

Responde con el número del destino."""
    
    def _procesar_seleccion_destino(
        self,
        telefono: str,
        mensaje: str,
        sesion: Sesion,
        row_index: int
    ) -> str:
        """Procesa la selección de destino."""
        destinos_map = {
            '1': 'bogota',
            '2': 'medellin',
            '3': 'cartagena',
            '4': 'arauca'
        }
        
        if mensaje not in destinos_map:
            return "Opción inválida. Por favor responde con un número del 1 al 4."
        
        destino_key = destinos_map[mensaje]
        sesion.datos_temp = {"destino": destino_key}
        sesion.estado = ESTADO_VER_HOTELES
        self.sheets.actualizar_sesion(sesion, row_index)
        
        return self._mostrar_hoteles(destino_key)
    
    def _mostrar_hoteles(self, destino: str) -> str:
        """Muestra los hoteles disponibles para un destino."""
        hoteles = HOTELES.get(destino, [])
        
        if not hoteles:
            return f"Lo sentimos, no tenemos hoteles disponibles en {DESTINOS[destino]['nombre']} en este momento.\n\nEscribe *menú* para volver al inicio."
        
        destino_info = DESTINOS[destino]
        mensaje = f"{destino_info['emoji']} *{destino_info['nombre']}* te espera con estos hoteles disponibles:\n\n"
        
        for idx, hotel in enumerate(hoteles, 1):
            mensaje += f"{idx}️⃣ {hotel['nombre']}\n"
        
        mensaje += "\n¿Cuál te llama la atención? Responde con el número."
        return mensaje
    
    def _procesar_seleccion_hotel(
        self,
        telefono: str,
        mensaje: str,
        sesion: Sesion,
        row_index: int
    ) -> str:
        """Procesa la selección de hotel y muestra detalles."""
        destino = sesion.datos_temp.get("destino")
        if not destino:
            self.sheets.eliminar_sesion(telefono)
            return "Error en la sesión. Escribe *menú* para comenzar de nuevo."
        
        hoteles = HOTELES.get(destino, [])
        
        try:
            opcion = int(mensaje)
            if opcion < 1 or opcion > len(hoteles):
                return f"Opción inválida. Por favor responde con un número del 1 al {len(hoteles)}."
        except ValueError:
            return f"Por favor responde con un número del 1 al {len(hoteles)}."
        
        hotel = hoteles[opcion - 1]
        
        # Limpiar sesión después de mostrar detalles
        self.sheets.eliminar_sesion(telefono)
        
        return self._formatear_detalle_hotel(hotel)
    
    def _formatear_detalle_hotel(self, hotel: dict) -> str:
        """Formatea los detalles completos de un hotel."""
        mensaje = f"🏨 *{hotel['nombre']} – {hotel['destino']}*\n\n"
        mensaje += "✅ Incluye:\n"
        
        for item in hotel['incluye']:
            mensaje += f"• {item}\n"
        
        mensaje += f"\n💰 *Precio por noche:* ${hotel['precio_noche']:,} COP\n"
        mensaje += "📅 Disponibilidad: Todo el año\n\n"
        mensaje += "¿Te interesa este plan o quieres ver otro hotel?\n\n"
        mensaje += "Escribe *menú* para volver al inicio o *3* para hablar con un asesor."
        
        return mensaje
    
    def _mostrar_informacion_agencia(self) -> str:
        """Muestra información sobre la agencia."""
        return f"""🏢 *Sobre {AGENCIA_NOMBRE}*

¡Llevamos más de 8 años conectando a los colombianos con los destinos más hermosos del país! 🇨🇴

🌟 *¿Qué ofrecemos?*
• Paquetes turísticos nacionales todo incluido
• Asesoría personalizada sin costo
• Planes para familias, parejas y grupos
• Hoteles seleccionados y verificados
• Acompañamiento antes, durante y después del viaje

📍 *Sede principal:* {AGENCIA_SEDE}
⏰ *Horario de atención:* {AGENCIA_HORARIO}
📞 *Línea directa:* {AGENCIA_TELEFONO}

¿Deseas volver al menú principal? Escribe *menú*"""
    
    def _contactar_humano(self) -> str:
        """Mensaje para contactar con un asesor humano."""
        return """👤 En un momento uno de nuestros asesores estará contigo.

Por favor cuéntanos brevemente: *¿en qué destino estás interesado?* así podemos ayudarte mejor. 😊

Escribe *menú* para volver al inicio."""
    
    def _mostrar_promociones(self) -> str:
        """Muestra las promociones y ofertas especiales."""
        mensaje = "🔥 *Promociones y Ofertas Especiales* 🔥\n\n"
        
        for idx, promo in enumerate(PROMOCIONES, 1):
            mensaje += f"🎉 *Oferta {idx} – {promo['nombre']}*\n"
            mensaje += f"Paquete {promo['noches']} noches para {promo['personas']} personas\n"
            mensaje += f"✅ {promo['incluye']}\n"
            mensaje += f"💰 Antes: ${promo['precio_antes']:,} | *Ahora: ${promo['precio_ahora']:,} COP*\n\n"
        
        mensaje += f"⏳ Ofertas válidas hasta el {PROMOCIONES[0]['valido_hasta']}\n\n"
        mensaje += "¿Te interesa alguna? Escríbenos o habla con un asesor.\n"
        mensaje += "¿Volver al menú? Escribe *menú*"
        
        return mensaje
