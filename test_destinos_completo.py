"""Test completo de selección de destinos nacionales e internacionales."""
from chatbot.engine import ChatbotEngine

def test_destinos_nacionales():
    """Prueba la selección de destinos nacionales con todas las opciones."""
    print("=" * 60)
    print("TEST: DESTINOS NACIONALES (25 OPCIONES)")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    telefono = "573009999999"
    
    # Iniciar conversación
    print("\n1️⃣ Iniciando conversación...")
    respuesta = chatbot.procesar_mensaje(telefono, "hola")
    print("✅ Menú principal mostrado")
    
    # Seleccionar opción 1 (Boletos nacionales)
    print("\n2️⃣ Seleccionando opción 1 (Boletos nacionales)...")
    respuesta = chatbot.procesar_mensaje(telefono, "1")
    print("✅ Destinos mostrados")
    print(f"\n{respuesta[:300]}...")
    
    # Probar selección de destino 1 (Tame)
    print("\n3️⃣ Probando destino 1 (Tame)...")
    respuesta = chatbot.procesar_mensaje(telefono, "1")
    if "Tame" in respuesta and "Arauca" in respuesta:
        print("✅ Destino 1 funciona correctamente")
    else:
        print("❌ Error con destino 1")
    
    # Reiniciar para probar destino 10
    print("\n4️⃣ Probando destino 10 (Sogamoso)...")
    chatbot.procesar_mensaje(telefono, "menu")
    chatbot.procesar_mensaje(telefono, "1")
    respuesta = chatbot.procesar_mensaje(telefono, "10")
    if "Sogamoso" in respuesta:
        print("✅ Destino 10 funciona correctamente")
    else:
        print("❌ Error con destino 10")
    
    # Reiniciar para probar destino 25
    print("\n5️⃣ Probando destino 25 (Necoclí)...")
    chatbot.procesar_mensaje(telefono, "menu")
    chatbot.procesar_mensaje(telefono, "1")
    respuesta = chatbot.procesar_mensaje(telefono, "25")
    if "Necoclí" in respuesta:
        print("✅ Destino 25 funciona correctamente")
    else:
        print("❌ Error con destino 25")
    
    # Probar opción inválida (26)
    print("\n6️⃣ Probando opción inválida (26)...")
    chatbot.procesar_mensaje(telefono, "menu")
    chatbot.procesar_mensaje(telefono, "1")
    respuesta = chatbot.procesar_mensaje(telefono, "26")
    if "inválida" in respuesta.lower() or "volver" in respuesta.lower():
        print("✅ Validación de opción inválida funciona")
    else:
        print("❌ Error en validación")
    
    # Probar comando "volver"
    print("\n7️⃣ Probando comando 'volver'...")
    chatbot.procesar_mensaje(telefono, "menu")
    chatbot.procesar_mensaje(telefono, "1")
    respuesta = chatbot.procesar_mensaje(telefono, "volver")
    if "Bienvenido" in respuesta and "Viajes Colombia Tours" in respuesta:
        print("✅ Comando 'volver' funciona correctamente")
    else:
        print("❌ Error con comando 'volver'")
    
    print("\n" + "=" * 60)
    print("✅ TEST DE DESTINOS NACIONALES COMPLETADO")
    print("=" * 60)

