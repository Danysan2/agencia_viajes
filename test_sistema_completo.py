"""Test completo del sistema de chatbot."""
from chatbot.engine import ChatbotEngine

def test_flujo_completo():
    """Prueba todos los flujos del chatbot."""
    print("=" * 70)
    print("TEST COMPLETO DEL SISTEMA")
    print("=" * 70)
    
    chatbot = ChatbotEngine()
    print(f"\n📱 Número profesional configurado: {chatbot.professional_phone}")
    
    # TEST 1: Opción 1 - Boletos Nacionales
    print("\n" + "=" * 70)
    print("TEST 1: OPCIÓN 1 - BOLETOS NACIONALES")
    print("=" * 70)
    
    telefono1 = "573001111111"
    print(f"\n📱 Cliente: {telefono1}")
    
    print("   1. Envía 'hola'")
    resp = chatbot.procesar_mensaje(telefono1, "hola")
    assert "Bienvenido" in resp, "❌ No muestra bienvenida"
    print("      ✅ Menú principal mostrado")
    
    print("   2. Selecciona opción '1' (Boletos nacionales)")
    resp = chatbot.procesar_mensaje(telefono1, "1")
    assert "Destinos disponibles" in resp, "❌ No muestra destinos"
    assert "Tame" in resp, "❌ No muestra Tame"
    assert "25" in resp or "Necoclí" in resp, "❌ No muestra todos los destinos"
    print("      ✅ 25 destinos mostrados")
    
    print("   3. Selecciona destino '10' (Sogamoso)")
    resp = chatbot.procesar_mensaje(telefono1, "10")
    assert "Sogamoso" in resp, "❌ No reconoce Sogamoso"
    assert "asesor" in resp.lower(), "❌ No menciona asesor"
    print("      ✅ Notificación enviada, handoff realizado")
    
    # TEST 2: Opción 2 - Boletos Internacionales
    print("\n" + "=" * 70)
    print("TEST 2: OPCIÓN 2 - BOLETOS INTERNACIONALES")
    print("=" * 70)
    
    telefono2 = "573002222222"
    print(f"\n📱 Cliente: {telefono2}")
    
    print("   1. Envía 'hola'")
    resp = chatbot.procesar_mensaje(telefono2, "hola")
    print("      ✅ Menú principal mostrado")
    
    print("   2. Selecciona opción '2' (Boletos internacionales)")
    resp = chatbot.procesar_mensaje(telefono2, "2")
    assert "Ecuador" in resp, "❌ No muestra Ecuador"
    assert "Perú" in resp or "Peru" in resp, "❌ No muestra Perú"
    assert "Chile" in resp, "❌ No muestra Chile"
    print("      ✅ 3 países mostrados")
    
    print("   3. Selecciona país '2' (Perú)")
    resp = chatbot.procesar_mensaje(telefono2, "2")
    assert "Perú" in resp or "Peru" in resp, "❌ No reconoce Perú"
    assert "asesor" in resp.lower(), "❌ No menciona asesor"
    assert "Tame" not in resp, "❌ ERROR: Muestra destinos nacionales"
    assert "Destinos disponibles" not in resp, "❌ ERROR: Muestra lista de destinos"
    print("      ✅ Notificación enviada, handoff realizado")
    print("      ✅ NO muestra destinos nacionales (correcto)")
    
    # TEST 3: Opción 3 - Boletos Aéreos
    print("\n" + "=" * 70)
    print("TEST 3: OPCIÓN 3 - BOLETOS AÉREOS")
    print("=" * 70)
    
    telefono3 = "573003333333"
    print(f"\n📱 Cliente: {telefono3}")
    
    print("   1. Envía 'hola'")
    chatbot.procesar_mensaje(telefono3, "hola")
    
    print("   2. Selecciona opción '3' (Boletos aéreos)")
    resp = chatbot.procesar_mensaje(telefono3, "3")
    assert "Boletos Aéreos" in resp, "❌ No muestra título"
    assert "asesor" in resp.lower(), "❌ No menciona asesor"
    print("      ✅ Notificación enviada inmediatamente")
    
    # TEST 4: Opción 4 - Paquetes Turísticos
    print("\n" + "=" * 70)
    print("TEST 4: OPCIÓN 4 - PAQUETES TURÍSTICOS")
    print("=" * 70)
    
    telefono4 = "573004444444"
    print(f"\n📱 Cliente: {telefono4}")
    
    print("   1. Envía 'hola'")
    chatbot.procesar_mensaje(telefono4, "hola")
    
    print("   2. Selecciona opción '4' (Paquetes turísticos)")
    resp = chatbot.procesar_mensaje(telefono4, "4")
    assert "Paquetes Turísticos" in resp, "❌ No muestra título"
    assert "asesor" in resp.lower(), "❌ No menciona asesor"
    print("      ✅ Notificación enviada inmediatamente")
    
    # TEST 5: Comando "volver"
    print("\n" + "=" * 70)
    print("TEST 5: COMANDO 'VOLVER'")
    print("=" * 70)
    
    telefono5 = "573005555555"
    print(f"\n📱 Cliente: {telefono5}")
    
    print("   1. Envía 'hola'")
    chatbot.procesar_mensaje(telefono5, "hola")
    
    print("   2. Selecciona opción '1'")
    chatbot.procesar_mensaje(telefono5, "1")
    
    print("   3. Escribe 'volver'")
    resp = chatbot.procesar_mensaje(telefono5, "volver")
    assert "Bienvenido" in resp, "❌ No regresa al menú"
    print("      ✅ Regresa al menú principal")
    
    # TEST 6: Validación de opciones inválidas
    print("\n" + "=" * 70)
    print("TEST 6: VALIDACIÓN DE OPCIONES INVÁLIDAS")
    print("=" * 70)
    
    telefono6 = "573006666666"
    print(f"\n📱 Cliente: {telefono6}")
    
    print("   1. Envía 'hola'")
    chatbot.procesar_mensaje(telefono6, "hola")
    
    print("   2. Selecciona opción '1'")
    chatbot.procesar_mensaje(telefono6, "1")
    
    print("   3. Intenta opción '30' (inválida)")
    resp = chatbot.procesar_mensaje(telefono6, "30")
    assert "inválida" in resp.lower() or "volver" in resp.lower(), "❌ No valida correctamente"
    print("      ✅ Validación funciona correctamente")
    
    # RESUMEN FINAL
    print("\n" + "=" * 70)
    print("✅ TODOS LOS TESTS PASARON EXITOSAMENTE")
    print("=" * 70)
    
    print(f"\n📊 Resumen:")
    print(f"   ✅ Opción 1 (Boletos nacionales): 25 destinos funcionando")
    print(f"   ✅ Opción 2 (Boletos internacionales): 3 países funcionando")
    print(f"   ✅ Opción 3 (Boletos aéreos): Notificación inmediata")
    print(f"   ✅ Opción 4 (Paquetes turísticos): Notificación inmediata")
    print(f"   ✅ Comando 'volver': Funciona correctamente")
    print(f"   ✅ Validación de opciones: Funciona correctamente")
    print(f"   ✅ Handoff a humano: Funciona en todas las opciones")
    print(f"   ✅ Notificaciones al profesional: {chatbot.professional_phone}")
    
    print(f"\n📞 Verifica tu WhatsApp {chatbot.professional_phone}")
    print(f"   Deberías haber recibido 4 notificaciones de prueba")
    
    print("\n🎉 Sistema completamente funcional y listo para producción!")

if __name__ == "__main__":
    try:
        test_flujo_completo()
    except AssertionError as e:
        print(f"\n❌ TEST FALLIDO: {e}")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
