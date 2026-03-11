"""Motor principal del chatbot de agencia de viajes."""
from typing import Optional, Tuple
from datetime import datetime

# Importar logger solo si está disponible
try:
    from loguru import logger
except ImportError:
    class SimpleLogger:
        def info(self, msg): print(f"INFO: {msg}")
        def error(self, msg): print(f"ERROR: {msg}")
        def warning(self, msg): print(f"WARNING: {msg}")
    logger = SimpleLogger()

from services import WhatsAppService
# SheetsClient y CalendarClient opcionales para testing
try:
    from services import SheetsClient
except:
    class SheetsClient:
        def __init__(self): pass
        def get_sesion(self, telefono): return None
        def crear_sesion(self, sesion): return True
        def actualizar_sesion(self, sesion, row): return True
        def eliminar_sesion(self, telefono): return True
        def get_cliente_por_telefono(self, telefono): return None
        def crear_cliente(self, telefono, nombre): 
            from models import Cliente
            from datetime import datetime
            return Cliente("cli_test", telefono, nombre, datetime.now(), 0)

from models import Cliente, Sesion
from config.constants import *
from config.settings import PROFESSIONAL_PHONE


class ChatbotEngine:
    """Motor del chatbot conversacional para agencia de viajes."""
    
    def __init__(self):
        """Inicializa el motor del chatbot."""
        try:
            self.sheets = SheetsClient()
        except:
            # Mock de SheetsClient que guarda sesiones en memoria
            class MockSheets:
                def __init__(self):
                    self.sesiones = {}  # Diccionario para guardar sesiones en memoria
                    self.row_counter = 1
                
                def get_sesion(self, telefono):
                    if telefono in self.sesiones:
                        logger.info(f"🔍 MockSheets: Sesión encontrada para {telefono}, estado={self.sesiones[telefono].estado}")
                        return self.sesiones[telefono], self.row_counter
                    logger.info(f"🔍 MockSheets: No hay sesión para {telefono}")
                    return None
                
                def crear_sesion(self, sesion):
                    logger.info(f"➕ MockSheets: Creando sesión para {sesion.telefono}, estado={sesion.estado}")
                    self.sesiones[sesion.telefono] = sesion
                    self.row_counter += 1
                    return self.row_counter
                
                def actualizar_sesion(self, sesion, row):
                    logger.info(f"🔄 MockSheets: Actualizando sesión para {sesion.telefono}, estado={sesion.estado}")
                    self.sesiones[sesion.telefono] = sesion
                    return True
                
                def eliminar_sesion(self, telefono):
                    logger.info(f"🗑️ MockSheets: Eliminando sesión para {telefono}")
                    if telefono in self.sesiones:
                        del self.sesiones[telefono]
                    return True
                
                def get_cliente_por_telefono(self, telefono):
                    return None
                
                def crear_cliente(self, telefono, nombre):
                    return None
            
            self.sheets = MockSheets()
        
        try:
            self.whatsapp = WhatsAppService()
        except:
            self.whatsapp = None
        
        # Número del profesional para notificaciones
        self.professional_phone = PROFESSIONAL_PHONE
    
    def procesar_mensaje(self, telefono: str, mensaje: str) -> str:
        """
        Procesa un mensaje entrante y retorna la respuesta.
        
        Args:
            telefono: Número de teléfono del usuario
            mensaje: Texto del mensaje
        
        Returns:
            Respuesta del chatbot
        """
        mensaje_original = mensaje
        mensaje = mensaje.strip().lower()
        
        # Obtener o crear sesión
        sesion_data = self.sheets.get_sesion(telefono)
        
        if sesion_data is None:
            sesion = Sesion(telefono=telefono, estado=ESTADO_INICIO, bot_activo=True)
            row_index = self.sheets.crear_sesion(sesion)
            logger.info(f"📝 Nueva sesión creada para {telefono} en estado {sesion.estado}")
        else:
            sesion, row_index = sesion_data
            logger.info(f"📝 Sesión recuperada para {telefono} en estado {sesion.estado}")
        
        # VERIFICAR SI EL BOT ESTÁ DESACTIVADO (HUMANO ATENDIENDO)
        if not sesion.bot_activo:
            # Verificar si han pasado 12 horas desde el handoff
            if sesion.handoff_timestamp:
                from datetime import timedelta
                tiempo_transcurrido = datetime.now() - sesion.handoff_timestamp
                if tiempo_transcurrido > timedelta(hours=HORAS_REACTIVACION_AUTO):
                    # Reactivar bot automáticamente después de 12 horas
                    logger.info(f"🤖 Reactivando bot automáticamente para {telefono} (12 horas transcurridas)")
                    sesion.bot_activo = True
                    sesion.handoff_timestamp = None
                    sesion.estado = ESTADO_INICIO
                    self.sheets.actualizar_sesion(sesion, row_index)
                    return self._menu_principal()
            
            # Verificar si el mensaje es un comando de reactivación del bot
            if any(comando in mensaje for comando in COMANDOS_REACTIVAR_BOT):
                logger.info(f"🤖 Reactivando bot for {telefono} por comando del asesor")
                sesion.bot_activo = True
                sesion.handoff_timestamp = None
                sesion.estado = ESTADO_INICIO
                self.sheets.actualizar_sesion(sesion, row_index)
                return """✅ *Bot reactivado*

Hola de nuevo! Estoy aquí para ayudarte.

""" + self._menu_principal()
            
            # Si el bot está desactivado y no es comando de reactivación, no responder
            logger.info(f"🔇 Bot desactivado para {telefono}. Mensaje ignorado: {mensaje_original[:50]}")
            return None  # No enviar respuesta automática
        
        # BOT ACTIVO - PROCESAMIENTO NORMAL
        
        # Verificar si es comando para volver al menú (excepto "hola" en primera interacción)
        if mensaje in ['menu', 'menú', 'inicio', 'volver']:
            self.sheets.eliminar_sesion(telefono)
            sesion = Sesion(telefono=telefono, estado=ESTADO_INICIO, bot_activo=True)
            row_index = self.sheets.crear_sesion(sesion)
            return self._menu_principal()
        
        # "hola" solo resetea si ya hay una sesión activa, sino es el saludo inicial
        if mensaje == 'hola' and sesion.estado != ESTADO_INICIO:
            self.sheets.eliminar_sesion(telefono)
            sesion = Sesion(telefono=telefono, estado=ESTADO_INICIO, bot_activo=True)
            row_index = self.sheets.crear_sesion(sesion)
            return self._menu_principal()
        
        # Procesar según el estado actual
        logger.info(f"🔄 Procesando mensaje en estado: {sesion.estado}")
        
        if sesion.estado == ESTADO_INICIO:
            # Si el usuario escribe "hola" en estado inicio, mostrar menú
            if mensaje == 'hola':
                return self._menu_principal()
            return self._procesar_menu_principal(telefono, mensaje, sesion, row_index)
        elif sesion.estado == ESTADO_BOLETOS_NACIONALES:
            logger.info(f"📍 Procesando selección de destino nacional: {mensaje}")
            return self._procesar_boletos_nacionales(telefono, mensaje, sesion, row_index)
        elif sesion.estado == ESTADO_BOLETOS_INTERNACIONALES:
            return self._procesar_boletos_internacionales(telefono, mensaje, sesion, row_index)
        elif sesion.estado == ESTADO_BOLETOS_AEREOS:
            return self._procesar_boletos_aereos(telefono, mensaje, sesion, row_index)
        elif sesion.estado == ESTADO_PAQUETES_TURISTICOS:
            return self._procesar_paquetes_turisticos(telefono, mensaje, sesion, row_index)
        
        # Estado desconocido - resetear
        logger.warning(f"⚠️ Estado desconocido: {sesion.estado} - Reseteando")
        self.sheets.eliminar_sesion(telefono)
        return self._menu_principal()
    
    def _menu_principal(self) -> str:
        """Retorna el menú principal de bienvenida."""
        return """✈️ ¡Hola! Bienvenido a *Viajes Colombia Tours* 🇨🇴

Tu agencia de confianza para viajar por Colombia y el mundo.

¿Qué estás buscando hoy?

1️⃣ Boletos nacionales en Colombia
2️⃣ Boletos internacionales
3️⃣ Boletos aéreos (rutas populares)
4️⃣ Paquetes turísticos

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
            # Boletos nacionales
            sesion.estado = ESTADO_BOLETOS_NACIONALES
            sesion.datos_temp = {}
            self.sheets.actualizar_sesion(sesion, row_index)
            return self._mostrar_destinos_nacionales()
        
        elif mensaje == '2':
            # Boletos internacionales
            sesion.estado = ESTADO_BOLETOS_INTERNACIONALES
            sesion.datos_temp = {}
            self.sheets.actualizar_sesion(sesion, row_index)
            return self._mostrar_destinos_internacionales()
        
        elif mensaje == '3':
            # Boletos aéreos - Enviar a humano
            self.sheets.eliminar_sesion(telefono)
            # Enviar notificación al profesional
            self._enviar_notificacion_profesional(telefono, "Boletos aéreos")
            return """✈️ *Boletos Aéreos*

