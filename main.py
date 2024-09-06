from fastapi import FastAPI
from enum import Enum
from typing import Optional, Union

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

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):  
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {item_id: item_id}
    if q:
        item.update({"q": q})
    if not short:    
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

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