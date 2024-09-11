from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from datetime import datetime, timedelta, time
from uuid import UUID
from typing import Union

app = FastAPI()

"""
Part 11: Extra Data Types
"""

@app.put("/items/{item_id}")
async def read_items(item_id:UUID, start_date:Union[datetime, None] = Body(None), end_date:Union[datetime, None] = Body(None), repeat_at:Union[time, None] = Body(None), process_after:Union[timedelta, None] = Body(None)):
    start_process = start_date + process_after
    duration = end_date - start_date
    return {"item_id": item_id, "start_date": start_date, "end_date": end_date, "repeat_at": repeat_at, "process_after": process_after, "start_process": start_process, "duration": duration}