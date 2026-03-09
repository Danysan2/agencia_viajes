# 🌍 Viajes Colombia Tours - Chatbot WhatsApp

## 📊 Resumen Ejecutivo

Sistema de chatbot conversacional para agencia de viajes que permite a los clientes explorar destinos turísticos, consultar hoteles, ver promociones y contactar asesores, todo a través de WhatsApp.

## 🎯 Objetivo del Proyecto

Automatizar la atención al cliente de una agencia de viajes mediante un chatbot inteligente que proporciona información sobre destinos, hoteles y promociones 24/7.

## ✨ Funcionalidades Principales

### 1. Menú Principal Interactivo
```
1️⃣ Conocer nuestros destinos en Colombia
2️⃣ Información sobre nosotros
3️⃣ Hablar con un asesor
4️⃣ Ver promociones y ofertas especiales
```

### 2. Exploración de Destinos
- **Bogotá** 🏛️ - 2 hoteles disponibles
- **Medellín** 🌸 - 2 hoteles disponibles
- **Cartagena** 🏖️ - 3 hoteles disponibles
- **Arauca** 🌾 - 1 hotel disponible

### 3. Información Detallada de Hoteles
Cada hotel incluye:
- ✅ Nombre y ubicación
- 💰 Precio por noche
- 📋 Lista completa de servicios incluidos
- 📅 Disponibilidad
- 📸 Opción de imagen (configurable)

### 4. Promociones Especiales
- **Cartagena Express**: 3 noches, $899.000 COP
- **Medellín City Tour**: 2 noches, $650.000 COP

### 5. Información de la Agencia
- Historia y experiencia (8 años)
- Servicios ofrecidos
- Datos de contacto
- Horarios de atención

### 6. Contacto con Asesor Humano
Transferencia directa a un asesor para consultas personalizadas.

## 🏗️ Arquitectura Técnica

### Componentes Principales

```
chatbot/
├── engine.py          # Motor conversacional
├── validaciones.py    # Validación de entradas
└── __init__.py

models/
├── cliente.py         # Modelo de cliente
├── sesion.py          # Gestión de sesiones
└── __init__.py

config/
├── constants.py       # Destinos, hoteles, promociones
├── settings.py        # Configuración general
└── __init__.py

services/
├── whatsapp.py        # Integración WhatsApp
├── google_sheets.py   # Almacenamiento en Sheets
└── __init__.py
```

### Tecnologías Utilizadas

- **Python 3.8+**: Lenguaje principal
- **Evolution API**: Integración con WhatsApp
- **Google Sheets API**: Base de datos
- **FastAPI/Flask**: Servidor web
- **Loguru**: Sistema de logs

## 📱 Flujo de Conversación

```
Usuario envía "hola"
    ↓
Menú Principal (4 opciones)
    ↓
Opción 1: Ver Destinos
    ↓
Selecciona Destino (Bogotá, Medellín, Cartagena, Arauca)
    ↓
Ve Lista de Hoteles
    ↓
Selecciona Hotel
    ↓
Ve Detalles Completos (precio, incluye, disponibilidad)
    ↓
Puede volver al menú o contactar asesor
```

## 🗂️ Estructura de Datos

### Destinos
```python
{
    "id": "dest_cartagena",
    "nombre": "Cartagena",
    "emoji": "🏖️",
    "descripcion": "La joya del Caribe colombiano"
}
```

### Hoteles
```python
{
    "id": "hotel_muralla_real",
    "nombre": "Hotel Muralla Real",
    "destino": "Cartagena",
    "precio_noche": 350000,
    "incluye": [
        "Desayuno buffet para 2 personas",
        "Habitación doble con vista al mar",
        "Acceso a piscina y spa",
        "Wi-Fi de alta velocidad",
        "Traslado aeropuerto - hotel"
    ]
}
```

### Promociones
```python
{
    "id": "promo_cartagena_express",
    "nombre": "Cartagena Express",
    "noches": 3,
    "personas": 2,
    "precio_antes": 1200000,
    "precio_ahora": 899000
}
```

## 🔧 Configuración

### Variables de Entorno (.env)
```env
GOOGLE_SHEET_ID=tu_sheet_id
EVOLUTION_API_URL=tu_url
EVOLUTION_API_KEY=tu_key
INSTANCE_NAME=tu_instancia
PORT=8000
```

### Google Sheets
Pestañas requeridas:
- `clientes`: Información de usuarios
- `sesiones_chat`: Estado de conversaciones

## 🚀 Despliegue

### Desarrollo Local
```bash
python start.py
```

### Docker
```bash
docker-compose up -d
```

### Producción
- Servidor con IP pública
- SSL/TLS configurado
- Webhook apuntando a tu servidor

## 📊 Métricas y Monitoreo

- Logs detallados con Loguru
- Seguimiento de sesiones en Google Sheets
- Historial de consultas por cliente

## 🔐 Seguridad

- Credenciales en variables de entorno
- API Keys protegidas
- Validación de entradas de usuario
- Gestión segura de sesiones

## 🎨 Personalización

### Agregar Nuevo Destino
Editar `config/constants.py`:
```python
DESTINOS["nuevo_destino"] = {
    "id": "dest_nuevo",
    "nombre": "Nuevo Destino",
    "emoji": "🌟",
    "descripcion": "Descripción"
}
```

### Agregar Nuevo Hotel
```python
HOTELES["nuevo_destino"] = [
    {
        "id": "hotel_nuevo",
        "nombre": "Hotel Nuevo",
        "precio_noche": 200000,
        "incluye": [...]
    }
]
```

## 📈 Próximas Mejoras

- [ ] Integración con sistema de reservas
- [ ] Envío de imágenes de hoteles
- [ ] Sistema de pagos en línea
- [ ] Notificaciones automáticas
- [ ] Dashboard de administración
- [ ] Reportes y analytics
- [ ] Soporte multiidioma
- [ ] Integración con CRM

## 📞 Información de Contacto

**Viajes Colombia Tours**
- 📍 Sede: Bogotá, Colombia
- ⏰ Horario: Lunes a sábado, 8am – 6pm
- 📞 Teléfono: +57 300 000 0000

## 📄 Documentación Adicional

- `GUIA_INSTALACION.md`: Instalación paso a paso
- `INICIO_RAPIDO.txt`: Guía rápida de inicio
- `flujos_chatbot.json`: Especificación de flujos
- `README.md`: Documentación general

## ✅ Estado del Proyecto

**Versión**: 1.0.0  
**Estado**: Listo para producción  
**Última actualización**: Marzo 2026

---

*Desarrollado para automatizar y mejorar la experiencia del cliente en Viajes Colombia Tours* 🇨🇴✈️
