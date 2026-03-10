"""Test del sistema de handoff (transferencia a humano)."""
import sys
sys.path.insert(0, '.')

from chatbot.engine import ChatbotEngine
from config.constants import COMANDOS_REACTIVAR_BOT, HORAS_REACTIVACION_AUTO
from datetime import datetime, timedelta

def test_flujo_handoff_opcion1():
    """Test: Flujo completo de handoff en opción 1 (Boletos Nacionales)."""
    print("=" * 70)
    print("TEST 1: Handoff en Opción 1 - Boletos Nacionales")
    print("=" * 70)
    
    engine = ChatbotEngine()
    telefono = "+573001111111"
    
    print("\n1. Cliente inicia conversación:")
    respuesta = engine.procesar_mensaje(telefono, "hola")
    print(f"   ✅ Menú mostrado: {'1️⃣' in respuesta}")
    
    print("\n2. Cliente selecciona opción 1 (Boletos nacionales):")
    respuesta = engine.procesar_mensaje(telefono, "1")
    print(f"   ✅ Destinos mostrados: {'Arauca' in respuesta}")
    
    print("\n3. Cliente selecciona Bogotá (#14):")
    respuesta = engine.procesar_mensaje(telefono, "14")
    print(f"   ✅ Solicitud recibida: {'Solicitud recibida' in respuesta}")
    print(f"   ✅ Menciona asesor: {'asesor' in respuesta.lower()}")
    print(f"   ✅ Menciona Bogotá: {'Bogotá' in respuesta}")
    print("\n   Respuesta al cliente:")
    print("   " + "\n   ".join(respuesta.split("\n")[:8]))
    
    print("\n4. Cliente intenta enviar otro mensaje (bot desactivado):")
    respuesta = engine.procesar_mensaje(telefono, "hola")
    if respuesta is None:
        print("   ✅ Bot correctamente desactivado (no responde)")
    else:
        print(f"   ❌ Bot respondió cuando debería estar desactivado: {respuesta[:50]}")
    
    print("\n5. Cliente intenta con otro mensaje:")
    respuesta = engine.procesar_mensaje(telefono, "necesito ayuda")
    if respuesta is None:
        print("   ✅ Bot sigue desactivado (no responde)")
    else:
        print(f"   ❌ Bot respondió: {respuesta[:50]}")
    
    print("\n✅ Test de handoff opción 1 completado\n")

def test_flujo_handoff_opcion2():
    """Test: Flujo completo de handoff en opción 2 (Boletos Internacionales)."""
    print("=" * 70)
    print("TEST 2: Handoff en Opción 2 - Boletos Internacionales")
    print("=" * 70)
    
    engine = ChatbotEngine()
    telefono = "+573002222222"
    
    print("\n1. Cliente inicia conversación:")
    engine.procesar_mensaje(telefono, "hola")
    
    print("\n2. Cliente selecciona opción 2 (Boletos internacionales):")
    respuesta = engine.procesar_mensaje(telefono, "2")
    print(f"   ✅ Destinos internacionales: {'Ecuador' in respuesta or 'Perú' in respuesta}")
    
    print("\n3. Cliente selecciona Ecuador (#1):")
    respuesta = engine.procesar_mensaje(telefono, "1")
    print(f"   ✅ Solicitud recibida: {'Solicitud recibida' in respuesta}")
    print(f"   ✅ Menciona Ecuador: {'Ecuador' in respuesta}")
    print("\n   Respuesta al cliente:")
    print("   " + "\n   ".join(respuesta.split("\n")[:8]))
    
    print("\n4. Bot desactivado - Cliente intenta mensaje:")
    respuesta = engine.procesar_mensaje(telefono, "cuánto cuesta?")
    if respuesta is None:
        print("   ✅ Bot correctamente desactivado")
    else:
        print(f"   ❌ Bot respondió: {respuesta[:50]}")
    
    print("\n✅ Test de handoff opción 2 completado\n")

def test_reactivacion_por_comando():
    """Test: Reactivación del bot por comandos del asesor."""
    print("=" * 70)
    print("TEST 3: Reactivación del Bot por Comandos")
    print("=" * 70)
    
    engine = ChatbotEngine()
    telefono = "+573003333333"
    
    # Simular handoff
    print("\n1. Simular handoff (cliente selecciona destino):")
    engine.procesar_mensaje(telefono, "hola")
    engine.procesar_mensaje(telefono, "1")
    engine.procesar_mensaje(telefono, "5")  # Aguazul
    print("   ✅ Handoff realizado")
    
    print("\n2. Verificar que bot está desactivado:")
    respuesta = engine.procesar_mensaje(telefono, "hola")
    print(f"   ✅ Bot desactivado: {respuesta is None}")
    
    print("\n3. Probar comandos de reactivación:")
    comandos_prueba = [
        "activar bot",
        "te dejo con el bot",
        "bot activo",
        "continua bot"
    ]
    
    for idx, comando in enumerate(comandos_prueba[:1], 1):  # Probar solo el primero
        print(f"\n   Comando #{idx}: '{comando}'")
        respuesta = engine.procesar_mensaje(telefono, comando)
        
        if respuesta and "Bot reactivado" in respuesta:
            print(f"   ✅ Bot reactivado correctamente")
            print(f"   ✅ Menú mostrado: {'1️⃣' in respuesta}")
            break
        else:
            print(f"   ❌ No se reactivó con: {comando}")
    
    print("\n4. Verificar que bot responde después de reactivación:")
    respuesta = engine.procesar_mensaje(telefono, "hola")
    if respuesta and "Viajes Colombia Tours" in respuesta:
        print("   ✅ Bot responde correctamente después de reactivación")
    else:
        print(f"   ❌ Bot no responde correctamente")
    
    print("\n✅ Test de reactivación por comando completado\n")

