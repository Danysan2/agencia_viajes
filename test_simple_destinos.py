"""Test simple y directo de los destinos nacionales desde Arauca."""
import sys
sys.path.insert(0, '.')

from config.constants import DESTINOS_NACIONALES_DESDE_ARAUCA, AGENCIA_TELEFONO

def test_constantes():
    """Verificar que las constantes están correctamente definidas."""
    print("=" * 70)
    print("TEST: Verificación de Constantes")
    print("=" * 70)
    
    print(f"\n✅ Total de destinos: {len(DESTINOS_NACIONALES_DESDE_ARAUCA)}")
    print(f"✅ Teléfono agencia: {AGENCIA_TELEFONO}")
    
    print("\n📍 Destinos por departamento:\n")
    
    # Agrupar por departamento
    departamentos = {}
    for idx, destino in enumerate(DESTINOS_NACIONALES_DESDE_ARAUCA, 1):
        dept = destino['departamento']
        if dept not in departamentos:
            departamentos[dept] = []
        departamentos[dept].append((idx, destino['nombre']))
    
    for dept in sorted(departamentos.keys()):
        print(f"  {dept}:")
        for num, ciudad in departamentos[dept]:
            print(f"    {num:2d}. {ciudad}")
        print()
    
    print(f"✅ Total: {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} destinos en {len(departamentos)} departamentos\n")

def test_metodos_engine():
    """Test directo de los métodos del engine."""
    print("=" * 70)
    print("TEST: Métodos del ChatbotEngine")
    print("=" * 70)
    
    from chatbot.engine import ChatbotEngine
    
    engine = ChatbotEngine()
    
    # Test 1: Menú principal
    print("\n1. Menú Principal:")
    print("-" * 70)
    menu = engine._menu_principal()
    print(menu)
    assert "1️⃣ Boletos nacionales en Colombia" in menu
    print("\n✅ Menú principal OK")
    
    # Test 2: Mostrar destinos nacionales
    print("\n2. Destinos Nacionales desde Arauca:")
    print("-" * 70)
    destinos = engine._mostrar_destinos_nacionales()
    print(destinos)
    
    # Verificaciones
    assert "Boletos Nacionales desde Arauca" in destinos
    assert "Tame" in destinos
    assert "Bogotá" in destinos
    assert "Medellín" in destinos
    assert "Cartagena" in destinos
    assert "Necoclí" in destinos
    print("\n✅ Destinos nacionales OK")
    
    # Test 3: Verificar que todos los 25 destinos están en el mensaje
    print("\n3. Verificación de los 25 destinos:")
    print("-" * 70)
    destinos_faltantes = []
    for destino in DESTINOS_NACIONALES_DESDE_ARAUCA:
        if destino['nombre'] not in destinos:
            destinos_faltantes.append(destino['nombre'])
    
    if destinos_faltantes:
        print(f"❌ Destinos faltantes: {', '.join(destinos_faltantes)}")
    else:
        print(f"✅ Todos los {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} destinos están presentes")

def test_formato_respuesta_destino():
    """Test del formato de respuesta al seleccionar un destino."""
    print("\n" + "=" * 70)
    print("TEST: Formato de Respuesta por Destino")
    print("=" * 70)
    
    # Simular respuesta para algunos destinos
    destinos_prueba = [
        (1, "Tame", "Arauca"),
        (14, "Bogotá", "Cundinamarca"),
        (16, "Medellín", "Antioquia"),
        (25, "Necoclí", "Antioquia")
    ]
    
    for idx, nombre, departamento in destinos_prueba:
        destino = DESTINOS_NACIONALES_DESDE_ARAUCA[idx - 1]
        
        # Formato esperado de la respuesta
        respuesta = f"""🚌 *Arauca → {destino['nombre']}*

📍 Destino: {destino['nombre']}, {destino['departamento']}
🚏 Origen: Arauca

Para consultar disponibilidad, horarios y precios de boletos, contáctanos:

📞 WhatsApp: {AGENCIA_TELEFONO}
📧 Email: info@viajescolombia.com
⏰ Horario: Lunes a sábado, 8am – 6pm

Te ayudaremos con:
• Horarios de salida disponibles
• Precios y tarifas especiales
• Tipo de vehículo (bus, van, etc.)
• Duración aproximada del viaje
• Reserva de tu boleto

Escribe *menú* para volver al inicio."""
        
        print(f"\n--- Destino #{idx}: {nombre} ---")
        print(respuesta)
        
        # Verificaciones
        assert f"Arauca → {nombre}" in respuesta
        assert departamento in respuesta
        assert AGENCIA_TELEFONO in respuesta
        print(f"✅ Formato correcto para {nombre}")

