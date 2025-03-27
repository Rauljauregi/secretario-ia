# 🤖 secretario-ia

**Tu secretario inteligente**: un agente modular con IA que organiza tu día, prioriza tareas y te habla por Telegram.

Este es un proyecto personal en desarrollo, creado con la idea de explorar cómo podemos usar inteligencia artificial de forma práctica, realista y útil para el día a día profesional.  
Si tú también gestionas muchas tareas, clientes y decisiones… esto es para ti.

---

## 🚀 ¿Qué hace este agente?

En su versión actual:

- 🗂️ **Lee tus tareas desde Notion** (usando [`notion-mcp`](https://github.com/ccabanillas/notion-mcp))
- 🧠 **Decide qué tareas son más importantes hoy** (con reglas configurables)
- 💬 **Te manda un resumen diario por Telegram** (usando [`mcp-telegram`](https://github.com/sparfenyuk/mcp-telegram))

Y próximamente:

- 🗣️ Podrás **hablar con él por Telegram** (gracias a un modelo LLM)
- ✍️ **Modificar tareas en Notion desde el chat**
- 🧘‍♂️ Enviarte recomendaciones inteligentes, recordatorios y mensajes con empatía

---

## 🧠 ¿Cómo está compuesto este agente?

| Parte | ¿Qué hace? | Ejemplo |
|-------|------------|---------|
| **Percepción** | Observa el estado del entorno | Lee tus tareas en Notion |
| **Modelo del entorno** | Entiende las consecuencias de actuar o no | ¿Qué pasa si dejo esta tarea para mañana? |
| **Módulo de decisión** | Elige qué hacer según prioridades | Calcula urgencia, impacto, estancamiento |
| **Ejecución** | Toma acción | Te escribe por Telegram con el resumen del día |

---

## 🧰 Tecnologías usadas

- **Python**
- **Notion MCP** · lectura estructurada de tareas
- **MCP Telegram** · canal de comunicación natural
- **Pydantic AI** · validación estructurada de datos para el agente
- **YAML** · para definir reglas y configuraciones
- **Docker** · para ejecutar el agente cada día automáticamente

---

## 🗂 Estructura del proyecto (en progreso)
/src main.py 
Lógica principal del agente prioritize.py 
Lógica de puntuación de tareas format_message.py 
Generación del mensaje Telegram initiatives.yaml 
Mensajes y recomendaciones inteligentes /config settings.env 
Variables de entorno (token, chat_id, etc.) /notion_export 
Datos simulados para testeo 
README.md 
requirements.txt 
Dockerfile


---

## 📚 Artículos del blog

Este repositorio va acompañado de una serie de artículos explicativos:

| Nº | Título |
|----|--------|
| 1 | [Tu secretario inteligente]([https://www.mindfulml.vialabsdigital.com](https://mindfulml.vialabsdigital.com/post/secretario-inteligente-1/)) |
| 2 | Cómo conectar tu agente con Notion y empezar a priorizar tu día |
| 3 | ¿Qué hago primero hoy? Cómo decidir tareas con IA (sin volverte loco) |
| 4 | Habla con tu agente por Telegram |
| 5 | Añade un LLM a tu agente |
| 6 | Tu agente también actúa |
| 7 | Dale memoria y emociones |
| 8 | De asistente a compañero |
| … | *(y los que vendrán)* |

---

## 🤝 Contribuciones

Este proyecto está en desarrollo y es completamente abierto.  
Si quieres proponer mejoras, usarlo en tu empresa o adaptarlo a tus flujos… estoy encantado de escuchar ideas.

👉 [www.vialabsdigital.com](https://www.vialabsdigital.com)

---

## 📝 Licencia

MIT – libre uso, modificación y distribución. Solo te pido que cites el origen.  