Perfecto! Un asesor especializado te contactará en breve para ayudarte con:

• Consulta de disponibilidad
• Mejores tarifas del momento
• Opciones de aerolíneas
• Horarios de vuelos
• Reserva y emisión de boletos

⏰ Tiempo de respuesta: 5-10 minutos

Escribe *menú* si deseas ver otras opciones mientras esperas."""
        
        elif mensaje == '4':
            # Paquetes turísticos - Enviar a humano
            self.sheets.eliminar_sesion(telefono)
            # Enviar notificación al profesional
            self._enviar_notificacion_profesional(telefono, "Paquetes turísticos")
            return """🎒 *Paquetes Turísticos*

Excelente elección! Un asesor especializado te contactará en breve para ayudarte con:

• Paquetes personalizados
• Mejores ofertas disponibles
• Itinerarios detallados
• Opciones de pago
• Reserva de tu paquete ideal

⏰ Tiempo de respuesta: 5-10 minutos

Escribe *menú* si deseas ver otras opciones mientras esperas."""
        
        return "Opción inválida."
    
    def _mostrar_destinos_nacionales(self) -> str:
        """Muestra los destinos nacionales disponibles desde Arauca con precios."""
        mensaje = "🚌 *Boletos Nacionales desde Arauca*\n\n"
        mensaje += "Destinos disponibles:\n\n"
        
        # Mostrar destinos con precios
        for idx, destino in enumerate(DESTINOS_NACIONALES_DESDE_ARAUCA, 1):
            precio_formateado = f"${destino['precio']:,}".replace(",", ".")
            mensaje += f"{idx}. {destino['nombre']} - {precio_formateado}\n"
            
            # Agregar salto de línea cada 5 destinos para mejor lectura
            if idx % 5 == 0:
                mensaje += "\n"
        
        mensaje += "\n💡 Todos los boletos son desde *Arauca* hacia el destino seleccionado.\n"
        mensaje += f"\n📝 Escribe el *número* del destino (1-{len(DESTINOS_NACIONALES_DESDE_ARAUCA)}) para más información.\n"
        mensaje += "\nEscribe *volver* para regresar al menú principal."
        return mensaje
    
    def _procesar_boletos_nacionales(
        self,
        telefono: str,
        mensaje: str,
        sesion: Sesion,
        row_index: int
    ) -> str:
        """Procesa la selección de destino nacional desde Arauca."""
        # Verificar si quiere volver al menú
        if mensaje in ['volver', 'menu', 'menú', 'atras', 'atrás']:
            self.sheets.eliminar_sesion(telefono)
            return self._menu_principal()
        
        try:
            opcion = int(mensaje)
            
            if opcion < 1 or opcion > len(DESTINOS_NACIONALES_DESDE_ARAUCA):
                return f"Opción inválida. Por favor responde con un número del 1 al {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} o escribe *volver* para regresar al menú."
            
            destino = DESTINOS_NACIONALES_DESDE_ARAUCA[opcion - 1]
            
            # Formatear precio
            precio_formateado = f"${destino['precio']:,}".replace(",", ".")
            
            # DESACTIVAR BOT Y TRANSFERIR A HUMANO
            sesion.bot_activo = False
            sesion.handoff_timestamp = datetime.now()
            sesion.estado = ESTADO_HANDOFF_HUMANO
            sesion.datos_temp['destino_seleccionado'] = destino['nombre']
            sesion.datos_temp['departamento'] = destino['departamento']
            sesion.datos_temp['precio'] = destino['precio']
            sesion.datos_temp['tipo_solicitud'] = 'Boleto Nacional'
            self.sheets.actualizar_sesion(sesion, row_index)
            
            # Obtener nombre del cliente si existe
            try:
                cliente = self.sheets.get_cliente_por_telefono(telefono)
                nombre_cliente = cliente.nombre if cliente else "Cliente"
            except:
                nombre_cliente = "Cliente"
            
            # Enviar notificación al profesional
            self._enviar_notificacion_handoff(
                telefono_cliente=telefono,
                nombre_cliente=nombre_cliente,
                tipo_solicitud="Boleto Nacional",
                detalles=f"Arauca → {destino['nombre']}, {destino['departamento']} | Precio: {precio_formateado}"
            )
            
            # Respuesta al cliente
            return f"""🚌 *Arauca → {destino['nombre']}*

