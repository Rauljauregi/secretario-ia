from fastapi import FastAPI, Request
from notion_mcp.client import NotionClient
import os
from dotenv import load_dotenv
import json  # <-- para imprimir mejor los resultados
import traceback

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
        print("❌ No se recibió un database_id válido")
        return {"context": []}

    try:
        results = await notion.query_database(database_id=db_id)
        print(f"📥 Petición MCP con ID: {db_id}")

        tareas = []
        for r in results["results"]:
            props = r.get("properties", {})
            id_tarea = r.get("id")
            sub_items = props.get("Sub-item", {}).get("relation", [])
            parent_item = props.get("Parent item", {}).get("relation", [])

            # Extraer los IDs de relación (si existen)
            sub_ids = [s.get("id") for s in sub_items]
            parent_id = parent_item[0]["id"] if parent_item else None

            print("🧩 Propiedades disponibles:", props.keys())
            due_date = ""
            due_date_prop = props.get("Due Date")
            if isinstance(due_date_prop, dict):
                date_value = due_date_prop.get("date")
                if isinstance(date_value, dict):
                    due_date = date_value.get("start", "")

            task_prop = props.get("Task", {})
            nombre = ""
            if task_prop and isinstance(task_prop, dict):
                title_list = task_prop.get("title", [])
                if title_list and isinstance(title_list, list):
                    nombre = " ".join(t.get("plain_text", "") for t in title_list if isinstance(t, dict))

            priority = ""
            priority_prop = props.get("Priority")
            if isinstance(priority_prop, dict):
                select_value = priority_prop.get("select")
                if isinstance(select_value, dict):
                    priority = select_value.get("name", "Baja")

            tarea = {
                "ID": id_tarea,
                "Nombre": nombre,
                "Prioridad": priority,
                "Fecha": due_date,
                "Subtareas": sub_ids,
                "Padre": parent_id
            }



            tareas.append(tarea)

        return {"context": tareas}

    except Exception as e:
        print(f"❌ Error al consultar Notion: {e}")
        traceback.print_exc()  # <- esto imprime el error completo
        return {"context": []}
