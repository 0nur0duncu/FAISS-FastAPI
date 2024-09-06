from fastapi import FastAPI
from enum import Enum
from typing import Optional, Union
from pydantic import BaseModel

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
    

class Item(BaseModel): # request body
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post("/items")
async def create_item(item : Item): #-> Item
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

# uvicorn main:app --host 127.0.0.1 --port 5000 --reload
"""
raw body:
{
    "name": "Hi",
    "description": "Hello World", varsayılan değer None olduğu için ybody de yazılmayabilir.
    "price": 0,
    "tax": 0
}
header:
"Content-Type":application/json
"""