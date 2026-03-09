"""Script de prueba para el chatbot de viajes."""
from chatbot.engine import ChatbotEngine


def test_flujo_completo():
    """Prueba el flujo completo del chatbot."""
    engine = ChatbotEngine()
    telefono_test = "+573001234567"
    
    print("=" * 60)
    print("PRUEBA DEL CHATBOT - VIAJES COLOMBIA TOURS")
    print("=" * 60)
    
    # 1. Mensaje inicial
    print("\n1. MENSAJE INICIAL (hola)")
    print("-" * 60)
    respuesta = engine.procesar_mensaje(telefono_test, "hola")
    print(respuesta)
    
    # 2. Seleccionar opción 1 (Ver destinos)
    print("\n2. SELECCIONAR OPCIÓN 1 (Ver destinos)")
    print("-" * 60)
    respuesta = engine.procesar_mensaje(telefono_test, "1")
    print(respuesta)
    
    # 3. Seleccionar Cartagena
    print("\n3. SELECCIONAR CARTAGENA (opción 3)")
    print("-" * 60)
    respuesta = engine.procesar_mensaje(telefono_test, "3")
    print(respuesta)
    
    # 4. Seleccionar Hotel Muralla Real
    print("\n4. SELECCIONAR HOTEL MURALLA REAL (opción 1)")
    print("-" * 60)
    respuesta = engine.procesar_mensaje(telefono_test, "1")
    print(respuesta)
    
    # 5. Volver al menú
    print("\n5. VOLVER AL MENÚ")
    print("-" * 60)
    respuesta = engine.procesar_mensaje(telefono_test, "menu")
    print(respuesta)
    
    # 6. Ver promociones
    print("\n6. VER PROMOCIONES (opción 4)")
    print("-" * 60)
    respuesta = engine.procesar_mensaje(telefono_test, "4")
    print(respuesta)
    
    # 7. Volver al menú y ver información
    print("\n7. VER INFORMACIÓN DE LA AGENCIA (opción 2)")
    print("-" * 60)
    respuesta = engine.procesar_mensaje(telefono_test, "menu")
    respuesta = engine.procesar_mensaje(telefono_test, "2")
    print(respuesta)
    
    print("\n" + "=" * 60)
    print("PRUEBA COMPLETADA EXITOSAMENTE ✅")
    print("=" * 60)


def test_todos_los_destinos():
    """Prueba todos los destinos disponibles."""
    engine = ChatbotEngine()
    telefono_test = "+573009876543"
    
    destinos = {
        "1": "Bogotá",
        "2": "Medellín",
        "3": "Cartagena",
        "4": "Arauca"
    }
    
    print("\n" + "=" * 60)
    print("PRUEBA DE TODOS LOS DESTINOS")
    print("=" * 60)
    
    for opcion, nombre in destinos.items():
        print(f"\n--- DESTINO: {nombre} ---")
        engine.procesar_mensaje(telefono_test, "menu")
        engine.procesar_mensaje(telefono_test, "1")
        respuesta = engine.procesar_mensaje(telefono_test, opcion)
        print(respuesta)
        print()


def test_contacto_humano():
    """Prueba la opción de contacto con humano."""
    engine = ChatbotEngine()
    telefono_test = "+573005555555"
    
    print("\n" + "=" * 60)
    print("PRUEBA DE CONTACTO CON ASESOR")
    print("=" * 60)
    
    engine.procesar_mensaje(telefono_test, "hola")
    respuesta = engine.procesar_mensaje(telefono_test, "3")
    print(respuesta)


if __name__ == "__main__":
    print("\n🚀 Iniciando pruebas del chatbot...\n")
    
    try:
        # Ejecutar pruebas
        test_flujo_completo()
        test_todos_los_destinos()
        test_contacto_humano()
        
        print("\n✅ Todas las pruebas completadas exitosamente!")
        
    except Exception as e:
        print(f"\n❌ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
