# ✅ Sistema de Handoff (Transferencia a Humano) - Funcionando

## Resumen

El sistema de handoff permite que cuando un cliente selecciona un destino, el bot se desactive automáticamente en ese chat específico, permitiendo que el asesor atienda manualmente al cliente. El bot solo se reactiva cuando el asesor lo indica o después de 12 horas.

## 🔄 Flujo Completo

### 1. Cliente Selecciona un Destino

```
Cliente: hola
Bot: [Muestra menú principal]

Cliente: 1
Bot: [Muestra 37 destinos nacionales]

Cliente: 5
Bot: ✅ Solicitud recibida - Pore, Casanare - $110.000
     Un asesor te contactará en breve...
     [BOT SE DESACTIVA EN ESTE CHAT]
```

### 2. Notificación al Profesional

El sistema envía automáticamente un mensaje al número del profesional (573001833654):

```
🔔 NUEVA SOLICITUD DE ATENCIÓN

👤 Cliente: [Nombre]
📱 Teléfono: 573123456789
📋 Tipo: Boleto Nacional
📍 Detalles: Arauca → Pore, Casanare | Precio: $110.000
⏰ Hora: 11/03/2026 10:05

Por favor, responde manualmente a este chat.

Para reactivar el bot después, escribe: "te dejo con el bot"
```

### 3. Bot Desactivado

Mientras el bot está desactivado en el chat del cliente:

```
Cliente: hola
[Sin respuesta - Bot desactivado]

Cliente: necesito ayuda
[Sin respuesta - Bot desactivado]

Cliente: cuánto cuesta
[Sin respuesta - Bot desactivado]
```

El asesor puede responder manualmente sin interferencia del bot.

### 4. Reactivación del Bot

El asesor puede reactivar el bot escribiendo cualquiera de estos comandos en el chat del cliente:

- `bot`
- `activar bot`
- `te dejo con el bot`
- `bot activo`
- `continua bot`
- `vuelve bot`
- `bot on`
- `activar chatbot`

```
Asesor (en el chat del cliente): bot

Bot: ✅ Bot reactivado
     Hola de nuevo! Estoy aquí para ayudarte.
     [Muestra menú principal]
```

### 5. Reactivación Automática

Si el asesor no reactiva el bot manualmente, el sistema lo reactiva automáticamente después de 12 horas.

## 📋 Comandos de Reactivación

| Comando | Descripción |
|---------|-------------|
| `bot` | Comando corto y rápido |
| `activar bot` | Comando explícito |
| `te dejo con el bot` | Comando natural |
| `bot activo` | Confirma activación |
| `continua bot` | Indica continuación |
| `vuelve bot` | Indica regreso |
| `bot on` | Comando técnico |
| `activar chatbot` | Comando formal |

## ⚙️ Configuración

### Tiempo de Reactivación Automática

Configurado en `config/constants.py`:

```python
HORAS_REACTIVACION_AUTO = 12  # 12 horas
```

### Número del Profesional

Configurado en `.env`:

```env
PROFESSIONAL_PHONE=573001833654
```

## 🧪 Tests Realizados

### Test 1: Desactivación del Bot
✅ Bot se desactiva cuando cliente selecciona destino
✅ Bot no responde a mensajes del cliente mientras está desactivado

### Test 2: Notificación al Profesional
✅ Mensaje enviado correctamente al profesional
✅ Incluye todos los datos del cliente y solicitud
✅ Status Code: 201 (éxito)

### Test 3: Comandos de Reactivación
✅ Comando "bot" funciona
✅ Comando "te dejo con el bot" funciona
✅ Comando "activar bot" funciona
✅ Todos los comandos reactivan correctamente

### Test 4: Funcionamiento Post-Reactivación
✅ Bot responde normalmente después de reactivarse
✅ Cliente puede usar todas las funciones del bot

## 📊 Estados del Bot

| Estado | Descripción | Bot Responde |
|--------|-------------|--------------|
| `inicio` | Estado inicial | ✅ Sí |
| `boletos_nacionales` | Seleccionando destino | ✅ Sí |
| `boletos_internacionales` | Seleccionando país | ✅ Sí |
| `handoff_humano` | Transferido a asesor | ❌ No |

## 🔍 Logs del Sistema

### Cuando el bot se desactiva:
```
INFO: ✏️ Sesión actualizada: 573123456789 - Estado: handoff_humano
INFO: 📤 Enviando notificación de handoff al profesional 573001833654
INFO: ✅ Mensaje enviado exitosamente a 573001833654
```

### Cuando el cliente intenta escribir (bot desactivado):
```
INFO: 🔇 Bot desactivado para 573123456789. Mensaje ignorado: hola
```

### Cuando el asesor reactiva el bot:
```
INFO: 🤖 Reactivando bot para 573123456789 por comando del asesor
INFO: ✏️ Sesión actualizada: 573123456789 - Estado: inicio
```

## ⚠️ Importante

### Solo el Asesor Debe Reactivar

Los comandos de reactivación están diseñados para que SOLO el asesor los use. En la práctica:

1. El asesor recibe la notificación en su chat
2. El asesor contacta al cliente (el bot está desactivado en ese chat)
3. Cuando termina la atención, el asesor escribe "bot" en el chat del cliente
4. El bot se reactiva y el cliente puede usarlo de nuevo

### Seguridad

- Cada chat tiene su propia sesión independiente
- Desactivar el bot en un chat NO afecta otros chats
- Las sesiones se almacenan en memoria (se limpian al reiniciar el servicio)
- Después de 12 horas, el bot se reactiva automáticamente

## 🚀 Casos de Uso

### Caso 1: Cliente Necesita Información Detallada
```
1. Cliente selecciona destino → Bot desactivado
2. Asesor llama al cliente para dar información detallada
3. Asesor escribe "bot" → Bot reactivado
4. Cliente puede consultar otros destinos
```

### Caso 2: Cliente Quiere Reservar
```
1. Cliente selecciona destino → Bot desactivado
2. Asesor procesa la reserva manualmente
3. Asesor confirma y escribe "te dejo con el bot"
4. Cliente puede hacer nuevas consultas
```

### Caso 3: Múltiples Clientes Simultáneos
```
Cliente A: Selecciona destino → Bot desactivado en chat A
Cliente B: Selecciona destino → Bot desactivado en chat B
Cliente C: Usa el bot normalmente → Bot activo en chat C

Cada chat es independiente
```

## 📝 Resumen de Funcionalidades

✅ Bot se desactiva automáticamente al seleccionar destino
✅ Notificación inmediata al profesional con todos los datos
✅ Bot no responde mientras está desactivado (solo en ese chat)
✅ 8 comandos diferentes para reactivar el bot
✅ Reactivación automática después de 12 horas
✅ Cada chat es independiente
✅ Sistema probado y funcionando correctamente

## 🎯 Próximos Pasos

1. Reiniciar el servicio para aplicar los cambios
2. Probar el flujo completo en producción
3. Verificar que las notificaciones lleguen correctamente
4. Capacitar al equipo en el uso de los comandos de reactivación

El sistema está listo para producción! 🎉