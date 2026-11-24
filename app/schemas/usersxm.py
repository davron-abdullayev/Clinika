from pydantic import BaseModel,Field

class UserCreateSchemas(BaseModel):
    full_name:str=Field(min_length=2,max_length=250)
    username:str
    password:str |None=None

class UserUpdateSchemas(BaseModel):
    full_name:str |None=None
    username:str |None=None
    password:str |None=None

class UserRegisterSchemas(BaseModel):
    full_name:str=Field(min_length=2,max_length=250)
    username:str
    password:str 

class UserLoginSchemas(BaseModel):
    username:str
    password:str 