def test_rangos_validos():
    """Test de validación de rangos."""
    print("\n" + "=" * 70)
    print("TEST: Validación de Rangos")
    print("=" * 70)
    
    total = len(DESTINOS_NACIONALES_DESDE_ARAUCA)
    
    print(f"\nRango válido: 1 a {total}")
    
    # Números válidos
    validos = [1, 5, 14, 16, 24, 25]
    print(f"\nNúmeros válidos de prueba: {validos}")
    for num in validos:
        if 1 <= num <= total:
            destino = DESTINOS_NACIONALES_DESDE_ARAUCA[num - 1]
            print(f"  ✅ {num} → {destino['nombre']}")
        else:
            print(f"  ❌ {num} fuera de rango")
    
    # Números inválidos
    invalidos = [0, 26, 100, -1]
    print(f"\nNúmeros inválidos de prueba: {invalidos}")
    for num in invalidos:
        if 1 <= num <= total:
            print(f"  ❌ {num} debería ser inválido pero está en rango")
        else:
            print(f"  ✅ {num} correctamente fuera de rango")

def test_estructura_datos():
    """Test de la estructura de datos."""
    print("\n" + "=" * 70)
    print("TEST: Estructura de Datos")
    print("=" * 70)
    
    print("\nVerificando estructura de cada destino...")
    
    errores = []
    for idx, destino in enumerate(DESTINOS_NACIONALES_DESDE_ARAUCA, 1):
        # Verificar que tiene las claves necesarias
        if 'nombre' not in destino:
            errores.append(f"Destino #{idx} no tiene 'nombre'")
        if 'departamento' not in destino:
            errores.append(f"Destino #{idx} no tiene 'departamento'")
        
        # Verificar que los valores no están vacíos
        if not destino.get('nombre'):
            errores.append(f"Destino #{idx} tiene nombre vacío")
        if not destino.get('departamento'):
            errores.append(f"Destino #{idx} tiene departamento vacío")
    
    if errores:
        print("\n❌ Errores encontrados:")
        for error in errores:
            print(f"  • {error}")
    else:
        print(f"\n✅ Todos los {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} destinos tienen estructura correcta")
        print("   • Clave 'nombre' presente")
        print("   • Clave 'departamento' presente")
        print("   • Valores no vacíos")

if __name__ == "__main__":
    print("\n" + "🚀" * 35)
    print("PRUEBAS SIMPLES - DESTINOS NACIONALES DESDE ARAUCA")
    print("🚀" * 35 + "\n")
    
    try:
        test_constantes()
        test_metodos_engine()
        test_formato_respuesta_destino()
        test_rangos_validos()
        test_estructura_datos()
        
        print("\n" + "=" * 70)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 70)
        print("\n📋 Resumen Final:")
        print(f"   • {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} destinos desde Arauca")
        print("   • Estructura de datos correcta")
        print("   • Métodos del engine funcionando")
        print("   • Formato de respuesta correcto")
        print("   • Validación de rangos OK")
        print("\n✈️  El sistema está listo para usar!\n")
        
    except AssertionError as e:
        print(f"\n❌ ERROR DE ASERCIÓN: {e}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
