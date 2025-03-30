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
- 🧘‍♂️ Enviarte recomendaciones inteligentes, recordatorios y mensajes con empatía.

## 🧠 ¿Cómo está compuesto este agente?

| Parte                 | ¿Qué hace?                            | Ejemplo                                           |
|----------------------|----------------------------------------|--------------------------------------------------|
| **Percepción**       | Observa el estado del entorno          | Lee tus tareas en Notion                         |
| **Modelo del entorno** | Entiende las consecuencias de actuar o no | ¿Qué pasa si dejo esta tarea para mañana?    |
| **Módulo de decisión** | Elige qué hacer según prioridades     | Calcula urgencia, impacto, estancamiento         |
| **Ejecución**        | Toma acción                            | Te escribe por Telegram con el resumen del día   |

---

### 🚦 Prioriza tareas con lógica configurable

El agente decide qué tareas son más urgentes e importantes, basándose en:

| Columna en Notion | ¿Cómo influye? |
|-------------------|----------------|
| **Priority**       | Da más peso a tareas *High*, menos a *Low*. |
| **Due Date**       | Penaliza si ya está vencida. Premia si está próxima. |
| **Status**         | Ignora tareas *Completed* o *Canceled*. Da puntuación parcial a *In progress*. |

Todo esto está definido en el archivo [`reglas.yaml`](reglas.yaml), que puedes modificar como quieras:

```yaml
prioridad:
  High: 3
  Medium: 2
  Low: 1

estado:
  Completed: 0
  Canceled: 0
  subtask-checked: 0.5
  In progress: 1
  Not started: 1

fecha_limite:
  penalizacion_dias_vencida: 1.5
  penalizacion_dias_restantes: 0.2
```

Puedes adaptar esta lógica a tu realidad. Por ejemplo:
- Poner más peso a las tareas urgentes aunque sean poco importantes.
- O lo contrario: priorizar tareas *High* aunque no tengan fecha límite.

---

## 🧰 Tecnologías usadas

- **Python**
- **Notion MCP** – lectura estructurada de tareas
- **MCP Telegram** – canal de comunicación natural
- **Pydantic AI** – validación estructurada de datos para el agente
- **YAML** – configuración editable de prioridades y mensajes
- **Docker** – para ejecución automática cada día

---

## 📁 Estructura del proyecto

```
secretario-ia/
├── mcp_client.py           # Cliente HTTP para servidores MCP
├── notion_client.py        # Script principal para probar el agente
├── prioritize.py           # Lógica de puntuación de tareas
├── format_message.py       # (futuro) Generación de mensajes para Telegram
├── initiatives.yaml        # (futuro) Ideas y recordatorios que puede sugerir el agente
├── mcp_servers/
│   └── api_server.py       # API REST para Notion usando MCP
├── .env                    # Variables de entorno (ID de Notion, tokens, etc.)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Requisitos

- Python 3.10+
- Una integración en Notion con acceso a tu base de tareas
- [`notion-mcp`](https://github.com/ccabanillas/notion-mcp) clonado localmente

---

## 🧪 Instalación y ejecución

### 1. Clona este repositorio

```bash
git clone https://github.com/Rauljauregi/secretario-ia.git
cd secretario-ia
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configura tu archivo `.env`

Crea un archivo `.env` en la raíz con el ID de tu base de datos de Notion:

```env
NOTION_DATABASE_ID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### 3. Prepara el servidor `notion-mcp`

En una carpeta paralela:

```bash
git clone https://github.com/ccabanillas/notion-mcp.git
cd notion-mcp
python -m venv venv
source venv/bin/activate
pip install -e .

# Crea tu archivo .env para este servidor
echo "NOTION_API_KEY=your_notion_token" > .env
```

### 4. Ejecuta el servidor como API REST

Desde dentro de `notion-mcp/src/notion_mcp`:

```bash
uvicorn api_server:app --reload
```

> El archivo `api_server.py` se encuentra en `secretario-ia/mcp_servers/`. Cópialo allí si no existe.

### 5. Ejecuta el agente

```bash
cd secretario-ia
source venv/bin/activate
python notion_client.py
```

---

## 📚 Artículos del blog

Este proyecto se documenta paso a paso en el blog:

| Nº | Título |
|----|--------|
| 1 | [Tu secretario inteligente](https://mindfulml.vialabsdigital.com/post/secretario-inteligente-1/) |
| 2 | [Cómo conectar tu agente con Notion y empezar a priorizar tu día](https://mindfulml.vialabsdigital.com/post/secretario-inteligente-2/) |
| 3 | [¿Qué hago primero hoy? Cómo prioriza el agente tus tareas](https://mindfulml.vialabsdigital.com/post/secretario-inteligente-3/)|
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
