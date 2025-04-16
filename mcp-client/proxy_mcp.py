from mcp.server.fastmcp import FastMCP
from typing import Any
import httpx
import sys
from notion_mcp.client import NotionClient
from pathlib import Path
import os

from dotenv import load_dotenv

# Cargar variables de entorno desde .env
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
if not NOTION_API_KEY:
    raise ValueError("No se encontró NOTION_API_KEY en .env")

notion = NotionClient(NOTION_API_KEY)

print("MCP proxy iniciado desde Claude", file=sys.stderr)

mcp = FastMCP("remote-mcp")

# 👉 Herramienta que actúa como proxy
@mcp.tool()
async def process(input: str, context: dict[str, Any] = {}) -> dict:
    async with httpx.AsyncClient() as client:
        print(f"Tool process() fue llamado con: {input}, contexto: {context}", file=sys.stderr)
        response = await client.post("https://mcp.vialabsdigital.com/process", json={
            "input": input,
            "context": context
        })
        return response.json()

# 👉 Herramienta para simular acciones en Notion
@mcp.tool()
async def notion_tool(action: str, page_title: str, content: str = "", database_id: str = "") -> dict:
    print(f"[NOTION TOOL] Acción: {action}, Título: {page_title}", file=sys.stderr)
    return {
        "status": "mocked",
        "message": f"Simulando acción '{action}' en Notion con título '{page_title}'"
    }

# 👉 Recurso de Claude que obtiene tareas desde Notion
@mcp.resource("http://localhost/notion/tasks")
async def notion_tasks_resource() -> list[dict[str, str]]:
    database_id = "0ca19f2f-d10c-484a-86cd-5d2dbb1662e8"  # Cambiar si deseas hacerlo dinámico
    try:
        results = await notion.query_database(database_id=database_id)
        tareas = []
        for r in results["results"]:
            props = r.get("properties", {})
            nombre = ""
            if "Task" in props:
                nombre = " ".join(t.get("plain_text", "") for t in props["Task"]["title"])
            tareas.append({
                "ID": r.get("id"),
                "Nombre": nombre
            })
        return tareas
    except Exception as e:
        print(f"❌ Error al obtener tareas de Notion: {e}", file=sys.stderr)
        return []

# 👉 Recurso para que Claude pueda ofrecer un selector de contexto
@mcp.resource("http://localhost/contextos")
async def contextos() -> list[dict[str, str]]:
    return [
        {"ID": "notion_tasks_0ca19f2f", "Nombre": "Tareas de Notion"},
        {"ID": "proyectos_demo", "Nombre": "Proyectos de ejemplo"}
    ]

# 👉 Punto de entrada
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--stdio":
        mcp.run(transport="stdio")
    else:
        print("Ejecutado sin --stdio, iniciando MCP igualmente", file=sys.stderr)
        mcp.run(transport="stdio")
