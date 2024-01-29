from fastapi import FastAPI, RedirectResponse

app = FastAPI()

# Configure handler for POST route '/'
@app.post("/")
async def post_root():
    return {"post": "ok"}

# Configure handler for POST route '/{id}'
@app.post("/{id}")
async def post_with_id(id: str):
    target_url = f"https://api.klix.ba/v1/rate/{id}"
    # Here you can add logic for request redirection or processing to the target URL

    # Example of redirecting to the target URL without raising an exception
    response = RedirectResponse(url=target_url, status_code=308)
    return response
