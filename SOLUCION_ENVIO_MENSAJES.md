# 🔧 Solución: Mensajes No Se Envían al Profesional

## ❌ Problema Identificado

Los mensajes NO se están enviando al número profesional **573001833654** porque el archivo `.env` tiene valores de ejemplo (placeholders) en lugar de las credenciales reales de Evolution API.

## 🔍 Diagnóstico

### Configuración Actual (INCORRECTA):
```env
EVOLUTION_API_URL=https://tu-instancia.evolution-api.com
EVOLUTION_API_KEY=tu_api_key_aqui
EVOLUTION_INSTANCE_NAME=nombre_de_tu_instancia
```

Estos son valores de ejemplo que NO funcionan. Necesitas reemplazarlos con tus credenciales reales.

## ✅ Solución Paso a Paso

### Paso 1: Obtener Credenciales de Evolution API

Necesitas obtener estos 3 valores de tu panel de Evolution API:

1. **EVOLUTION_API_URL**: La URL de tu servidor Evolution API
   - Ejemplo: `https://api.evolution.com` o `https://tu-servidor.com:8080`
   
2. **EVOLUTION_API_KEY**: Tu API key de autenticación
   - Ejemplo: `B6D711FCDE4D4FD5936544120E713976`
   
3. **EVOLUTION_INSTANCE_NAME**: El nombre de tu instancia de WhatsApp
   - Ejemplo: `mi_instancia` o `whatsapp_bot`

### Paso 2: Actualizar el Archivo .env

Abre el archivo `.env` y reemplaza los valores de ejemplo con tus credenciales reales:

```env
# Evolution API - WhatsApp
EVOLUTION_API_URL=https://TU_URL_REAL_AQUI
EVOLUTION_API_KEY=TU_API_KEY_REAL_AQUI
EVOLUTION_INSTANCE_NAME=TU_INSTANCIA_REAL_AQUI

# Notificaciones al Profesional
PROFESSIONAL_PHONE=573001833654
```

**IMPORTANTE**: 
- NO incluyas el símbolo `+` en el número de teléfono
- El formato correcto es: `573001833654` (código país + número)

### Paso 3: Verificar la Configuración

Ejecuta el script de prueba para verificar que todo funciona:

```bash
python test_evolution_connection.py
```

Este script te mostrará:
- ✅ Si las credenciales están configuradas
- ✅ Si la conexión con Evolution API funciona
- ✅ Si el mensaje de prueba se envió correctamente

### Paso 4: Reiniciar el Servidor

Después de actualizar el `.env`, reinicia el servidor para que cargue las nuevas configuraciones:

```bash
# Detener el servidor actual (Ctrl+C)
# Luego iniciar de nuevo:
python server.py
```

## 🔧 Cambios Realizados en el Código

### 1. Actualizado `services/evolution_api.py`
- ✅ Mejorado el manejo del formato de números (elimina `+` automáticamente)
- ✅ Agregado logging detallado para debugging
- ✅ Muestra URL, payload y respuesta completa en los logs

### 2. Actualizado `.env`
- ✅ Cambiado `PROFESSIONAL_PHONE` a `573001833654`
- ✅ Actualizado comentarios sobre formato correcto

### 3. Creado `test_evolution_connection.py`
- ✅ Script para probar la conexión con Evolution API
- ✅ Verifica todas las configuraciones
- ✅ Envía mensaje de prueba al número profesional

## 📋 Checklist de Verificación

Antes de que funcione, asegúrate de:

- [ ] Tienes acceso a tu panel de Evolution API
- [ ] Obtuviste las 3 credenciales (URL, API_KEY, INSTANCE_NAME)
- [ ] Actualizaste el archivo `.env` con valores reales
- [ ] Tu instancia de Evolution API está conectada a WhatsApp
- [ ] El número 573001833654 está en formato correcto (sin +)
- [ ] Ejecutaste `test_evolution_connection.py` exitosamente
- [ ] Reiniciaste el servidor después de los cambios

## 🆘 ¿Dónde Obtener las Credenciales?

Si no sabes dónde obtener las credenciales de Evolution API:

1. **Accede a tu panel de Evolution API** (donde configuraste tu instancia)
2. **Busca la sección de API Keys o Configuración**
3. **Copia los valores de:**
   - URL del servidor
   - API Key
   - Nombre de la instancia

Si no tienes Evolution API configurado, necesitas:
1. Instalar Evolution API en un servidor
2. Crear una instancia de WhatsApp
3. Conectar tu número de WhatsApp escaneando el QR

## 🧪 Probar el Sistema Completo

Una vez configurado, prueba el flujo completo:

1. Envía un mensaje al chatbot desde otro número
2. Selecciona opción 3 (Boletos aéreos) o 4 (Paquetes turísticos)
3. Verifica que el número **573001833654** reciba la notificación

## 📝 Logs para Debugging

Cuando envíes mensajes, verás logs detallados como:

```
📤 Intentando enviar mensaje a: 573001833654
🔗 URL: https://tu-api.com/message/sendText/tu_instancia
📋 Payload: {'number': '573001833654', 'text': '...'}
📥 Status Code: 200
📥 Response: {"status": "success"}
✅ Mensaje enviado exitosamente a 573001833654
```

Si hay errores, los logs mostrarán exactamente qué falló.

## ⚠️ Errores Comunes

### Error: "Connection refused"
- La URL de Evolution API es incorrecta
- El servidor Evolution API no está corriendo

### Error: "Unauthorized" o "401"
- La API_KEY es incorrecta

### Error: "Instance not found" o "404"
- El INSTANCE_NAME es incorrecto
- La instancia no existe en tu servidor

### Error: "Instance not connected"
- Tu instancia de WhatsApp no está conectada
- Necesitas escanear el QR nuevamente

## 📞 Contacto

Si después de seguir estos pasos aún no funciona, verifica:
1. Los logs del servidor Evolution API
2. Que tu instancia esté conectada (estado "open")
3. Que el número 573001833654 sea válido en WhatsApp
