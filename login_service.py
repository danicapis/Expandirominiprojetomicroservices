from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/login")
async def login(username: str, password: str):
    if username == "user" and password == "password":
        return {"status": "sucesso", "mensagem": "Usuário autenticado"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")