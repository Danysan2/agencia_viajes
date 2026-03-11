"""Script para probar la conexión con Evolution API y envío de mensajes."""
import os
from dotenv import load_dotenv
from services.evolution_api import EvolutionAPI

# Cargar variables de entorno
load_dotenv()

def test_evolution_api():
    """Prueba la conexión y envío de mensajes con Evolution API."""
    print("=" * 60)
    print("TEST DE EVOLUTION API")
    print("=" * 60)
    
    # Verificar variables de entorno
    print("\n1️⃣ VERIFICANDO CONFIGURACIÓN:")
    print("-" * 60)
    
    api_url = os.getenv('EVOLUTION_API_URL', '')
    api_key = os.getenv('EVOLUTION_API_KEY', '')
    instance_name = os.getenv('EVOLUTION_INSTANCE_NAME', '')
    professional_phone = os.getenv('PROFESSIONAL_PHONE', '')
    
    print(f"EVOLUTION_API_URL: {api_url if api_url else '❌ NO CONFIGURADO'}")
    print(f"EVOLUTION_API_KEY: {'✅ Configurado' if api_key else '❌ NO CONFIGURADO'}")
    print(f"EVOLUTION_INSTANCE_NAME: {instance_name if instance_name else '❌ NO CONFIGURADO'}")
    print(f"PROFESSIONAL_PHONE: {professional_phone if professional_phone else '❌ NO CONFIGURADO'}")
    
    # Verificar si hay valores placeholder
    if 'tu-instancia' in api_url or 'tu_api_key' in api_key or 'nombre_de_tu_instancia' in instance_name:
        print("\n❌ ERROR: Aún tienes valores de ejemplo en tu .env")
        print("\n📝 NECESITAS CONFIGURAR:")
        print("   1. EVOLUTION_API_URL con tu URL real de Evolution API")
        print("   2. EVOLUTION_API_KEY con tu API key real")
        print("   3. EVOLUTION_INSTANCE_NAME con el nombre de tu instancia")
        print("\n💡 Estos valores los obtienes de tu panel de Evolution API")
        return False
    
    if not all([api_url, api_key, instance_name, professional_phone]):
        print("\n❌ ERROR: Faltan configuraciones en el archivo .env")
        return False
    
    print("\n✅ Todas las variables están configuradas")
    
    # Crear instancia de Evolution API
    print("\n2️⃣ CREANDO CLIENTE DE EVOLUTION API:")
    print("-" * 60)
    
    try:
        evolution = EvolutionAPI()
        print("✅ Cliente creado exitosamente")
    except Exception as e:
        print(f"❌ Error creando cliente: {e}")
        return False
    
    # Verificar estado de la instancia
    print("\n3️⃣ VERIFICANDO ESTADO DE LA INSTANCIA:")
    print("-" * 60)
    
    try:
        status = evolution.get_instance_status()
        if status:
            print(f"✅ Estado obtenido: {status}")
        else:
            print("⚠️ No se pudo obtener el estado de la instancia")
            print("   Esto puede significar:")
            print("   - La URL de la API es incorrecta")
            print("   - La API key es incorrecta")
            print("   - La instancia no existe")
            print("   - Hay problemas de red")
    except Exception as e:
        print(f"❌ Error obteniendo estado: {e}")
    
    # Probar envío de mensaje
    print("\n4️⃣ PROBANDO ENVÍO DE MENSAJE:")
    print("-" * 60)
    print(f"Enviando mensaje de prueba a: {professional_phone}")
    
    mensaje_prueba = """🧪 *MENSAJE DE PRUEBA*

Este es un mensaje de prueba del sistema de notificaciones.

Si recibes este mensaje, significa que:
✅ Evolution API está configurado correctamente
✅ El número del profesional es correcto
✅ El sistema puede enviar notificaciones

⏰ Hora: """ + __import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    try:
        resultado = evolution.send_message(professional_phone, mensaje_prueba)
        
        if resultado:
            print("\n✅ ¡MENSAJE ENVIADO EXITOSAMENTE!")
            print(f"   Verifica tu WhatsApp ({professional_phone})")
        else:
            print("\n❌ El mensaje NO se envió")
            print("   Revisa los logs arriba para ver el error específico")
    except Exception as e:
        print(f"\n❌ Error enviando mensaje: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("FIN DEL TEST")
    print("=" * 60)

if __name__ == "__main__":
    test_evolution_api()
