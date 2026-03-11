"""Test para verificar que el mock de sheets funciona."""
from chatbot.engine import ChatbotEngine
from models import Sesion

def test_mock():
    """Verifica que el mock guarda y recupera sesiones."""
    print("=" * 60)
    print("TEST: MOCK DE SHEETS")
    print("=" * 60)
    
    chatbot = ChatbotEngine()
    
    print(f"\n1️⃣ Tipo de sheets: {type(chatbot.sheets)}")
    print(f"   Tiene sesiones dict: {hasattr(chatbot.sheets, 'sesiones')}")
    
    # Crear una sesión manualmente
    telefono = "573001111111"
    sesion = Sesion(telefono=telefono, estado="boletos_nacionales", bot_activo=True)
    
    print(f"\n2️⃣ Creando sesión manualmente...")
    row = chatbot.sheets.crear_sesion(sesion)
    print(f"   Row index: {row}")
    print(f"   Sesiones en memoria: {len(chatbot.sheets.sesiones)}")
    print(f"   Teléfonos: {list(chatbot.sheets.sesiones.keys())}")
    
    print(f"\n3️⃣ Recuperando sesión...")
    resultado = chatbot.sheets.get_sesion(telefono)
    if resultado:
        sesion_recuperada, row_index = resultado
        print(f"   ✅ Sesión recuperada")
        print(f"   Estado: {sesion_recuperada.estado}")
        print(f"   Teléfono: {sesion_recuperada.telefono}")
    else:
        print(f"   ❌ No se pudo recuperar la sesión")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_mock()