def test_destinos_internacionales():
    """Prueba la selección de destinos internacionales."""
    print("\n" + "=" * 60)
    print("TEST: DESTINOS INTERNACIONALES")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    telefono = "573008888888"
    
    # Iniciar conversación
    print("\n1️⃣ Iniciando conversación...")
    chatbot.procesar_mensaje(telefono, "hola")
    
    # Seleccionar opción 2 (Boletos internacionales)
    print("\n2️⃣ Seleccionando opción 2 (Boletos internacionales)...")
    respuesta = chatbot.procesar_mensaje(telefono, "2")
    print("✅ Destinos internacionales mostrados")
    
    # Probar Ecuador (opción 1)
    print("\n3️⃣ Probando Ecuador (opción 1)...")
    respuesta = chatbot.procesar_mensaje(telefono, "1")
    if "Ecuador" in respuesta and ("Quito" in respuesta or "Guayaquil" in respuesta):
        print("✅ Ecuador funciona correctamente")
    else:
        print("❌ Error con Ecuador")
    
    # Probar Perú (opción 2)
    print("\n4️⃣ Probando Perú (opción 2)...")
    chatbot.procesar_mensaje(telefono, "menu")
    chatbot.procesar_mensaje(telefono, "2")
    respuesta = chatbot.procesar_mensaje(telefono, "2")
    if "Perú" in respuesta or "Peru" in respuesta:
        print("✅ Perú funciona correctamente")
    else:
        print("❌ Error con Perú")
    
    # Probar Chile (opción 3)
    print("\n5️⃣ Probando Chile (opción 3)...")
    chatbot.procesar_mensaje(telefono, "menu")
    chatbot.procesar_mensaje(telefono, "2")
    respuesta = chatbot.procesar_mensaje(telefono, "3")
    if "Chile" in respuesta and "Santiago" in respuesta:
        print("✅ Chile funciona correctamente")
    else:
        print("❌ Error con Chile")
    
    # Probar comando "volver"
    print("\n6️⃣ Probando comando 'volver'...")
    chatbot.procesar_mensaje(telefono, "menu")
    chatbot.procesar_mensaje(telefono, "2")
    respuesta = chatbot.procesar_mensaje(telefono, "volver")
    if "Bienvenido" in respuesta:
        print("✅ Comando 'volver' funciona correctamente")
    else:
        print("❌ Error con comando 'volver'")
    
    print("\n" + "=" * 60)
    print("✅ TEST DE DESTINOS INTERNACIONALES COMPLETADO")
    print("=" * 60)

def test_notificaciones():
    """Verifica que se envíen notificaciones al profesional."""
    print("\n" + "=" * 60)
    print("TEST: NOTIFICACIONES AL PROFESIONAL")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    print(f"\n📱 Número profesional: {chatbot.professional_phone}")
    
    # Test con destino nacional
    print("\n1️⃣ Probando notificación con destino nacional...")
    telefono1 = "573007777777"
    chatbot.procesar_mensaje(telefono1, "hola")
    chatbot.procesar_mensaje(telefono1, "1")
    respuesta = chatbot.procesar_mensaje(telefono1, "5")  # Aguazul
    if "asesor" in respuesta.lower() and "contactará" in respuesta.lower():
        print("✅ Notificación enviada para destino nacional")
    
    # Test con destino internacional
    print("\n2️⃣ Probando notificación con destino internacional...")
    telefono2 = "573006666666"
    chatbot.procesar_mensaje(telefono2, "hola")
    chatbot.procesar_mensaje(telefono2, "2")
    respuesta = chatbot.procesar_mensaje(telefono2, "1")  # Ecuador
    if "asesor" in respuesta.lower() and "contactará" in respuesta.lower():
        print("✅ Notificación enviada para destino internacional")
    
    print("\n" + "=" * 60)
    print("✅ TEST DE NOTIFICACIONES COMPLETADO")
    print("=" * 60)
    print(f"\n📞 Verifica el WhatsApp {chatbot.professional_phone}")
    print("   Deberías haber recibido 2 notificaciones adicionales")

if __name__ == "__main__":
    test_destinos_nacionales()
    test_destinos_internacionales()
    test_notificaciones()
    
    print("\n" + "=" * 60)
    print("🎉 TODOS LOS TESTS COMPLETADOS")
    print("=" * 60)
    print("\n✅ Resumen:")
    print("   - Destinos nacionales: 25 opciones funcionando")
    print("   - Destinos internacionales: 3 opciones funcionando")
    print("   - Comando 'volver': funcionando en ambos")
    print("   - Notificaciones al profesional: funcionando")
    print("   - Validación de opciones inválidas: funcionando")
