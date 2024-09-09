from fastapi import FastAPI, Query, Path, Body
from enum import Enum
from typing import Optional, Union, List
from pydantic import BaseModel, Field

app = FastAPI()

"""
Part 8: Body - Field
"""

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(None, title="Description of the item", max_length=300)
    price : float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item = Body(...,embed=True)
):
    result = {"item_id": item_id, "item": item}
    return result
