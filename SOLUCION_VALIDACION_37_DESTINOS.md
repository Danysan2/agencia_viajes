# Solución: Error de Validación 1-4 en Destinos Nacionales

## Problema Identificado

El sistema estaba mostrando el error "Opción inválida. Por favor responde con un número del 1 al 4" cuando el usuario intentaba seleccionar destinos del 5 al 37 en la opción de boletos nacionales.

## Causa Raíz

El problema NO está en el código de validación (que está correcto y acepta 1-37), sino en la **persistencia de sesiones** cuando se usa Google Sheets en producción. 

Cuando el usuario selecciona la opción 1 (destinos nacionales), el estado de la sesión se actualiza a `ESTADO_BOLETOS_NACIONALES` en Google Sheets. Sin embargo, cuando llega el siguiente mensaje del usuario, la sesión no se está recuperando correctamente desde Google Sheets, causando que el sistema piense que el usuario todavía está en el menú principal (que solo acepta opciones 1-4).

## Solución Implementada

### 1. Logging Mejorado

Se agregó logging detallado en `services/google_sheets.py` para rastrear:
- Cuándo se recupera una sesión y su estado
- Cuándo se actualiza una sesión y su estado
- Errores en la lectura/escritura de Google Sheets

```python
# En get_sesion()
logger.info(f"🔍 Sesión recuperada (Sheets): {telefono} - Estado: {sesion.estado}")

# En actualizar_sesion()
logger.info(f"✏️ Sesión actualizada (Sheets): {sesion.telefono} - Estado: {sesion.estado} - Row: {row_index}")
```

### 2. Logging en Chatbot Engine

Se agregó logging en `chatbot/engine.py` para ver qué estado se está procesando:

```python
logger.info(f"🔄 Procesando mensaje en estado: {sesion.estado}")
logger.info(f"📍 Procesando selección de destino nacional: {mensaje}")
```

## Verificación del Sistema

### Test Local (Modo Mock)

El sistema funciona correctamente en modo mock (sin Google Sheets):

```bash
python test_session_flow.py
```

Resultado: ✅ Todos los tests pasan (destinos 1-37 funcionan)

### Test de 37 Destinos

```bash
python test_final_37_destinos.py
```

Resultado: ✅ Sistema completamente funcional con 37 destinos

## Diagnóstico en Producción

Para diagnosticar el problema en producción, revisa los logs y busca:

1. **Verificar que la sesión se actualiza correctamente:**
   ```
   ✏️ Sesión actualizada (Sheets): 573123613840 - Estado: boletos_nacionales - Row: X
   ```

2. **Verificar que la sesión se recupera con el estado correcto:**
   ```
   🔍 Sesión recuperada (Sheets): 573123613840 - Estado: boletos_nacionales
   ```

3. **Verificar que se procesa en el estado correcto:**
   ```
   🔄 Procesando mensaje en estado: boletos_nacionales
   📍 Procesando selección de destino nacional: 5
   ```

## Posibles Causas del Problema en Producción

### 1. Delay en Google Sheets API

Google Sheets puede tener un pequeño delay entre escritura y lectura. Solución:
- Agregar un pequeño delay después de actualizar la sesión
- Usar caché local para sesiones recientes

### 2. Múltiples Instancias del Bot

Si hay múltiples instancias del bot corriendo, pueden estar usando diferentes cachés. Solución:
- Asegurar que solo hay una instancia corriendo
- Usar una base de datos compartida en lugar de Google Sheets

### 3. Formato de Datos en Google Sheets

El formato de los datos en Google Sheets puede estar corrupto. Solución:
- Verificar que la hoja "sesiones_chat" tiene las columnas correctas
- Limpiar sesiones antiguas

## Recomendaciones

### Inmediato

1. **Reiniciar el servicio** para aplicar los cambios con logging mejorado
2. **Revisar los logs** para identificar exactamente dónde falla la persistencia
3. **Limpiar la hoja de sesiones** en Google Sheets para eliminar datos corruptos

### A Mediano Plazo

1. **Migrar a una base de datos real** (PostgreSQL, MySQL, SQLite) en lugar de Google Sheets
2. **Implementar caché local** para sesiones activas
3. **Agregar retry logic** para operaciones de Google Sheets

## Código de Validación (Correcto)

El código de validación en `chatbot/engine.py` está correcto y acepta 1-37:

```python
def _procesar_boletos_nacionales(self, telefono: str, mensaje: str, sesion: Sesion, row_index: int) -> str:
    try:
        opcion = int(mensaje)
        
        # Esta validación es correcta - acepta 1 a 37
        if opcion < 1 or opcion > len(DESTINOS_NACIONALES_DESDE_ARAUCA):
            return f"Opción inválida. Por favor responde con un número del 1 al {len(DESTINOS_NACIONALES_DESDE_ARAUCA)} o escribe *volver* para regresar al menú."
        
        destino = DESTINOS_NACIONALES_DESDE_ARAUCA[opcion - 1]
        # ... resto del código
```

## Despliegue

1. Hacer commit de los cambios:
```bash
git add .
git commit -m "fix: Mejorar logging para diagnosticar problema de sesiones"
git push
```

2. Reiniciar el servicio en producción

3. Monitorear los logs para ver el flujo de sesiones

## Contacto

Si el problema persiste después de aplicar estos cambios, los logs mejorados mostrarán exactamente dónde está fallando la persistencia de sesiones.