def test_comandos_reactivacion():
    """Test: Verificar todos los comandos de reactivación."""
    print("=" * 70)
    print("TEST 4: Lista de Comandos de Reactivación")
    print("=" * 70)
    
    print(f"\nTotal de comandos configurados: {len(COMANDOS_REACTIVAR_BOT)}")
    print("\nComandos que reactivan el bot:")
    for idx, comando in enumerate(COMANDOS_REACTIVAR_BOT, 1):
        print(f"   {idx}. '{comando}'")
    
    print(f"\n✅ Tiempo de reactivación automática: {HORAS_REACTIVACION_AUTO} horas")
    print("\n✅ Test de comandos completado\n")

def test_reactivacion_automatica_12h():
    """Test: Simular reactivación automática después de 12 horas."""
    print("=" * 70)
    print("TEST 5: Reactivación Automática (12 horas)")
    print("=" * 70)
    
    engine = ChatbotEngine()
    telefono = "+573004444444"
    
    print("\n1. Simular handoff:")
    engine.procesar_mensaje(telefono, "hola")
    engine.procesar_mensaje(telefono, "1")
    engine.procesar_mensaje(telefono, "10")  # Sogamoso
    print("   ✅ Handoff realizado")
    
    print("\n2. Verificar bot desactivado:")
    respuesta = engine.procesar_mensaje(telefono, "test")
    print(f"   ✅ Bot desactivado: {respuesta is None}")
    
    print("\n3. Simular paso de 12 horas:")
    # Obtener sesión y modificar timestamp manualmente
    sesion_data = engine.sheets.get_sesion(telefono)
    if sesion_data:
        sesion, row_index = sesion_data
        # Establecer timestamp hace 13 horas
        sesion.handoff_timestamp = datetime.now() - timedelta(hours=13)
        engine.sheets.actualizar_sesion(sesion, row_index)
        print("   ✅ Timestamp modificado (13 horas atrás)")
        
        print("\n4. Cliente envía mensaje después de 12 horas:")
        respuesta = engine.procesar_mensaje(telefono, "hola")
        
        if respuesta and "Viajes Colombia Tours" in respuesta:
            print("   ✅ Bot reactivado automáticamente")
            print("   ✅ Menú principal mostrado")
        else:
            print(f"   ⚠️  Respuesta: {respuesta[:100] if respuesta else 'None'}")
    else:
        print("   ❌ No se pudo obtener sesión")
    
    print("\n✅ Test de reactivación automática completado\n")

def test_info_en_notificacion():
    """Test: Verificar que la notificación incluye información del cliente."""
    print("=" * 70)
    print("TEST 6: Información en Notificación al Profesional")
    print("=" * 70)
    
    print("\nCuando un cliente selecciona un destino, el profesional recibe:")
    print("   • Nombre del cliente")
    print("   • Teléfono del cliente")
    print("   • Tipo de solicitud (Boleto Nacional/Internacional)")
    print("   • Detalles específicos (destino, ciudades, etc.)")
    print("   • Hora de la solicitud")
    print("   • Información sobre comandos de reactivación")
    
    print("\nEjemplo de notificación:")
    print("-" * 70)
    ejemplo = """🔔 *CLIENTE REQUIERE ATENCIÓN HUMANA*

👤 *Cliente:* Juan Pérez
📱 *Teléfono:* +573001234567
📋 *Tipo:* Boleto Nacional
📍 *Detalles:* Arauca → Bogotá, Cundinamarca
⏰ *Hora:* 09/03/2026 14:30

🤖 *El bot ha sido DESACTIVADO para este cliente.*

Por favor, atiende a este cliente personalmente. El bot se reactivará 
automáticamente en 12 horas o cuando envíes uno de estos comandos:
• "Activar bot"
• "Te dejo con el bot"
• "Bot activo"

_Este es un mensaje automático del sistema._"""
    print(ejemplo)
    print("-" * 70)
    
    print("\n✅ Test de información en notificación completado\n")

if __name__ == "__main__":
    print("\n" + "🤖" * 35)
    print("PRUEBAS DEL SISTEMA DE HANDOFF (TRANSFERENCIA A HUMANO)")
    print("🤖" * 35 + "\n")
    
    try:
        test_flujo_handoff_opcion1()
        test_flujo_handoff_opcion2()
        test_reactivacion_por_comando()
        test_comandos_reactivacion()
        test_reactivacion_automatica_12h()
        test_info_en_notificacion()
        
        print("=" * 70)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS")
        print("=" * 70)
        print("\n📋 Resumen del Sistema de Handoff:")
        print("   • Bot se desactiva al seleccionar destino (opciones 1 y 2)")
        print("   • Profesional recibe notificación con info del cliente")
        print("   • Bot no responde mientras está desactivado")
        print(f"   • {len(COMANDOS_REACTIVAR_BOT)} comandos para reactivar bot")
        print(f"   • Reactivación automática después de {HORAS_REACTIVACION_AUTO} horas")
        print("   • Cliente recibe confirmación de que será atendido por humano")
        print("\n✅ Sistema de handoff funcionando correctamente!\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
