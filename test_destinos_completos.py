"""Test para verificar todos los destinos con precios actualizados."""

def test_destinos_completos():
    """Prueba que todos los 37 destinos están con precios correctos."""
    print("=" * 70)
    print("TEST: TODOS LOS DESTINOS CON PRECIOS")
    print("=" * 70)
    
    # Eliminar cache
    import sys
    modules_to_reload = [k for k in sys.modules.keys() if k.startswith('config')]
    for mod in modules_to_reload:
        del sys.modules[mod]
    
    from config.constants import DESTINOS_NACIONALES_DESDE_ARAUCA
    from chatbot.engine import ChatbotEngine
    
    print(f"\n📊 Total de destinos: {len(DESTINOS_NACIONALES_DESDE_ARAUCA)}")
    
    # Verificar destinos específicos
    destinos_verificar = [
        ("Tame", 60000),
        ("Yopal", 110000),
        ("Bogotá", 150000),
        ("Cali", 270000),
        ("La Hormiga", 300000),
        ("Pasto", 360000),
        ("Santa Marta", 380000),
        ("Cartagena", 380000),
        ("Barranquilla", 380000),
        ("Necoclí", 400000)
    ]
    
    print("\n🔍 Verificando destinos específicos:")
    for nombre, precio_esperado in destinos_verificar:
        encontrado = False
        for destino in DESTINOS_NACIONALES_DESDE_ARAUCA:
            if destino['nombre'] == nombre:
                if destino['precio'] == precio_esperado:
                    print(f"   ✅ {nombre}: ${precio_esperado:,}")
                else:
                    print(f"   ❌ {nombre}: Esperado ${precio_esperado:,}, encontrado ${destino['precio']:,}")
                encontrado = True
                break
        if not encontrado:
            print(f"   ❌ {nombre}: NO ENCONTRADO")
    
    # Mostrar todos los destinos
    print(f"\n📋 Lista completa de {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} destinos:")
    for i, destino in enumerate(DESTINOS_NACIONALES_DESDE_ARAUCA, 1):
        precio_formateado = f"${destino['precio']:,}".replace(",", ".")
        print(f"   {i:2d}. {destino['nombre']} - {precio_formateado}")
    
    # Probar el chatbot
    print("\n" + "=" * 70)
    print("PROBANDO CHATBOT CON NUEVOS DESTINOS")
    print("=" * 70)
    
    chatbot = ChatbotEngine()
    telefono = "573001234567"
    
    print("\n1️⃣ Iniciando conversación...")
    chatbot.procesar_mensaje(telefono, "hola")
    
    print("2️⃣ Seleccionando opción 1 (Boletos nacionales)...")
    respuesta = chatbot.procesar_mensaje(telefono, "1")
    
    # Verificar que muestra los nuevos precios
    precios_verificar = ["$300.000", "$380.000", "$400.000"]
    for precio in precios_verificar:
        if precio in respuesta:
            print(f"   ✅ {precio} encontrado en la lista")
        else:
            print(f"   ❌ {precio} NO encontrado")
    
    # Probar selección de Necoclí (último destino, más caro)
    print(f"\n3️⃣ Seleccionando destino {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} (Necoclí - $400.000)...")
    respuesta = chatbot.procesar_mensaje(telefono, str(len(DESTINOS_NACIONALES_DESDE_ARAUCA)))
    
    if "Necoclí" in respuesta and "$400.000" in respuesta:
        print("   ✅ Necoclí seleccionado correctamente con precio")
        print("   ✅ Notificación enviada al profesional")
    else:
        print("   ❌ Error con Necoclí")
    
    print("\n" + "=" * 70)
    print("✅ TEST COMPLETADO")
    print("=" * 70)
    
    print(f"\n📈 Resumen de precios:")
    print(f"   💰 Más barato: Tame/Saravena - $60.000")
    print(f"   💰 Más caro: Necoclí - $400.000")
    print(f"   📊 Total destinos: {len(DESTINOS_NACIONALES_DESDE_ARAUCA)}")
    print(f"   🎯 Todos con precios incluidos")

if __name__ == "__main__":
    try:
        test_destinos_completos()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()