import requests

class MCPClient:
    def __init__(self, endpoint_url: str):
        self.endpoint_url = endpoint_url

    def query(self, database_id: str) -> list:
        payload = {
            "query": {
                "database_id": database_id
            }
        }
        try:
            response = requests.post(self.endpoint_url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("context", [])
        except Exception as e:
            print(f"❌ Error al consultar MCP: {e}")
            return []
