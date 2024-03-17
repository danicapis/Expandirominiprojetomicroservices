from fastapi import FastAPI

app = FastAPI()

@app.post("/pedido/{user_id}/add")
async def create_order(user_id: int):
    with open(f"pedido_data/{user_id}_order.txt", "w") as order_file:
        order_file.write("Pedido criado\n")
    return {"status": "sucesso", "mensagem": "Pedido criado"}
