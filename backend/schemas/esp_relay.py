from pydantic import BaseModel
from typing import List

class RelaysReq(BaseModel):
    relays: List[int]