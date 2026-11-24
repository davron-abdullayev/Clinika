from pydantic import BaseModel,Field
from sqlalchemy import Date

class DoctorCreateSchemas(BaseModel):
    specialty:str=Field(min_length=2,max_length=250)
    room:str
    experience_yaers:int
    bio:str

class DoctorUpdateSchemas(BaseModel):
    specialty:str |None=None
    room:str|None=None
    experience_yaers:int|None=None
    bio:str|None=None