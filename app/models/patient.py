from sqlalchemy import BigInteger,Boolean, Date, ForeignKey, Integer,String, Text
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from sqlalchemy import DateTime
from enum import Enum
from sqlalchemy import Enum as SQLEnum

from . import db

class Patient(db.Model):
    __tablename__='patients'

    id:Mapped[int]=mapped_column(BigInteger(),primary_key=True,nullable=False)
    phone:Mapped[str]=mapped_column(String(20),nullable=False)
    birth_date:Mapped[Date]=mapped_column(Date,nullable=True)
    address:Mapped[str]=mapped_column(String(255),nullable=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"), nullable=False)

    user:Mapped["User"]=relationship(back_populates="patient")
    appointment:Mapped["Appointment"]=relationship(back_populates="patient")
    

    def _dict(self):
            return{
                "id":self.id,
                "phone":self.phone,
                "birth_date":str(self.birth_date),
                "address":self.address
            }

