
from sqlalchemy import BigInteger,Boolean,String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from sqlalchemy import DateTime
from enum import Enum
from sqlalchemy import Enum as SQLEnum

from . import db

class UserRole(Enum):
    ADMIN="admin"
    DOCTOR="doctor"
    PATIENT="patient"


class User(db.Model):
    __tablename__='users'

    id:Mapped[int]=mapped_column(BigInteger(),primary_key=True)
    full_name:Mapped[str]=mapped_column(String(100),nullable=False)
    username:Mapped[str]=mapped_column(String(100),unique=True,nullable=False)
    password:Mapped[int]=mapped_column(String(255),nullable=False)
    role:Mapped[UserRole]=mapped_column(SQLEnum(UserRole),default=UserRole.PATIENT,nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(),default=datetime.now)

    def _dict(self):
            return{
                "id":self.id,
                "full_name":self.full_name,
                "username":self.username,
                "role":self.role

            }
