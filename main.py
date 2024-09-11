from fastapi import FastAPI, Query, Path, Body, Cookie, Header
from enum import Enum
from datetime import datetime, timedelta, time
from uuid import UUID
from typing import Union, List

app = FastAPI()

"""
Part 12: Cookie and Header Parameters
"""

@app.get("/items/")
async def read_items(cookie_id: Union[str, None] = Cookie(default=None), accept_encoding: Union[List[str], None] = Header(default=None, convert_underscores=False), sec_ch_ua: Union[str, None] = Header(default=None), user_agent: Union[str, None] = Header(default=None), x_token: list[str, None] = Header(default=None)):
    return {"cookie_id": cookie_id, "Accept-Encoding": accept_encoding, "sec-ch-ua": sec_ch_ua, "User-Agent": user_agent, "X-Token values": x_token}