📍 Destino: {destino['nombre']}, {destino['departamento']}
🚏 Origen: Arauca
💰 Precio: {precio_formateado} COP

✅ *Solicitud recibida*

Un asesor especializado te contactará en breve para ayudarte con:
• Disponibilidad de horarios
• Confirmación de precio
• Tipo de vehículo
• Duración del viaje
• Reserva de tu boleto

⏰ Tiempo de respuesta: 5-10 minutos

_Un asesor humano te atenderá personalmente._"""
            
        except ValueError:
            return f"Por favor responde con el número del destino (1-{len(DESTINOS_NACIONALES_DESDE_ARAUCA)}) o escribe *volver* para regresar al menú."
    
    def _mostrar_destinos_internacionales(self) -> str:
        """Muestra los destinos internacionales disponibles."""
        mensaje = "🌎 *Boletos Internacionales*\n\n"
        mensaje += "Destinos disponibles:\n\n"
        
        for idx, (key, destino) in enumerate(DESTINOS_INTERNACIONALES.items(), 1):
            mensaje += f"{idx}️⃣ {destino['emoji']} *{destino['nombre']}*\n"
            # Mostrar ciudades disponibles
            ciudades_str = ", ".join(destino['ciudades'])
            mensaje += f"   📍 Ciudades: {ciudades_str}\n\n"
        
        mensaje += "💡 Selecciona el número del país para más información.\n"
        mensaje += "\nEscribe *volver* para regresar al menú principal."
        return mensaje
    
    def _procesar_boletos_internacionales(
        self,
        telefono: str,
        mensaje: str,
        sesion: Sesion,
        row_index: int
    ) -> str:
        """Procesa la selección de destino internacional."""
        # Verificar si quiere volver al menú
        if mensaje in ['volver', 'menu', 'menú', 'atras', 'atrás']:
            self.sheets.eliminar_sesion(telefono)
            return self._menu_principal()
        
        try:
            opcion = int(mensaje)
            destinos_list = list(DESTINOS_INTERNACIONALES.values())
            
            if opcion < 1 or opcion > len(destinos_list):
                return f"Opción inválida. Por favor responde con un número del 1 al {len(destinos_list)} o escribe *volver* para regresar al menú."
            
            destino = destinos_list[opcion - 1]
            
            # DESACTIVAR BOT Y TRANSFERIR A HUMANO
            sesion.bot_activo = False
            sesion.handoff_timestamp = datetime.now()
            sesion.estado = ESTADO_HANDOFF_HUMANO
            sesion.datos_temp['destino_seleccionado'] = destino['nombre']
            sesion.datos_temp['ciudades'] = destino['ciudades']
            sesion.datos_temp['tipo_solicitud'] = 'Boleto Internacional'
            self.sheets.actualizar_sesion(sesion, row_index)
            
            # Obtener nombre del cliente si existe
            try:
                cliente = self.sheets.get_cliente_por_telefono(telefono)
                nombre_cliente = cliente.nombre if cliente else "Cliente"
            except:
                nombre_cliente = "Cliente"
            
            # Formatear ciudades
            ciudades_str = ", ".join(destino['ciudades'])
            
            # Enviar notificación al profesional
            self._enviar_notificacion_handoff(
                telefono_cliente=telefono,
                nombre_cliente=nombre_cliente,
                tipo_solicitud="Boleto Internacional",
                detalles=f"{destino['emoji']} {destino['nombre']} ({ciudades_str})"
            )
            
            # Respuesta al cliente
            return f"""✈️ *{destino['emoji']} {destino['nombre']}*

