from mcp_client import MCPClient
from prioritize import cargar_pesos, priorizar_tareas
import pandas as pd
from dotenv import load_dotenv
import os

# Cargar .env
load_dotenv()

MCP_NOTION_URL = "http://localhost:8000/context"
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def obtener_tareas_desde_notion():
    if not NOTION_DATABASE_ID:
        print("❌ No se ha definido NOTION_DATABASE_ID en el .env")
        return pd.DataFrame()

    cliente = MCPClient(MCP_NOTION_URL)
    tareas = cliente.query(NOTION_DATABASE_ID)
    df = pd.DataFrame(tareas)

    if df.empty:
        print("⚠️ No se encontraron tareas.")
        return df

    print("✅ Tareas recibidas:")
    print(df[["Nombre"]]) if "Nombre" in df.columns else print(df.head())

    # Aplicar prioridad
    pesos = cargar_pesos()
    df_prioritizadas = priorizar_tareas(df, pesos)

    print("📋 Tareas priorizadas:")
    print(df_prioritizadas[["Nombre", "score"]].sort_values("score", ascending=False))

    return df_prioritizadas

if __name__ == "__main__":
    obtener_tareas_desde_notion()
