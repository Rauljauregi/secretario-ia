from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/context")
async def context(request: Request):
    body = await request.json()
    db_name = body.get("query", {}).get("database_name", "")
    print(f"📥 Petición recibida para la base de datos: {db_name}")
    return {
        "context": [
            {"Nombre": "Llamar al cliente A", "Prioridad": "Alta"},
            {"Nombre": "Preparar propuesta B", "Prioridad": "Media"},
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
