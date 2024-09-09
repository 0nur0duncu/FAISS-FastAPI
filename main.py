from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, Union, List
from pydantic import BaseModel, Field
import re

app = FastAPI()

"""
Part 9: Body - Nested Models
"""

class Image(BaseModel):
    url: str = Field(..., regex=re("^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"))
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(None, title="Description of the item", max_length=300)
    price : float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None
    # tags : List[int] = []
    tags : set[str] = set()
    # image : Union[Image, None] = None
    image: Union[List[Image], None] = None

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item]

@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item = Body(...,embed=True)
):
    result = {"item_id": item_id, "item": item}
    return result

@app.put("/offers")
async def create_offer(offer: Offer = Body(...,embed=True)):
    return offer

@app.post("/images/multiple")
async def create_multiple_images(images: List[Image] = Body(...,embed=True)):
    return images

@app.post("blah")
async def create_some_item(blah: dict[int, float]):
    return blah