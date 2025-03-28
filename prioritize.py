import yaml
import pandas as pd

def cargar_pesos(path="prioridades.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def priorizar_tareas(df_tareas: pd.DataFrame, pesos: dict) -> pd.DataFrame:
    def puntuar(fila):
        score = 0
        for campo, reglas in pesos.items():
            valor = fila.get(campo)
            if valor in reglas:
                score += reglas[valor]
        return score

    df_tareas = df_tareas.copy()
    df_tareas["score"] = df_tareas.apply(puntuar, axis=1)
    df_tareas = df_tareas.sort_values(by="score", ascending=False)
    return df_tareas
