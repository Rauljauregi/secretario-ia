from fastapi import FastAPI, Request
from notion_mcp.client import NotionClient
import os
from dotenv import load_dotenv
import json  # <-- para imprimir mejor los resultados

app = FastAPI()

# Cargar variables de entorno desde .env
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
dotenv_path = os.path.join(project_root, ".env")
load_dotenv(dotenv_path)

NOTION_API_KEY = os.getenv("NOTION_API_KEY")

if not NOTION_API_KEY:
    raise ValueError("⚠️ No se encontró NOTION_API_KEY en el .env")

notion = NotionClient(NOTION_API_KEY)

@app.post("/context")
async def context(request: Request):
    body = await request.json()
    db_id = body.get("query", {}).get("database_id")

    if not db_id:
        print("❌ No se recibió un database_id")
        return {"context": []}

    print(f"📥 Petición MCP con ID: {db_id}")
    
    try:
        results = await notion.query_database(database_id=db_id)
    except Exception as e:
        print(f"❌ Error al consultar Notion: {e}")
        return {"context": []}

    print("📦 Resultados crudos desde Notion:")
    print(json.dumps(results, indent=2))  # <-- para ver bien en consola

    tareas = []
    for r in results.get("results", []):
        props = r.get("properties", {})

        # Imprimir los nombres de los campos para depuración
        print("🔍 Propiedades de una tarea:", list(props.keys()))

        tarea = {
            "Nombre": props.get("Name", {}).get("title", [{}])[0].get("plain_text", ""),
            "Prioridad": props.get("Prioridad", {}).get("select", {}).get("name", "Baja"),
        }
        tareas.append(tarea)

    print(f"✅ Tareas procesadas: {len(tareas)}")
    return {"context": tareas}
