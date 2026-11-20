from sqlalchemy import BigInteger,Boolean, Integer,String, Text
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from sqlalchemy import DateTime
from enum import Enum
from sqlalchemy import Enum as SQLEnum

from . import db

class Doctor(db.Model):
    __tablename__='doctors'

    id:Mapped[int]=mapped_column(BigInteger(),primary_key=True,nullable=False)
    specialty:Mapped[str]=mapped_column(String(100),nullable=False)
    room:Mapped[str]=mapped_column(String(20),nullable=False)
    experience_years:Mapped[int]=mapped_column(Integer(),nullable=False)
    bio:Mapped[str]=mapped_column(String(255),nullable=False)
    is_active:Mapped[bool]=mapped_column(Boolean(),default=True)
    user_id:Mapped["User"]=relationship(back_populates="doctors")

    def _dict(self):
            return{
                "id":self.id,
                "specialty":self.specialty,
                "room":self.room,
                "experience_years":self.experience_years,
                "bio":self.bio
            }
