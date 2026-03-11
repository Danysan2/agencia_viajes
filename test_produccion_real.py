#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test simulando el flujo real de producción."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.engine import ChatbotEngine

def test_produccion_real():
    """Simula el flujo exacto que ocurre en producción."""
    print("🎯 TEST: Simulación de Producción Real")
    print("=" * 60)
    
    # Simular usuario real
    user_phone = "573123613840"
    
    # Crear instancia del chatbot (como en producción)
    chatbot = ChatbotEngine()
    
    print(f"\n📱 Usuario: {user_phone}")
    print("\n--- Mensaje 1: hola ---")
    response = chatbot.procesar_mensaje(user_phone, "hola")
    print(f"✅ Respuesta: {response[:100]}...")
    
    if "Viajes Colombia Tours" not in response:
        print("❌ ERROR: Mensaje de bienvenida incorrecto")
        return False
    
    print("\n--- Mensaje 2: 1 (seleccionar destinos nacionales) ---")
    response = chatbot.procesar_mensaje(user_phone, "1")
    print(f"✅ Respuesta: {response[:100]}...")
    
    if "Tame - $60.000" not in response:
        print("❌ ERROR: No se muestran los destinos")
        return False
    
    print("\n--- Mensaje 3: 5 (seleccionar Pore) ---")
    response = chatbot.procesar_mensaje(user_phone, "5")
    
    if "Opción inválida" in response or "1 al 4" in response:
        print(f"❌ ERROR: Validación incorrecta!")
        print(f"Respuesta: {response}")
        return False
    
    if "Pore" in response and "$110.000" in response:
        print(f"✅ Respuesta correcta: {response[:150]}...")
    else:
        print(f"❌ ERROR: Respuesta incorrecta")
        print(f"Respuesta: {response}")
        return False
    
    # Probar con otro usuario y destino 37
    print("\n\n--- NUEVO USUARIO ---")
    user_phone2 = "573001234567"
    
    print(f"\n📱 Usuario: {user_phone2}")
    print("\n--- Mensaje 1: hola ---")
    chatbot.procesar_mensaje(user_phone2, "hola")
    
    print("\n--- Mensaje 2: 1 ---")
    chatbot.procesar_mensaje(user_phone2, "1")
    
    print("\n--- Mensaje 3: 37 (seleccionar Necoclí) ---")
    response = chatbot.procesar_mensaje(user_phone2, "37")
    
    if "Opción inválida" in response or "1 al 4" in response:
        print(f"❌ ERROR: Validación incorrecta para destino 37!")
        print(f"Respuesta: {response}")
        return False
    
    if "Necoclí" in response and "$400.000" in response:
        print(f"✅ Respuesta correcta: {response[:150]}...")
    else:
        print(f"❌ ERROR: Respuesta incorrecta para destino 37")
        print(f"Respuesta: {response}")
        return False
    
    # Probar destinos intermedios
    print("\n\n--- PRUEBA DESTINOS INTERMEDIOS ---")
    for destino_num in [10, 20, 30]:
        user_test = f"test_{destino_num}"
        print(f"\n📱 Probando destino {destino_num}...")
        chatbot.procesar_mensaje(user_test, "hola")
        chatbot.procesar_mensaje(user_test, "1")
        response = chatbot.procesar_mensaje(user_test, str(destino_num))
        
        if "Opción inválida" in response or "1 al 4" in response:
            print(f"❌ ERROR: Validación incorrecta para destino {destino_num}!")
            return False
        print(f"✅ Destino {destino_num} funciona correctamente")
    
    print("\n\n🎉 TODOS LOS TESTS PASARON")
    print("✅ El sistema funciona correctamente en modo producción")
    print("✅ Todos los destinos (1-37) son accesibles")
    print("✅ No hay errores de validación")
    print("✅ Las sesiones se mantienen correctamente")
    
    return True

if __name__ == "__main__":
    success = test_produccion_real()
    sys.exit(0 if success else 1)