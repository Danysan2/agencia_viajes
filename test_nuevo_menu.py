"""Script de prueba para el nuevo menú del chatbot."""

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


def mostrar_boletos_nacionales():
    """Muestra destinos nacionales."""
    return """🇨🇴 *Boletos Nacionales en Colombia*

Destinos disponibles:

1️⃣ 🏛️ Bogotá
2️⃣ 🌸 Medellín
3️⃣ 🏖️ Cartagena
4️⃣ 💃 Cali
5️⃣ 🏝️ Santa Marta

💡 Selecciona el número del destino para ver disponibilidad y precios.

Escribe *menú* para volver al inicio."""


def mostrar_boletos_internacionales():
    """Muestra destinos internacionales."""
    return """🌎 *Boletos Internacionales*

Destinos populares:

1️⃣ 🌴 Miami, USA
2️⃣ 🏖️ Cancún, México
3️⃣ 🇪🇸 Madrid, España
4️⃣ 🗼 París, Francia
5️⃣ 🥩 Buenos Aires, Argentina

💡 Selecciona el número del destino para más información.

Escribe *menú* para volver al inicio."""


def mostrar_boletos_aereos():
    """Muestra rutas aéreas populares."""
    return """✈️ *Boletos Aéreos - Rutas Populares*

🇨🇴 *Vuelos Nacionales:*

1. Bogotá → Cartagena
   💰 Desde $180.000 COP
   ⏱️ 1h 30min
   ✈️ Avianca / LATAM

2. Bogotá → Medellín
   💰 Desde $150.000 COP
   ⏱️ 1h
   ✈️ Avianca / LATAM

3. Bogotá → Cali
   💰 Desde $160.000 COP
   ⏱️ 1h 15min
   ✈️ Avianca / LATAM

🌎 *Vuelos Internacionales:*

4. Bogotá → Miami
   💰 Desde $850.000 COP
   ⏱️ 4h
   ✈️ Avianca / Copa

5. Bogotá → Cancún
   💰 Desde $750.000 COP
   ⏱️ 3h 30min
   ✈️ Avianca / Wingo

6. Bogotá → Madrid
   💰 Desde $1.800.000 COP
   ⏱️ 10h
   ✈️ Avianca / Iberia

💡 Precios referenciales. Pueden variar según fecha y disponibilidad.

Para reservar, contáctanos:
📞 +57 300 000 0000

Escribe *menú* para volver al inicio."""


def mostrar_paquetes_turisticos():
    """Muestra paquetes turísticos."""
    return """🎒 *Paquetes Turísticos*

Nuestros paquetes todo incluido:

1️⃣ 🇨🇴 *Cartagena Mágica*
   📍 Cartagena
   📅 3 días / 2 noches
   💰 $899.000 COP

2️⃣ 🇨🇴 *San Andrés Paraíso*
   📍 San Andrés
   📅 5 días / 4 noches
   💰 $1.450.000 COP

3️⃣ 🇨🇴 *Eje Cafetero Experiencia*
   📍 Eje Cafetero
   📅 4 días / 3 noches
   💰 $1.100.000 COP

4️⃣ 🌎 *Cancún Todo Incluido*
   📍 Cancún, México
   📅 5 días / 4 noches
   💰 $2.800.000 COP

5️⃣ 🌎 *Miami Shopping & Playa*
   📍 Miami, USA
   📅 6 días / 5 noches
   💰 $3.200.000 COP

💡 Selecciona el número del paquete para ver detalles completos.

Escribe *menú* para volver al inicio."""


def mostrar_detalle_paquete_cartagena():
    """Muestra detalles del paquete Cartagena."""
    return """🇨🇴 *Cartagena Mágica*

📍 Destino: Cartagena
📅 Duración: 3 días / 2 noches
💰 Precio: $899.000 COP por persona

✅ *Incluye:*
• Boletos aéreos ida y vuelta
• Hotel 4 estrellas con desayuno
• Traslados aeropuerto-hotel
• City tour por el centro histórico
• Seguro de viaje

📞 Para reservar este paquete, contáctanos:
WhatsApp: +57 300 000 0000
Horario: Lunes a sábado, 8am – 6pm

💳 Aceptamos todas las formas de pago
📝 Cupos limitados - ¡Reserva ya!

Escribe *menú* para volver al inicio."""


def test_flujo_completo():
    """Simula el flujo completo del nuevo chatbot."""
    print("=" * 70)
    print("SIMULACIÓN DEL NUEVO CHATBOT - VIAJES COLOMBIA TOURS")
    print("=" * 70)
    
    # 1. Menú principal
    print("\n📱 Usuario: hola")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # 2. Boletos nacionales
    print("\n📱 Usuario: 1")
    print("-" * 70)
    print(mostrar_boletos_nacionales())
    
    # 3. Volver al menú
    print("\n📱 Usuario: menú")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # 4. Boletos internacionales
    print("\n📱 Usuario: 2")
    print("-" * 70)
    print(mostrar_boletos_internacionales())
    
    # 5. Volver al menú
    print("\n📱 Usuario: menú")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # 6. Boletos aéreos
    print("\n📱 Usuario: 3")
    print("-" * 70)
    print(mostrar_boletos_aereos())
    
    # 7. Volver al menú
    print("\n📱 Usuario: menú")
    print("-" * 70)
    print(mostrar_menu_principal())
    
    # 8. Paquetes turísticos
    print("\n📱 Usuario: 4")
    print("-" * 70)
    print(mostrar_paquetes_turisticos())
    
    # 9. Ver detalle de paquete
    print("\n📱 Usuario: 1")
    print("-" * 70)
    print(mostrar_detalle_paquete_cartagena())
    
    print("\n" + "=" * 70)
    print("✅ SIMULACIÓN COMPLETADA EXITOSAMENTE")
    print("=" * 70)
    print("\n💡 Nuevo menú implementado:")
    print("   1. Boletos nacionales en Colombia")
    print("   2. Boletos internacionales")
    print("   3. Boletos aéreos (rutas populares)")
    print("   4. Paquetes turísticos")


if __name__ == "__main__":
    test_flujo_completo()
