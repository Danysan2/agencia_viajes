"""Test simple para verificar precios."""

# Verificar primero que constants.py tiene los precios
print("Verificando config/constants.py...")
from config.constants import DESTINOS_NACIONALES_DESDE_ARAUCA
print(f"Total destinos: {len(DESTINOS_NACIONALES_DESDE_ARAUCA)}")
print(f"Primer destino: {DESTINOS_NACIONALES_DESDE_ARAUCA[0]}")
print(f"Tiene precio: {'precio' in DESTINOS_NACIONALES_DESDE_ARAUCA[0]}")

if 'precio' not in DESTINOS_NACIONALES_DESDE_ARAUCA[0]:
    print("\n❌ ERROR: Los destinos NO tienen precios!")
    exit(1)

print("\n✅ Los destinos SÍ tienen precios")
print("\nEjemplos:")
for i in [0, 3, 10, 20, 31]:
    dest = DESTINOS_NACIONALES_DESDE_ARAUCA[i]
    print(f"  {i+1}. {dest['nombre']} - ${dest['precio']:,}")

# Ahora probar el chatbot
print("\n" + "=" * 70)
print("Probando chatbot...")
from chatbot.engine import ChatbotEngine

chatbot = ChatbotEngine()
telefono = "573009999999"

print("\n1. Iniciando conversación...")
chatbot.procesar_mensaje(telefono, "hola")

print("2. Seleccionando opción 1...")
respuesta = chatbot.procesar_mensaje(telefono, "1")

print("\n3. Verificando precios en la respuesta...")
if "$60.000" in respuesta:
    print("   ✅ Precio de Tame ($60.000) encontrado")
else:
    print("   ❌ Precio de Tame NO encontrado")
    
if "$110.000" in respuesta:
    print("   ✅ Precio de Yopal ($110.000) encontrado")
else:
    print("   ❌ Precio de Yopal NO encontrado")

if "$360.000" in respuesta:
    print("   ✅ Precio de Pasto ($360.000) encontrado")
else:
    print("   ❌ Precio de Pasto NO encontrado")

print("\n4. Seleccionando destino 1 (Tame)...")
respuesta = chatbot.procesar_mensaje(telefono, "1")

if "Tame" in respuesta and "$60.000" in respuesta:
    print("   ✅ Confirmación con precio correcto")
else:
    print("   ❌ Confirmación sin precio")

print("\n" + "=" * 70)
print("✅ TEST COMPLETADO")
print("=" * 70)
