from fastapi import FastAPI, Path, Body
import json

app = FastAPI()

# Função para ler o carrinho do usuário do arquivo de texto
def ler_carrinho(user_id):
    try:
        with open(f"carrinho_data/{user_id}_cart.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Função para escrever o carrinho do usuário no arquivo de texto
def escrever_carrinho(user_id, carrinho):
    with open(f"carrinho_data/{user_id}_cart.txt", "w") as file:
        json.dump(carrinho, file)

# Endpoint para adicionar um item ao carrinho
@app.post("/carrinho/{user_id}/add")
async def add_item_to_cart(user_id: int = Path(..., title="ID do usuário"), produto_id: int = Body(..., embed=True), quantidade: int = Body(..., embed=True)):
    carrinho = ler_carrinho(user_id)
    carrinho[produto_id] = quantidade
    escrever_carrinho(user_id, carrinho)
    return {"status": "sucesso", "mensagem": "Produto adicionado ao carrinho"}

# Endpoint para listar o carrinho do usuário
@app.get("/carrinho/{user_id}")
async def listar_carrinho(user_id: int = Path(default=None, description="ID do usuário")):
    return ler_carrinho(user_id)
