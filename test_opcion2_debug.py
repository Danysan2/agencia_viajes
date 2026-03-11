"""Test para debuggear la opción 2 (Boletos internacionales)."""
from chatbot.engine import ChatbotEngine

def test_opcion2():
    """Prueba el flujo completo de la opción 2."""
    print("=" * 60)
    print("DEBUG: OPCIÓN 2 - BOLETOS INTERNACIONALES")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    telefono = "573005555555"
    
    print("\n1️⃣ Mensaje: 'hola'")
    respuesta1 = chatbot.procesar_mensaje(telefono, "hola")
    print(f"Contiene 'Bienvenido': {'Bienvenido' in respuesta1}")
    print(f"Primeros 200 caracteres:\n{respuesta1[:200]}")
    
    print("\n2️⃣ Mensaje: '2' (Boletos internacionales)")
    respuesta2 = chatbot.procesar_mensaje(telefono, "2")
    print(f"Contiene 'Ecuador': {'Ecuador' in respuesta2}")
    print(f"Contiene 'Perú': {'Perú' in respuesta2 or 'Peru' in respuesta2}")
    print(f"Contiene 'Chile': {'Chile' in respuesta2}")
    print(f"\nPrimeros 500 caracteres:\n{respuesta2[:500]}")
    
    print("\n3️⃣ Mensaje: '1' (Seleccionar Ecuador)")
    respuesta3 = chatbot.procesar_mensaje(telefono, "1")
    print(f"Contiene 'Ecuador': {'Ecuador' in respuesta3}")
    print(f"Contiene 'asesor': {'asesor' in respuesta3.lower()}")
    print(f"Contiene 'Tame': {'Tame' in respuesta3}")
    print(f"Contiene 'Destinos disponibles': {'Destinos disponibles' in respuesta3}")
    print(f"\nRespuesta completa:\n{respuesta3}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_opcion2()
