from fastapi import FastAPI
from enum import Enum

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

@app.get("/items")
async def get_items():  
    return {"message": "Hello from get items route"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"message": "Hello from get item route", "item_id": item_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    diary = "diary"

@app.get("/food/{food_type}")
async def get_food(food_type: FoodEnum):
    if food_type == FoodEnum.fruits:
        return {"message": "Hello from get fruits route"}
    elif food_type == FoodEnum.vegetables:
        return {"message": "Hello from get vegetables route"}
    elif food_type == FoodEnum.diary:
        return {"message": "Hello from get diary route"}

# uvicorn main:app --host 127.0.0.1 --port 5000 --reload