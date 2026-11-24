from pydantic import BaseModel,Field
from sqlalchemy import Date

class ScheduleCreateSchemas(BaseModel):
    weekday:int
    start_time:str
    end_time:str
    slot_minutes:int 

class ScheduleUpdateSchemas(BaseModel):
    weekday:str|None=None
    start_time:str |None=None
    end_time:str|None=None
    slot_minutes:int|None=None