📍 Ciudades: {ciudades_str}

✅ *Solicitud recibida*

Un asesor especializado te contactará en breve para ayudarte con:
• Disponibilidad de vuelos
• Mejores tarifas
• Opciones de aerolíneas
• Requisitos de viaje
• Documentación necesaria
• Reserva de boletos

⏰ Tiempo de respuesta: 5-10 minutos

_Un asesor humano te atenderá personalmente._"""
            
        except ValueError:
            return f"Por favor responde con el número del país (1-{len(list(DESTINOS_INTERNACIONALES.values()))}) o escribe *volver* para regresar al menú."
    
    def _mostrar_boletos_aereos(self) -> str:
        """Muestra las rutas aéreas populares."""
        mensaje = "✈️ *Boletos Aéreos - Rutas Populares*\n\n"
        
        mensaje += "🇨🇴 *Vuelos Nacionales:*\n\n"
        for idx, vuelo in enumerate(BOLETOS_AEREOS["nacionales"], 1):
            mensaje += f"{idx}. {vuelo['ruta']}\n"
            mensaje += f"   💰 Desde ${vuelo['precio_desde']:,} COP\n"
            mensaje += f"   ⏱️ {vuelo['duracion']}\n"
            mensaje += f"   ✈️ {vuelo['aerolinea']}\n\n"
        
        mensaje += "🌎 *Vuelos Internacionales:*\n\n"
        for idx, vuelo in enumerate(BOLETOS_AEREOS["internacionales"], len(BOLETOS_AEREOS["nacionales"]) + 1):
            mensaje += f"{idx}. {vuelo['ruta']}\n"
            mensaje += f"   💰 Desde ${vuelo['precio_desde']:,} COP\n"
            mensaje += f"   ⏱️ {vuelo['duracion']}\n"
            mensaje += f"   ✈️ {vuelo['aerolinea']}\n\n"
        
        mensaje += "💡 Precios referenciales. Pueden variar según fecha y disponibilidad.\n\n"
        mensaje += f"Para reservar, contáctanos:\n📞 {AGENCIA_TELEFONO}\n\n"
        mensaje += "Escribe *menú* para volver al inicio."
        
        self.sheets.eliminar_sesion(telefono)
        return mensaje
    
    def _procesar_boletos_aereos(
        self,
        telefono: str,
        mensaje: str,
        sesion: Sesion,
        row_index: int
    ) -> str:
        """Procesa consultas sobre boletos aéreos."""
        # Ya se mostró la información, cualquier mensaje vuelve al menú
        self.sheets.eliminar_sesion(telefono)
        return self._menu_principal()
    
    def _mostrar_paquetes_turisticos(self) -> str:
        """Muestra los paquetes turísticos disponibles."""
        mensaje = "🎒 *Paquetes Turísticos*\n\n"
        mensaje += "Nuestros paquetes todo incluido:\n\n"
        
        for idx, paquete in enumerate(PAQUETES_TURISTICOS, 1):
            tipo_emoji = "🇨🇴" if paquete["tipo"] == "nacional" else "🌎"
            mensaje += f"{idx}️⃣ {tipo_emoji} *{paquete['nombre']}*\n"
            mensaje += f"   📍 {paquete['destino']}\n"
            mensaje += f"   📅 {paquete['duracion']}\n"
            mensaje += f"   💰 ${paquete['precio']:,} COP\n\n"
        
        mensaje += "💡 Selecciona el número del paquete para ver detalles completos.\n"
        mensaje += "\nEscribe *menú* para volver al inicio."
        return mensaje
    
    def _procesar_paquetes_turisticos(
        self,
        telefono: str,
        mensaje: str,
        sesion: Sesion,
        row_index: int
    ) -> str:
        """Procesa la selección de paquete turístico."""
        try:
            opcion = int(mensaje)
            
            if opcion < 1 or opcion > len(PAQUETES_TURISTICOS):
                return f"Opción inválida. Por favor responde con un número del 1 al {len(PAQUETES_TURISTICOS)}."
            
            paquete = PAQUETES_TURISTICOS[opcion - 1]
            self.sheets.eliminar_sesion(telefono)
            
            return self._formatear_detalle_paquete(paquete)
            
        except ValueError:
            return "Por favor responde con el número del paquete."
    
    def _formatear_detalle_paquete(self, paquete: dict) -> str:
        """Formatea los detalles completos de un paquete turístico."""
        tipo_emoji = "🇨🇴" if paquete["tipo"] == "nacional" else "🌎"
        
        mensaje = f"{tipo_emoji} *{paquete['nombre']}*\n\n"
        mensaje += f"📍 Destino: {paquete['destino']}\n"
        mensaje += f"📅 Duración: {paquete['duracion']}\n"
        mensaje += f"💰 Precio: ${paquete['precio']:,} COP por persona\n\n"
        
        mensaje += "✅ *Incluye:*\n"
        for item in paquete['incluye']:
            mensaje += f"• {item}\n"
        
        mensaje += f"\n📞 Para reservar este paquete, contáctanos:\n"
        mensaje += f"WhatsApp: {AGENCIA_TELEFONO}\n"
        mensaje += f"Horario: {AGENCIA_HORARIO}\n\n"
        
        mensaje += "💳 Aceptamos todas las formas de pago\n"
        mensaje += "📝 Cupos limitados - ¡Reserva ya!\n\n"
        mensaje += "Escribe *menú* para volver al inicio."
        
        return mensaje
    
    def _enviar_notificacion_profesional(self, telefono_cliente: str, tipo_solicitud: str) -> bool:
        """
        Envía notificación al profesional cuando un cliente solicita atención.
        
        Args:
            telefono_cliente: Número del cliente que solicita atención
            tipo_solicitud: Tipo de solicitud (ej: "Boletos aéreos", "Paquetes turísticos")
        
        Returns:
            True si se envió exitosamente, False en caso contrario
        """
        from datetime import datetime
        
        # Obtener información del cliente si existe
        try:
            cliente = self.sheets.get_cliente_por_telefono(telefono_cliente)
            nombre_cliente = cliente.nombre if cliente else "Cliente nuevo"
        except:
            nombre_cliente = "Cliente nuevo"
        
        # Formatear mensaje de notificación
        mensaje_notificacion = f"""🔔 *NUEVA SOLICITUD DE ATENCIÓN*

