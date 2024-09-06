from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from get route"}

@app.post("/")
async def post():
    return {"message": "Hello from post route"}

@app.put("/")
async def put():
    return {"message": "Hello from put route"}

# uvicorn main:app --host 127.0.0.1 --port 5000 --reload