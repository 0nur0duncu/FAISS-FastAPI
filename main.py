from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from typing import Optional, Union, List
from pydantic import BaseModel, Field
import re

app = FastAPI()

"""
Part 10: Declare Request Example Data
"""

class Item(BaseModel):
    """ name: str = Field(..., example="Foo")
    description: Union[str, None] = Field(None, example="A very nice Item")
    price: float = Field(..., example=16.25)
    tax: Union[float, None] = Field(None, example=10.5) """
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = []

    class Config: # yöntem 1
        json_schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 16.25,
                "tax": 1.67
            }
        }

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(..., examples={"normal": {"name": "Foo", "description": "A very nice Item", "value" :{"price": 16.25, "price": 1.67}}, "converted": { "summary": "An example with converted data", "description": "FastAPI can convert prices 'string'", "value": {"name":"bar", "price":"16.25"}}, "invalid": {"summary":"invalid data is rejected with an error", "value": {"name":"Baz", "price":"sixteen point twenty five"}}}),
):
    pass