👤 *Cliente:* {nombre_cliente}
📱 *Teléfono:* {telefono_cliente}
📋 *Solicitud:* {tipo_solicitud}
⏰ *Hora:* {datetime.now().strftime('%d/%m/%Y %H:%M')}

Por favor, responde manualmente a este chat.

_Para reactivar el bot después, escribe: "te dejo con el bot"_"""
        
        # Intentar enviar el mensaje
        if self.whatsapp:
            try:
                logger.info(f"📤 Enviando notificación al profesional {self.professional_phone}")
                logger.info(f"Cliente: {telefono_cliente}, Solicitud: {tipo_solicitud}")
                
                # Enviar mensaje al profesional
                resultado = self.whatsapp.enviar_mensaje(self.professional_phone, mensaje_notificacion)
                
                if resultado:
                    logger.info(f"✅ Notificación enviada exitosamente al profesional")
                else:
                    logger.warning(f"⚠️ No se pudo confirmar el envío de la notificación")
                
                return resultado
            except Exception as e:
                logger.error(f"❌ Error enviando notificación al profesional: {e}")
                import traceback
                traceback.print_exc()
                return False
        else:
            # Si no hay servicio de WhatsApp, solo loguear
            logger.warning(f"⚠️ WhatsApp no disponible. Notificación no enviada.")
            logger.info(f"📋 Cliente {telefono_cliente} solicitó: {tipo_solicitud}")
            logger.info(f"📱 Profesional configurado: {self.professional_phone}")
            logger.info(f"💬 Mensaje que se enviaría:\n{mensaje_notificacion}")
            return False
    
    def _enviar_notificacion_handoff(
        self,
        telefono_cliente: str,
        nombre_cliente: str,
        tipo_solicitud: str,
        detalles: str
    ) -> bool:
        """
        Envía notificación al profesional cuando se transfiere un cliente (handoff).
        Incluye información detallada de lo que el cliente solicitó.
        
        Args:
            telefono_cliente: Número del cliente
            nombre_cliente: Nombre del cliente
            tipo_solicitud: Tipo de solicitud (ej: "Boleto Nacional", "Boleto Internacional")
            detalles: Detalles específicos de la solicitud
        
        Returns:
            True si se envió exitosamente, False en caso contrario
        """
        from datetime import datetime
        
        # Formatear mensaje de notificación con información detallada
        mensaje_notificacion = f"""🔔 *NUEVA SOLICITUD DE ATENCIÓN*

