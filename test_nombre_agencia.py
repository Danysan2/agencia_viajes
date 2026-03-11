#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test para verificar que el nombre de la agencia es correcto."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.engine import ChatbotEngine

def test_nombre_agencia():
    """Verifica que el nombre de la agencia aparece correctamente."""
    print("🧪 TEST: Nombre de la Agencia")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    user_id = "test_nombre"
    
    print("\n--- Mensaje de Bienvenida ---")
    response = chatbot.procesar_mensaje(user_id, "hola")
    
    print(f"\nRespuesta:\n{response}\n")
    
    # Verificar que el nombre correcto aparece
    if "JYE Conexiones Arauca Libertadores" in response:
        print("✅ Nombre de la agencia correcto")
    else:
        print("❌ ERROR: Nombre de la agencia incorrecto")
        return False
    
    # Verificar otros datos
    if "Arauca, Colombia" in response:
        print("✅ Sede correcta")
    else:
        print("⚠️  Sede no aparece en el mensaje")
    
    if "6am – 8pm" in response or "6am - 8pm" in response:
        print("✅ Horario correcto")
    else:
        print("⚠️  Horario no aparece en el mensaje")
    
    print("\n🎉 TEST COMPLETADO")
    print("✅ El nombre de la agencia se muestra correctamente")
    
    return True

if __name__ == "__main__":
    success = test_nombre_agencia()
    sys.exit(0 if success else 1)