from fastapi import FastAPI
import json

app = FastAPI()

# Função para ler os produtos do arquivo de texto
def ler_produtos():
    try:
        with open("produtos_data/produtos.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Endpoint para listar produtos
@app.get("/produtos")
async def listar_produtos():
    return ler_produtos()