👤 *Cliente:* {nombre_cliente}
📱 *Teléfono:* {telefono_cliente}
📋 *Tipo:* {tipo_solicitud}
📍 *Detalles:* {detalles}
⏰ *Hora:* {datetime.now().strftime('%d/%m/%Y %H:%M')}

Por favor, responde manualmente a este chat.

_Para reactivar el bot después, escribe: "te dejo con el bot"_"""
        
        # Intentar enviar el mensaje
        if self.whatsapp:
            try:
                logger.info(f"📤 Enviando notificación de handoff al profesional {self.professional_phone}")
                logger.info(f"Cliente: {telefono_cliente} ({nombre_cliente})")
                logger.info(f"Solicitud: {tipo_solicitud} - {detalles}")
                
                # Enviar mensaje al profesional
                resultado = self.whatsapp.enviar_mensaje(self.professional_phone, mensaje_notificacion)
                
                if resultado:
                    logger.info(f"✅ Notificación de handoff enviada exitosamente")
                else:
                    logger.warning(f"⚠️ No se pudo confirmar el envío de la notificación de handoff")
                
                return resultado
            except Exception as e:
                logger.error(f"❌ Error enviando notificación de handoff: {e}")
                import traceback
                traceback.print_exc()
                return False
        else:
            # Si no hay servicio de WhatsApp, solo loguear
            logger.warning(f"⚠️ WhatsApp no disponible. Notificación de handoff no enviada.")
            logger.info(f"📋 Handoff: {nombre_cliente} ({telefono_cliente})")
            logger.info(f"📋 Solicitud: {tipo_solicitud} - {detalles}")
            logger.info(f"📱 Profesional configurado: {self.professional_phone}")
            logger.info(f"💬 Mensaje que se enviaría:\n{mensaje_notificacion}")
            return False
