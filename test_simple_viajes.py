"""Script de prueba simple para verificar la estructura del chatbot."""

def mostrar_menu_principal():
    """Muestra el menú principal."""
    return """✈️ ¡Hola! Bienvenido a *Viajes Colombia Tours* 🇨🇴

Es un gusto tenerte aquí. Somos tu agencia de confianza para descubrir los destinos más increíbles de nuestro país.

¿En qué te podemos ayudar hoy? Elige una opción:

1️⃣ Conocer nuestros destinos en Colombia
2️⃣ Información sobre nosotros
3️⃣ Hablar con un asesor
4️⃣ Ver promociones y ofertas especiales

Responde con el número de la opción."""


def mostrar_destinos():
    """Muestra los destinos disponibles."""
    return """🗺️ ¡Excelente elección! Colombia tiene destinos increíbles para ti.

¿A cuál de estos lugares te gustaría viajar?

1️⃣ Bogotá 🏛️
2️⃣ Medellín 🌸
3️⃣ Cartagena 🏖️
4️⃣ Arauca 🌾

Responde con el número del destino."""


def mostrar_hoteles_cartagena():
    """Muestra hoteles de Cartagena."""
    return """🏖️ *Cartagena* te espera con estos hoteles disponibles:

1️⃣ Hotel Muralla Real
2️⃣ Hotel Caribe Boutique
3️⃣ Hotel Playa Dorada

¿Cuál te llama la atención? Responde con el número."""


def mostrar_detalle_hotel_muralla():
    """Muestra detalles del Hotel Muralla Real."""
    return """🏨 *Hotel Muralla Real – Cartagena*

✅ Incluye:
• Desayuno buffet para 2 personas
• Habitación doble con vista al mar
• Acceso a piscina y spa
• Wi-Fi de alta velocidad
• Traslado aeropuerto - hotel

💰 *Precio por noche:* $350.000 COP
📅 Disponibilidad: Todo el año

¿Te interesa este plan o quieres ver otro hotel?

Escribe *menú* para volver al inicio o *3* para hablar con un asesor."""


def mostrar_promociones():
    """Muestra las promociones."""
    return """🔥 *Promociones y Ofertas Especiales* 🔥

🎉 *Oferta 1 – Cartagena Express*
Paquete 3 noches para 2 personas
✅ Hotel + Desayuno + Traslados
💰 Antes: $1.200.000 | *Ahora: $899.000 COP*

🎉 *Oferta 2 – Medellín City Tour*
Paquete 2 noches con recorrido por la ciudad
✅ Hotel + City Tour + Cena romántica
💰 Antes: $900.000 | *Ahora: $650.000 COP*

⏳ Ofertas válidas hasta el 31 de marzo de 2026

¿Te interesa alguna? Escríbenos o habla con un asesor.
¿Volver al menú? Escribe *menú*"""


def mostrar_informacion_agencia():
    """Muestra información de la agencia."""
    return """🏢 *Sobre Viajes Colombia Tours*

¡Llevamos más de 8 años conectando a los colombianos con los destinos más hermosos del país! 🇨🇴

🌟 *¿Qué ofrecemos?*
• Paquetes turísticos nacionales todo incluido
• Asesoría personalizada sin costo
• Planes para familias, parejas y grupos
• Hoteles seleccionados y verificados
• Acompañamiento antes, durante y después del viaje

📍 *Sede principal:* Bogotá, Colombia
⏰ *Horario de atención:* Lunes a sábado, 8am – 6pm
📞 *Línea directa:* +57 300 000 0000

¿Deseas volver al menú principal? Escribe *menú*"""


def test_flujo_completo():
    """Simula el flujo completo del chatbot."""
    print("=" * 70)
    print("SIMULACIÓN DEL CHATBOT - VIAJES COLOMBIA TOURS")
    print("=" * 70)
    
    # 1. Menú principal
    print("\n📱 Usuario: hola")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # 2. Ver destinos
    print("\n📱 Usuario: 1")
    print("-" * 70)
    print(mostrar_destinos())
    
    # 3. Seleccionar Cartagena
    print("\n📱 Usuario: 3")
    print("-" * 70)
    print(mostrar_hoteles_cartagena())
    
    # 4. Ver Hotel Muralla Real
    print("\n📱 Usuario: 1")
    print("-" * 70)
    print(mostrar_detalle_hotel_muralla())
    
    # 5. Volver al menú
    print("\n📱 Usuario: menú")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # 6. Ver promociones
    print("\n📱 Usuario: 4")
    print("-" * 70)
    print(mostrar_promociones())
    
    # 7. Volver y ver información
    print("\n📱 Usuario: menú")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    print("\n📱 Usuario: 2")
    print("-" * 70)
    print(mostrar_informacion_agencia())
    
    print("\n" + "=" * 70)
    print("✅ SIMULACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 70)
    print("\n💡 Este es el flujo que experimentarán los usuarios por WhatsApp")
    print("💡 Para probar con el sistema real, instala las dependencias:")
    print("   pip install -r requirements.txt")
    print("   python test_chatbot_viajes.py")


if __name__ == "__main__":
    test_flujo_completo()
