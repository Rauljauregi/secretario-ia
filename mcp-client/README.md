# MCP Proxy para Claude Desktop

Este archivo `proxy_mcp.py` actúa como **puente (proxy)** entre Claude Desktop y el servidor MCP remoto (`https://mcp.vialabsdigital.com`). También proporciona herramientas personalizadas y contextos seleccionables para Claude, como tareas de Notion.

## 🚀 ¿Qué hace este proxy?

- Expone herramientas MCP compatibles con Claude Desktop (`process`, `notion_tool`)
- Permite a Claude seleccionar contextos (`/contextos`)
- Llama al servidor MCP en producción
- Simula acciones en Notion (o reales, si activas tu API Key)

---

## 📁 Estructura

```bash
/mcp-client/
│
├── proxy_mcp.py     # Proxy MCP que Claude puede usar por stdin
├── .env             # Debes crear este archivo con tu NOTION_API_KEY
└── README.md        # Este documento
```

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Claude Desktop instalado
- Archivo `.env` con tu clave de Notion:
  ```env
  NOTION_API_KEY=secret_xxx_tu_clave_aqui
  ```

- Instala los paquetes necesarios:
  ```bash
  pip install -r requirements.txt
  ```

> Puedes crear el archivo `requirements.txt` con estas líneas:
```txt
httpx
python-dotenv
mcp
```

---

## ▶️ Ejecución del Proxy

Desde la raíz del proyecto (donde está `proxy_mcp.py`):

```bash
set PYTHONPATH=.
python proxy_mcp.py --stdio
```

> En Mac/Linux:
```bash
export PYTHONPATH=.
python3 proxy_mcp.py --stdio
```

---

## 🧠 Conexión con Claude Desktop

1. Asegúrate de que Claude Desktop esté cerrado.
2. Edita el archivo de configuración `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mcp-vialabs-remote": {
      "command": "python",
      "args": ["proxy_mcp.py", "--stdio"],
      "cwd": "/ruta/completa/a/mcp-client/"
    }
  }
}
```

> En Windows, `"cwd"` es obligatorio si no estás en la misma ruta. Usa rutas absolutas con `\\` o `/`.

3. Inicia Claude Desktop.
4. Abre el botón 🛠️ “Tools” y activa tus herramientas.
5. (Opcional) Abre el menú “📤 Share context” si deseas seleccionar un contexto (ej: Tareas de Notion).

---

## 📚 Herramientas y Contextos disponibles

- `process`: Llama al endpoint `/process` del servidor MCP.
- `notion_tool`: Simula acciones con páginas de Notion.
- `listar_contextos`: Devuelve dos contextos de ejemplo para Claude.

---

## 🧪 Pruebas sugeridas

- Pregunta a Claude: *“¿Qué herramientas tienes disponibles?”*
- Escribe: *“Usa `notion_tool` para crear una página llamada Plan Semanal”*
- Cambia el contexto desde el menú "📤 Compartir contexto"

---

## ✨ Créditos

Este proxy ha sido creado como parte del proyecto **[Secretario IA](https://github.com/raulj/secretario-ia)**, un agente personal conectado a servicios como Notion, Telegram y más.

---

¿Tienes dudas o sugerencias?  
Escríbenos o abre un issue en el repositorio 🚀
```
