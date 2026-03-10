"""Test de notificación al profesional."""

def simular_opcion_3():
    """Simula cuando un usuario selecciona opción 3 (Boletos aéreos)."""
    return """✈️ *Boletos Aéreos*

Perfecto! Un asesor especializado te contactará en breve para ayudarte con:

• Consulta de disponibilidad
• Mejores tarifas del momento
• Opciones de aerolíneas
• Horarios de vuelos
• Reserva y emisión de boletos

⏰ Tiempo de respuesta: 5-10 minutos

Escribe *menú* si deseas ver otras opciones mientras esperas."""


def simular_opcion_4():
    """Simula cuando un usuario selecciona opción 4 (Paquetes turísticos)."""
    return """🎒 *Paquetes Turísticos*

Excelente elección! Un asesor especializado te contactará en breve para ayudarte con:

• Paquetes personalizados
• Mejores ofertas disponibles
• Itinerarios detallados
• Opciones de pago
• Reserva de tu paquete ideal

⏰ Tiempo de respuesta: 5-10 minutos

Escribe *menú* si deseas ver otras opciones mientras esperas."""


def simular_notificacion_profesional(telefono_cliente: str, tipo_solicitud: str):
    """Simula el mensaje que recibe el profesional."""
    from datetime import datetime
    
    return f"""🔔 *NUEVA SOLICITUD DE ATENCIÓN*

👤 *Cliente:* Cliente nuevo
📱 *Teléfono:* {telefono_cliente}
📋 *Solicitud:* {tipo_solicitud}
⏰ *Hora:* {datetime.now().strftime('%d/%m/%Y %H:%M')}

Por favor, contacta a este cliente para ayudarle con su solicitud.

_Este es un mensaje automático del sistema._"""


def test_flujo_completo():
    """Test del flujo completo con notificaciones."""
    print("=" * 70)
    print("TEST: NOTIFICACIÓN AL PROFESIONAL")
    print("=" * 70)
    
    telefono_cliente = "+573001234567"
    telefono_profesional = "+573007654321"
    
    # Escenario 1: Usuario selecciona opción 3
    print("\n" + "=" * 70)
    print("ESCENARIO 1: Usuario selecciona Boletos Aéreos (Opción 3)")
    print("=" * 70)
    
    print("\n📱 Usuario: hola")
    print("-" * 70)
    print("[Menú principal mostrado]")
    
    print("\n📱 Usuario: 3")
    print("-" * 70)
    print("🤖 Bot responde al cliente:")
    print(simular_opcion_3())
    
    print("\n📤 Sistema envía notificación al profesional:")
    print(f"Destinatario: {telefono_profesional}")
    print("-" * 70)
    print(simular_notificacion_profesional(telefono_cliente, "Boletos aéreos"))
    
    # Escenario 2: Usuario selecciona opción 4
    print("\n" + "=" * 70)
    print("ESCENARIO 2: Usuario selecciona Paquetes Turísticos (Opción 4)")
    print("=" * 70)
    
    print("\n📱 Usuario: hola")
    print("-" * 70)
    print("[Menú principal mostrado]")
    
    print("\n📱 Usuario: 4")
    print("-" * 70)
    print("🤖 Bot responde al cliente:")
    print(simular_opcion_4())
    
    print("\n📤 Sistema envía notificación al profesional:")
    print(f"Destinatario: {telefono_profesional}")
    print("-" * 70)
    print(simular_notificacion_profesional(telefono_cliente, "Paquetes turísticos"))
    
    # Resumen
    print("\n" + "=" * 70)
    print("✅ TEST COMPLETADO")
    print("=" * 70)
    print("\n📋 Resumen:")
    print("   • Opción 3 (Boletos aéreos) → Notifica al profesional")
    print("   • Opción 4 (Paquetes turísticos) → Notifica al profesional")
    print("   • Cliente recibe mensaje de espera")
    print("   • Profesional recibe notificación con datos del cliente")
    print("\n💡 Configuración necesaria:")
    print("   • Agregar PROFESSIONAL_PHONE en .env")
    print("   • Ejemplo: PROFESSIONAL_PHONE=+573001234567")


def test_configuracion():
    """Test de configuración."""
    print("\n" + "=" * 70)
    print("TEST: VERIFICACIÓN DE CONFIGURACIÓN")
    print("=" * 70)
    
    try:
        from config.settings import PROFESSIONAL_PHONE
        print(f"\n✅ PROFESSIONAL_PHONE configurado: {PROFESSIONAL_PHONE}")
    except ImportError:
        print("\n⚠️  No se pudo importar PROFESSIONAL_PHONE")
        print("   Asegúrate de que config/settings.py esté actualizado")
    
    print("\n📝 Pasos para configurar:")
    print("   1. Editar archivo .env")
    print("   2. Agregar: PROFESSIONAL_PHONE=+573001234567")
    print("   3. Reemplazar con el número real del profesional")
    print("   4. Reiniciar el servidor")


if __name__ == "__main__":
    test_flujo_completo()
    test_configuracion()
