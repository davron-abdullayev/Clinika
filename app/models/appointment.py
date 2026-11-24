from sqlalchemy import BigInteger,Boolean, Date, ForeignKey, Integer,String, Text, Time
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from sqlalchemy import DateTime
from enum import Enum
from sqlalchemy import Enum as SQLEnum

from . import db

class UserStatus(Enum):
    PENDING="pending"
    CONFIRMED="confirmed"
    CANCELLED="cancelled"
    COMPLETED="completed"




class Appointment(db.Model):
    __tablename__='appointments'

    id:Mapped[int]=mapped_column(BigInteger(),primary_key=True,nullable=False)
    date:Mapped[Date]=mapped_column(Date,nullable=False)
    start_time:Mapped[Time]=mapped_column(Time)
    end_time:Mapped[Time]=mapped_column(Time)
    status:Mapped[UserStatus]=mapped_column(SQLEnum(UserStatus),default=UserStatus.PENDING,nullable=False)
    reason:Mapped[str]=mapped_column(String(255),nullable=True)
    doctor_note:Mapped[str]=mapped_column(Text)
    created_at:Mapped[datetime]=mapped_column(DateTime(),default=datetime.now)
    doctor_id:Mapped[int]=mapped_column(ForeignKey("doctors.id"), nullable=False)
    patient_id:Mapped[int]=mapped_column(ForeignKey("patients.id"), nullable=False)

    doctor:Mapped["Doctor"]=relationship(back_populates="appointments")
    patient:Mapped["Patient"]=relationship(back_populates="appointment")

    def _dict(self):
            return{
                "id":self.id,
                "date":self.date,
                "start_time":str(self.start_time),
                "end_time":str(self.end_time),
                "status":self.status,
                "reason":self.reason,
                "doctor_note":self.doctor_note

            }