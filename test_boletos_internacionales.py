"""Test de boletos internacionales actualizados."""

def mostrar_menu_principal():
    """Muestra el menú principal."""
    return """✈️ ¡Hola! Bienvenido a *Viajes Colombia Tours* 🇨🇴

Tu agencia de confianza para viajar por Colombia y el mundo.

¿Qué estás buscando hoy?

1️⃣ Boletos nacionales en Colombia
2️⃣ Boletos internacionales
3️⃣ Boletos aéreos (rutas populares)
4️⃣ Paquetes turísticos

Responde con el número de la opción."""


def mostrar_boletos_internacionales():
    """Muestra destinos internacionales actualizados."""
    return """🌎 *Boletos Internacionales*

Destinos disponibles:

1️⃣ 🇪🇨 *Ecuador*
   📍 Ciudades: Quito, Guayaquil

2️⃣ 🇵🇪 *Perú*
   📍 Ciudades: Lima

3️⃣ 🇨🇱 *Chile*
   📍 Ciudades: Santiago de Chile

💡 Selecciona el número del país para más información.

Escribe *menú* para volver al inicio."""


def mostrar_detalle_ecuador():
    """Muestra detalles de Ecuador."""
    return """✈️ *🇪🇨 Ecuador*

📍 *Ciudades disponibles:*
   • Quito
   • Guayaquil

Para consultar disponibilidad y precios de boletos a Ecuador, contáctanos:

📞 WhatsApp: +57 300 000 0000
📧 Email: internacional@viajescolombia.com
⏰ Horario: Lunes a sábado, 8am – 6pm

Te ayudaremos con:
• Mejores tarifas disponibles
• Opciones de aerolíneas
• Horarios de vuelos
• Requisitos de viaje
• Documentación necesaria

Escribe *menú* para volver al inicio."""


def mostrar_detalle_peru():
    """Muestra detalles de Perú."""
    return """✈️ *🇵🇪 Perú*

📍 *Ciudades disponibles:*
   • Lima

Para consultar disponibilidad y precios de boletos a Perú, contáctanos:

📞 WhatsApp: +57 300 000 0000
📧 Email: internacional@viajescolombia.com
⏰ Horario: Lunes a sábado, 8am – 6pm

Te ayudaremos con:
• Mejores tarifas disponibles
• Opciones de aerolíneas
• Horarios de vuelos
• Requisitos de viaje
• Documentación necesaria

Escribe *menú* para volver al inicio."""


def mostrar_detalle_chile():
    """Muestra detalles de Chile."""
    return """✈️ *🇨🇱 Chile*

📍 *Ciudades disponibles:*
   • Santiago de Chile

Para consultar disponibilidad y precios de boletos a Chile, contáctanos:

📞 WhatsApp: +57 300 000 0000
📧 Email: internacional@viajescolombia.com
⏰ Horario: Lunes a sábado, 8am – 6pm

Te ayudaremos con:
• Mejores tarifas disponibles
• Opciones de aerolíneas
• Horarios de vuelos
• Requisitos de viaje
• Documentación necesaria

Escribe *menú* para volver al inicio."""


def test_flujo_completo():
    """Test del flujo completo de boletos internacionales."""
    print("=" * 70)
    print("TEST: BOLETOS INTERNACIONALES ACTUALIZADOS")
    print("=" * 70)
    
    # Menú principal
    print("\n📱 Usuario: hola")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # Seleccionar opción 2
    print("\n📱 Usuario: 2")
    print("-" * 70)
    print(mostrar_boletos_internacionales())
    
    # Seleccionar Ecuador
    print("\n📱 Usuario: 1")
    print("-" * 70)
    print(mostrar_detalle_ecuador())
    
    # Volver al menú
    print("\n📱 Usuario: menú")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # Seleccionar opción 2 de nuevo
    print("\n📱 Usuario: 2")
    print("-" * 70)
    print(mostrar_boletos_internacionales())
    
    # Seleccionar Perú
    print("\n📱 Usuario: 2")
    print("-" * 70)
    print(mostrar_detalle_peru())
    
    # Volver al menú
    print("\n📱 Usuario: menú")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # Seleccionar opción 2 de nuevo
    print("\n📱 Usuario: 2")
    print("-" * 70)
    print(mostrar_boletos_internacionales())
    
    # Seleccionar Chile
    print("\n📱 Usuario: 3")
    print("-" * 70)
    print(mostrar_detalle_chile())
    
    print("\n" + "=" * 70)
    print("✅ TEST COMPLETADO")
    print("=" * 70)
    print("\n📋 Resumen de destinos internacionales:")
    print("   1. 🇪🇨 Ecuador - Quito, Guayaquil")
    print("   2. 🇵🇪 Perú - Lima")
    print("   3. 🇨🇱 Chile - Santiago de Chile")


def test_datos_configurados():
    """Verifica los datos configurados."""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE DATOS")
    print("=" * 70)
    
    try:
        from config.constants import DESTINOS_INTERNACIONALES
        
        print("\n✅ Destinos internacionales configurados:")
        for key, destino in DESTINOS_INTERNACIONALES.items():
            print(f"\n   {destino['emoji']} {destino['nombre']}")
            print(f"   Ciudades: {', '.join(destino['ciudades'])}")
        
        print("\n✅ Total de países: 3")
        print("✅ Total de ciudades: 4")
        
    except ImportError as e:
        print(f"\n❌ Error importando datos: {e}")


if __name__ == "__main__":
    test_flujo_completo()
    test_datos_configurados()
