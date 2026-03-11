#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test completo del sistema de handoff (transferencia a humano)."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.engine import ChatbotEngine

def test_handoff_completo():
    """Test del sistema de handoff completo."""
    print("🧪 TEST: Sistema de Handoff Completo")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    cliente = "573123456789"
    
    print(f"\n📱 Cliente: {cliente}")
    
    # Paso 1: Cliente inicia conversación
    print("\n--- PASO 1: Cliente inicia conversación ---")
    response = chatbot.procesar_mensaje(cliente, "hola")
    print(f"✅ Bot responde: {response[:80]}...")
    
    # Paso 2: Cliente selecciona destinos nacionales
    print("\n--- PASO 2: Cliente selecciona opción 1 ---")
    response = chatbot.procesar_mensaje(cliente, "1")
    print(f"✅ Bot muestra destinos: {response[:80]}...")
    
    # Paso 3: Cliente selecciona un destino
    print("\n--- PASO 3: Cliente selecciona destino 5 (Pore) ---")
    response = chatbot.procesar_mensaje(cliente, "5")
    print(f"✅ Bot confirma y desactiva: {response[:80]}...")
    
    if "Pore" not in response or "$110.000" not in response:
        print("❌ ERROR: Respuesta incorrecta")
        return False
    
    # Paso 4: Verificar que el bot está desactivado
    print("\n--- PASO 4: Cliente intenta escribir (bot desactivado) ---")
    response = chatbot.procesar_mensaje(cliente, "hola")
    
    if response is not None:
        print(f"❌ ERROR: Bot respondió cuando debería estar desactivado")
        print(f"Respuesta: {response}")
        return False
    
    print("✅ Bot correctamente desactivado (no responde)")
    
    # Paso 5: Cliente intenta reactivar (no debería funcionar en producción)
    print("\n--- PASO 5: Cliente intenta escribir más mensajes ---")
    response = chatbot.procesar_mensaje(cliente, "necesito ayuda")
    
    if response is not None:
        print(f"❌ ERROR: Bot respondió cuando debería estar desactivado")
        return False
    
    print("✅ Bot sigue desactivado")
    
    # Paso 6: Asesor reactiva el bot
    print("\n--- PASO 6: Asesor escribe 'bot' para reactivar ---")
    response = chatbot.procesar_mensaje(cliente, "bot")
    
    if response is None:
        print("❌ ERROR: Bot no se reactivó con comando 'bot'")
        return False
    
    if "Bot reactivado" not in response:
        print(f"❌ ERROR: Respuesta incorrecta al reactivar")
        print(f"Respuesta: {response[:200]}")
        return False
    
    print(f"✅ Bot reactivado correctamente: {response[:80]}...")
    
    # Paso 7: Verificar que el bot responde normalmente
    print("\n--- PASO 7: Cliente puede usar el bot de nuevo ---")
    response = chatbot.procesar_mensaje(cliente, "1")
    
    if "Boletos Nacionales" not in response:
        print("❌ ERROR: Bot no responde correctamente después de reactivarse")
        return False
    
    print("✅ Bot funciona normalmente después de reactivación")
    
    # Paso 8: Probar otros comandos de reactivación
    print("\n--- PASO 8: Probar comando 'te dejo con el bot' ---")
    
    # Desactivar bot de nuevo
    chatbot.procesar_mensaje(cliente, "1")
    chatbot.procesar_mensaje(cliente, "10")  # Seleccionar otro destino
    
    # Intentar reactivar con otro comando
    response = chatbot.procesar_mensaje(cliente, "te dejo con el bot")
    
    if response is None or "Bot reactivado" not in response:
        print("❌ ERROR: Comando 'te dejo con el bot' no funciona")
        return False
    
    print("✅ Comando 'te dejo con el bot' funciona correctamente")
    
    # Paso 9: Probar comando 'activar bot'
    print("\n--- PASO 9: Probar comando 'activar bot' ---")
    
    # Desactivar bot de nuevo
    chatbot.procesar_mensaje(cliente, "1")
    chatbot.procesar_mensaje(cliente, "15")
    
    # Reactivar con 'activar bot'
    response = chatbot.procesar_mensaje(cliente, "activar bot")
    
    if response is None or "Bot reactivado" not in response:
        print("❌ ERROR: Comando 'activar bot' no funciona")
        return False
    
    print("✅ Comando 'activar bot' funciona correctamente")
    
    print("\n\n🎉 TODOS LOS TESTS DE HANDOFF PASARON")
    print("✅ Bot se desactiva correctamente cuando cliente selecciona destino")
    print("✅ Bot no responde mientras está desactivado")
    print("✅ Comandos de reactivación funcionan:")
    print("   - 'bot'")
    print("   - 'te dejo con el bot'")
    print("   - 'activar bot'")
    print("✅ Bot funciona normalmente después de reactivación")
    print("\n⚠️  IMPORTANTE: En producción, solo el asesor debe usar los comandos de reactivación")
    
    return True

if __name__ == "__main__":
    success = test_handoff_completo()
    sys.exit(0 if success else 1)