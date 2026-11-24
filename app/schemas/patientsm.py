from pydantic import BaseModel,Field
from sqlalchemy import Date

class PatientCreateSchemas(BaseModel):
    phone:str=Field(min_length=2,max_length=250)
    birth_date:Date
    address:str 

class PatientUpdateSchemas(BaseModel):
    phone:str |None=None
    birth_date:Date|None=None
    address:str |None=None
