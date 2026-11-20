from sqlalchemy import BigInteger,Boolean, Date, Integer,String, Text
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
    user_id:Mapped["User"]=relationship(back_populates="patients")

    def _dict(self):
            return{
                "id":self.id,
                "phone":self.phone,
                "birth_date":self.birth_date,
                "address":self.address
            }

