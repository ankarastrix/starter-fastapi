from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

# Konfigurišite handler za POST rutu '/'
@app.post("/")
async def post_root():
    return {"post": "ok"}

# Konfigurišite handler za POST rutu '/{id}'
@app.post("/{id}")
async def post_with_id(id: str):
    target_url = f"https://api.klix.ba/v1/rate/{id}"
    # Ovde možete dodati logiku preusmeravanja ili obrade zahteva prema ciljnoj adresi

    # Primer preusmeravanja na ciljanu adresu
    raise HTTPException(status_code=308, detail=target_url)

# Ostatak vaših ruta i podešavanja
