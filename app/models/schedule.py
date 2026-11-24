from sqlalchemy import BigInteger,Boolean, ForeignKey, Integer,String, Text, Time
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime
from sqlalchemy import DateTime
from enum import Enum
from sqlalchemy import Enum as SQLEnum

from . import db


class Schedule(db.Model):
    __tablename__='schedules'

    id:Mapped[int]=mapped_column(BigInteger(),primary_key=True,nullable=False)
    weekday:Mapped[int]=mapped_column(Integer(),nullable=False)
    start_time:Mapped[Time]=mapped_column(Time)
    end_time:Mapped[Time]=mapped_column(Time)
    slot_minutes:Mapped[int]=mapped_column(Integer(),default=30)
    is_active:Mapped[bool]=mapped_column(Boolean(),default=True)
    doctor_id:Mapped[int]=mapped_column(ForeignKey("doctors.id"), nullable=False)

    doctor:Mapped["Doctor"]=relationship(back_populates="schedules")

    def _dict(self):
            return{
                "id":self.id,
                "weekday":self.weekday,
                "start_time":str(self.start_time),
                "end_time":str(self.end_time),
                "slot_minutes":self.slot_minutes
            }
