from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, Union, List
from pydantic import BaseModel

app = FastAPI()

"""
Part-7 -> Body -> Multiple Parameters
"""

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

class Importance(BaseModel):
    importance: int

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=150),
    q: Union[str, None] = None,
    # item: Union[Item, None] = None,
    item: Item = Body(..., embed=True),
    user: User,
    importance: int = Body(...),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    if importance:
        results.update({"importance": importance})
    return results

# Ctrl + Ö yorum satırı
#Shift + Alt + A blok yorum satırı

""" 
{
item : {},
user : {}
}
"""