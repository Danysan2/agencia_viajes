"""Test completo del sistema de notificaciones al profesional."""
from chatbot.engine import ChatbotEngine

def test_notificacion_completa():
    """Prueba el flujo completo de notificación al profesional."""
    print("=" * 60)
    print("TEST COMPLETO DE NOTIFICACIONES")
    print("=" * 60)
    
    # Crear instancia del chatbot
    print("\n1️⃣ Inicializando chatbot...")
    chatbot = ChatbotEngine()
    print(f"✅ Chatbot inicializado")
    print(f"📱 Número profesional configurado: {chatbot.professional_phone}")
    
    # Simular cliente que solicita boletos aéreos (opción 3)
    print("\n2️⃣ Simulando cliente que solicita Boletos Aéreos...")
    print("-" * 60)
    
    telefono_cliente = "573001111111"  # Número de prueba
    
    # Primer mensaje - menú principal
    print(f"\n📱 Cliente {telefono_cliente}: 'hola'")
    respuesta1 = chatbot.procesar_mensaje(telefono_cliente, "hola")
    print(f"🤖 Bot: {respuesta1[:100]}...")
    
    # Segundo mensaje - seleccionar opción 3 (Boletos aéreos)
    print(f"\n📱 Cliente {telefono_cliente}: '3'")
    respuesta2 = chatbot.procesar_mensaje(telefono_cliente, "3")
    print(f"🤖 Bot: {respuesta2[:200]}...")
    
    print("\n" + "=" * 60)
    print("✅ TEST COMPLETADO")
    print("=" * 60)
    print(f"\n📞 Verifica el WhatsApp {chatbot.professional_phone}")
    print("   Deberías haber recibido una notificación con:")
    print("   - Teléfono del cliente: 573001111111")
    print("   - Solicitud: Boletos aéreos")
    print("   - Hora de la solicitud")
    
    # Probar también con opción 4 (Paquetes turísticos)
    print("\n" + "=" * 60)
    print("3️⃣ Probando con Paquetes Turísticos (opción 4)...")
    print("-" * 60)
    
    telefono_cliente2 = "573002222222"
    
    print(f"\n📱 Cliente {telefono_cliente2}: 'menu'")
    respuesta3 = chatbot.procesar_mensaje(telefono_cliente2, "menu")
    
    print(f"\n📱 Cliente {telefono_cliente2}: '4'")
    respuesta4 = chatbot.procesar_mensaje(telefono_cliente2, "4")
    print(f"🤖 Bot: {respuesta4[:200]}...")
    
    print("\n" + "=" * 60)
    print("✅ SEGUNDO TEST COMPLETADO")
    print("=" * 60)
    print(f"\n📞 Verifica el WhatsApp {chatbot.professional_phone}")
    print("   Deberías haber recibido otra notificación con:")
    print("   - Teléfono del cliente: 573002222222")
    print("   - Solicitud: Paquetes turísticos")
    
    # Probar con destino nacional (opción 1 -> seleccionar destino)
    print("\n" + "=" * 60)
    print("4️⃣ Probando con Boleto Nacional (opción 1)...")
    print("-" * 60)
    
    telefono_cliente3 = "573003333333"
    
    print(f"\n📱 Cliente {telefono_cliente3}: 'hola'")
    chatbot.procesar_mensaje(telefono_cliente3, "hola")
    
    print(f"\n📱 Cliente {telefono_cliente3}: '1' (Boletos nacionales)")
    respuesta5 = chatbot.procesar_mensaje(telefono_cliente3, "1")
    print(f"🤖 Bot muestra destinos...")
    
    print(f"\n📱 Cliente {telefono_cliente3}: '1' (Selecciona Tame)")
    respuesta6 = chatbot.procesar_mensaje(telefono_cliente3, "1")
    print(f"🤖 Bot: {respuesta6[:200]}...")
    
    print("\n" + "=" * 60)
    print("✅ TERCER TEST COMPLETADO")
    print("=" * 60)
    print(f"\n📞 Verifica el WhatsApp {chatbot.professional_phone}")
    print("   Deberías haber recibido una tercera notificación con:")
    print("   - Teléfono del cliente: 573003333333")
    print("   - Solicitud: Boleto Nacional")
    print("   - Detalles: Arauca → Tame, Arauca")
    
    print("\n" + "=" * 60)
    print("🎉 TODOS LOS TESTS COMPLETADOS")
    print("=" * 60)
    print(f"\n📱 Total de notificaciones enviadas: 3")
    print(f"📞 Todas al número: {chatbot.professional_phone}")
    print("\n💡 Si recibiste las 3 notificaciones, el sistema funciona perfectamente!")

if __name__ == "__main__":
    test_notificacion_completa()
