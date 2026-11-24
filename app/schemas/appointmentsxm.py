from pydantic import BaseModel,Field
from sqlalchemy import Date

class AppointmentCreateSchemas(BaseModel):
    date:Date
    start_time:str
    end_time:str
    status:str=Field(min_length=2,max_length=250)
    reason:str
    doctor_note:str

class AppointmentUpdateSchemas(BaseModel):
    date:Date |None=None
    start_time:str|None=None
    end_time:str|None=None
    status:str|None=None
    reason:str|None=None
    doctor_note:str|None=None