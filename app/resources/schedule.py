from flask import Blueprint,request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.schedulesxm import ScheduleCreateSchemas,ScheduleUpdateSchemas
from app.models.schedule import Schedule
from app.models import db
from pydantic import BaseModel,Field
from app.routes.decorators import rol_required
from flask_bcrypt import generate_password_hash,check_password_hash

schedule_bp=Blueprint('schedules',__name__,url_prefix='/schedules')

class ScheduleResource(Resource):

    def get(self,schedule_id):
        schedule=Schedule.query.filter_by(id=schedule_id).first()
        if schedule is None:
            return {"message":"Bunday idli schedule mavjud emas"},404
        return {
            "schedules":[{
                "id":schedule.id,
                "weekday":schedule.weekday,
                "start_time":schedule.start_time,
                "end_time":schedule.end_time,
                "slot-minutes":schedule.slot_minutes
                }]
                },200


    def delete(self,schedule_id):
            schedule=Schedule.query.filter_by(id=schedule_id).first()
            if schedule is None:
                return {"message":"Bunday idli schedule mavjud emas"},404
            db.session.delete(schedule)
            db.session.commit()
            return {"message":"Schedule muvaffaqiyatli uchirildi"},200
    
    def patch(self,schedule_id):
        try:
            data=ScheduleUpdateSchemas.model_validate(request.get_json())
            
            schedule=Schedule.query.filter_by(id=schedule_id).first()
            if schedule is None:
                return {"message":"Bunday idli schedule mavjud emas"},404
            if data.weekday is not None:
                schedule.weekday=data.weekday
            if data.start_time is not None:
                schedule.start_time=data.start_time
            if data.end_time is not None:
                schedule.end_time=data.end_time
            if data.slot_minutes is not None:
                schedule.slot_minutes=data.slot_minutes
           
            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        return {"message":"Schedule muvaffaqiyatli yangilandi","schedule":schedule._dict()},200


    def put(self,schedule_id):
        try:
            data=ScheduleUpdateSchemas.model_validate(request.get_json())
            
            schedule=Schedule.query.filter_by(id=schedule_id).first()
            if schedule is None:
                return {"message":"Bunday idli schedule mavjud emas"},404
            
            schedule.weekday=data.weekday
            schedule.start_time=data.start_time
            schedule.end_time=data.end_time
            schedule.slot_minutes=data.slot_minutes

            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        
        return {"message":"Schedule muvaffaqiyatli tuliq yangilandi","schedule":schedule._dict()},200

class ScheduleCreateResource(Resource):
    @rol_required(['admin'])

    def get(self):
        schedules=Schedule.query.all()
        return({
            "schedules":[schedule._dict() for schedule in schedules]},200)

    @rol_required(['admin'])
    def post(self):
        try:
            data=ScheduleCreateSchemas.model_validate(request.get_json())
            new_schedule=Schedule(
                weekday=data.weekday,
                start_time=data.start_time,
                end_time=data.end_time,
                slot_minutes=data.slot_minutes)

            db.session.add(new_schedule)
            db.session.commit()
        except ValidationError as e:
            return {"errors":e.errors(include_url=False)}
        return{"message":"Schedule muvaffaqiyatli yaratildi","doctor":new_schedule._dict()},201