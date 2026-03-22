from fastapi import FastAPI

app = FastAPI(title="FAST Backend")

@app.get("/")
def read_root():
    return {"message": "FAST backend rodando"}
