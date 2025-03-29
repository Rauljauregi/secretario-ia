import requests
import yaml
import pandas as pd
from datetime import datetime
from dateutil.parser import parse as parse_date

# Cargar reglas desde el archivo YAML
def cargar_reglas():
    with open("prioridades.yaml", "r") as f:
        return yaml.safe_load(f)

# Calcular puntuación de una tarea
def calcular_score(tarea, reglas):
    score = 0

    prioridades = reglas.get("prioridad", {})
    estados = reglas.get("estado", {})
    fecha_cfg = reglas.get("fecha_limite", {})

    prioridad = tarea.get("Prioridad", "Low")
    estado = tarea.get("Estado", "Not started")
    fecha_str = tarea.get("Fecha", "")

    # Prioridad
    score += prioridades.get(prioridad, 0)

    # Estado
    score += estados.get(estado, 0)

    # Fecha
    if fecha_str:
        try:
            fecha = parse_date(fecha_str).date()
            hoy = datetime.today().date()
            diferencia = (fecha - hoy).days

            if diferencia < 0:
                # Tarea vencida
                score += abs(diferencia) * fecha_cfg.get("penalizacion_dias_vencida", 1.5)
            else:
                # Aún queda margen
                score += (7 - min(diferencia, 7)) * fecha_cfg.get("penalizacion_dias_restantes", 0.2)
        except Exception as e:
            print(f"⚠️ Fecha malformada: {fecha_str} -> {e}")

    return round(score, 2)

# Llamar al servidor local de Notion MCP
def obtener_tareas():
    url = "http://localhost:8000/context"
    payload = {
        "query": {
            "database_id": "0ca19f2f-d10c-484a-86cd-5d2dbb1662e8"
        }
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        datos = response.json()
        return datos.get("context", [])
    except Exception as e:
        print(f"❌ Error al consultar MCP: {e}")
        return []

# Programa principal
if __name__ == "__main__":
    tareas = obtener_tareas()
    if not tareas:
        print("⚠️ No se encontraron tareas.")
        exit()

    print("✅ Tareas recibidas:")
    df = pd.DataFrame(tareas)
    print(df[["Nombre"]])

    reglas = cargar_reglas()
    df["score"] = df.apply(lambda row: calcular_score(row, reglas), axis=1)
    df_ordenado = df.sort_values(by="score", ascending=False)

    print("📋 Tareas priorizadas:")
    print(df_ordenado[["Nombre", "score"]])
