"""Test para debuggear el problema de estados."""
from chatbot.engine import ChatbotEngine

def test_debug():
    """Debug del flujo de estados."""
    print("=" * 60)
    print("DEBUG: FLUJO DE ESTADOS")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    telefono = "573001111111"
    
    print("\n1️⃣ Mensaje: 'hola'")
    respuesta = chatbot.procesar_mensaje(telefono, "hola")
    print(f"Respuesta contiene 'Bienvenido': {'Bienvenido' in respuesta}")
    print(f"Respuesta contiene '1️⃣': {'1️⃣' in respuesta}")
    
    print("\n2️⃣ Mensaje: '1' (seleccionar Boletos nacionales)")
    respuesta = chatbot.procesar_mensaje(telefono, "1")
    print(f"Respuesta contiene 'Destinos disponibles': {'Destinos disponibles' in respuesta}")
    print(f"Respuesta contiene 'Tame': {'Tame' in respuesta}")
    print(f"Respuesta contiene '25': {'25' in respuesta}")
    print(f"\nPrimeros 500 caracteres de la respuesta:")
    print(respuesta[:500])
    
    print("\n3️⃣ Mensaje: '5' (seleccionar Aguazul)")
    respuesta = chatbot.procesar_mensaje(telefono, "5")
    print(f"Respuesta contiene 'Aguazul': {'Aguazul' in respuesta}")
    print(f"Respuesta contiene 'Opción inválida': {'Opción inválida' in respuesta}")
    print(f"Respuesta contiene 'asesor': {'asesor' in respuesta.lower()}")
    print(f"\nRespuesta completa:")
    print(respuesta)
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_debug()
