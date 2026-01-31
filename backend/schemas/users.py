from pydantic import BaseModel

class UserCreate(BaseModel):
    pria : str
    wanita : str
