# 🌍 Viajes Colombia Tours - Chatbot WhatsApp

Sistema de chatbot conversacional para agencia de viajes integrado con WhatsApp, Google Sheets y Evolution API.

## 📋 Descripción

Chatbot inteligente que permite a los clientes:
- 🗺️ Explorar destinos turísticos en Colombia (Bogotá, Medellín, Cartagena, Arauca)
- 🏨 Consultar hoteles disponibles con precios y detalles completos
- 🎉 Ver promociones y ofertas especiales
- 📞 Contactar con asesores humanos
- ℹ️ Obtener información sobre la agencia

## 🚀 Características

- ✅ Conversación natural por WhatsApp
- ✅ Menú interactivo con opciones numeradas
- ✅ Información detallada de hoteles por destino
- ✅ Sistema de promociones y ofertas
- ✅ Integración con Google Sheets para almacenamiento
- ✅ Gestión de sesiones de usuario
- ✅ Respuestas automáticas 24/7

## 🏗️ Arquitectura

```
chatbot/
├── engine.py          # Motor principal del chatbot
├── validaciones.py    # Validaciones de entrada
models/
├── cliente.py         # Modelo de cliente
├── sesion.py          # Modelo de sesión
config/
├── constants.py       # Constantes (destinos, hoteles, promociones)
├── settings.py        # Configuración
services/
├── whatsapp.py        # Integración WhatsApp
├── google_sheets.py   # Integración Google Sheets
```

## 📦 Instalación

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno en `.env`:
```
GOOGLE_SHEET_ID=tu_sheet_id
EVOLUTION_API_URL=tu_url
EVOLUTION_API_KEY=tu_key
INSTANCE_NAME=tu_instancia
```

4. Configurar credenciales de Google Sheets (`service_account.json`)

## 🎯 Uso

Iniciar el servidor:
```bash
python start.py
```

El chatbot responderá automáticamente a mensajes de WhatsApp con el menú principal.

## 🗺️ Destinos Disponibles

- 🏛️ **Bogotá** - La capital colombiana
- 🌸 **Medellín** - Ciudad de la eterna primavera
- 🏖️ **Cartagena** - Joya del Caribe
- 🌾 **Arauca** - Tierra de llanuras

## 💼 Contacto

**Viajes Colombia Tours**
- 📍 Sede: Bogotá, Colombia
- ⏰ Horario: Lunes a sábado, 8am – 6pm
- 📞 Teléfono: +57 300 000 0000

## 📄 Licencia

Proyecto privado - Todos los derechos reservados
