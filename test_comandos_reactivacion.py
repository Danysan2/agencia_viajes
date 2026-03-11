#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test de todos los comandos de reactivación del bot."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chatbot.engine import ChatbotEngine
from config.constants import COMANDOS_REACTIVAR_BOT

def test_comandos_reactivacion():
    """Prueba todos los comandos de reactivación."""
    print("🧪 TEST: Comandos de Reactivación del Bot")
    print("=" * 60)
    
    print(f"\n📋 Total de comandos configurados: {len(COMANDOS_REACTIVAR_BOT)}")
    print("\nComandos disponibles:")
    for i, cmd in enumerate(COMANDOS_REACTIVAR_BOT, 1):
        print(f"  {i:2d}. '{cmd}'")
    
    chatbot = ChatbotEngine()
    comandos_exitosos = 0
    comandos_fallidos = []
    
    print(f"\n🔄 Probando {len(COMANDOS_REACTIVAR_BOT)} comandos...")
    print("-" * 60)
    
    for i, comando in enumerate(COMANDOS_REACTIVAR_BOT, 1):
        # Crear un usuario único para cada test
        user_id = f"test_cmd_{i}"
        
        # Desactivar el bot primero
        chatbot.procesar_mensaje(user_id, "hola")
        chatbot.procesar_mensaje(user_id, "1")
        chatbot.procesar_mensaje(user_id, "1")  # Seleccionar destino para desactivar
        
        # Intentar reactivar con el comando
        response = chatbot.procesar_mensaje(user_id, comando)
        
        if response and "Bot reactivado" in response:
            print(f"✅ {i:2d}. '{comando}' - FUNCIONA")
            comandos_exitosos += 1
        else:
            print(f"❌ {i:2d}. '{comando}' - FALLA")
            comandos_fallidos.append(comando)
    
    print("\n" + "=" * 60)
    print(f"📊 RESULTADOS:")
    print(f"   ✅ Comandos exitosos: {comandos_exitosos}/{len(COMANDOS_REACTIVAR_BOT)}")
    print(f"   ❌ Comandos fallidos: {len(comandos_fallidos)}/{len(COMANDOS_REACTIVAR_BOT)}")
    
    if comandos_fallidos:
        print(f"\n⚠️  Comandos que fallaron:")
        for cmd in comandos_fallidos:
            print(f"   - '{cmd}'")
        return False
    
    print("\n🎉 TODOS LOS COMANDOS FUNCIONAN CORRECTAMENTE")
    print(f"✅ {len(COMANDOS_REACTIVAR_BOT)} comandos de reactivación disponibles")
    
    # Mostrar comandos recomendados
    print("\n⭐ COMANDOS RECOMENDADOS (más cortos):")
    comandos_cortos = [cmd for cmd in COMANDOS_REACTIVAR_BOT if len(cmd) <= 10]
    for cmd in sorted(comandos_cortos, key=len):
        print(f"   - '{cmd}'")
    
    return True

if __name__ == "__main__":
    success = test_comandos_reactivacion()
    sys.exit(0 if success else 1)