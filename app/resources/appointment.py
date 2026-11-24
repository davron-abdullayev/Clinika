from flask import Blueprint,request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.appointmentsxm import AppointmentCreateSchemas,AppointmentUpdateSchemas
from app.models.appointment import Appointment
from app.models import db
from pydantic import BaseModel,Field
from app.routes.decorators import rol_required


appointment_bp=Blueprint('appointments',__name__,url_prefix='/appointments')

class AppointmentResource(Resource):

    def get(self,appointment_id):
        appointment=Appointment.query.filter_by(id=appointment_id).first()
        if appointment is None:
            return {"message":"Bunday idli appointment mavjud emas"},404
        return {
            "appointments":[{
                "id":appointment.id,
                "date":appointment.date,
                "start_time":appointment.start_time,
                "end_time":appointment.end_time,
                "reason":appointment.reason,
                "doctor_note":appointment.doctor_note
                }]
                },200


    def delete(self,appointment_id):
            appointment=Appointment.query.filter_by(id=appointment_id).first()
            if appointment is None:
                return {"message":"Bunday idli appointment mavjud emas"},404
            db.session.delete(appointment)
            db.session.commit()
            return {"message":"appointment muvaffaqiyatli uchirildi"},200
    
    def patch(self,appointment_id):
        try:
            data=AppointmentUpdateSchemas.model_validate(request.get_json())
            
            appointment=Appointment.query.filter_by(id=appointment_id).first()
            if appointment is None:
                return {"message":"Bunday idli appointment mavjud emas"},404
            if data.date is not None:
                appointment.date=data.date
            if data.start_time is not None:
                appointment.start_time=data.start_time
            if data.end_time is not None:
                appointment.end_time=data.end_time
            if data.reason is not None:
                appointment.reason=data.reason
            if data.doctor_note is not None:
                appointment.doctor_note=data.doctor_note
           
            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        return {"message":"Appointment muvaffaqiyatli yangilandi","appointment":appointment._dict()},200


    def put(self,appointment_id):
        try:
            data=AppointmentUpdateSchemas.model_validate(request.get_json())
            
            appointment=Appointment.query.filter_by(id=appointment_id).first()
            if appointment is None:
                return {"message":"Bunday idli appointment mavjud emas"},404
            
            appointment.date=data.date
            appointment.start_time=data.start_time
            appointment.end_time=data.end_time
            appointment.reason=data.reason
            appointment.doctor_note=data.doctor_note

            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        
        return {"message":"appointment muvaffaqiyatli tuliq yangilandi","appointment":appointment._dict()},200

class AppointmentCreateResource(Resource):
    @rol_required(['admin'])

    def get(self):
        appointments=Appointment.query.all()
        return({
            "appointment":[appointment._dict() for appointment in appointments]},200)

    @rol_required(['admin'])
    def post(self):
        try:
            data=AppointmentCreateSchemas.model_validate(request.get_json())
            new_appointment=Appointment(
                date=data.date,
                start_time=data.start_time,
                end_time=data.end_time,
                reason=data.reason,
                doctor_note=data.doctor_note
                )

            db.session.add(new_appointment)
            db.session.commit()
        except ValidationError as e:
            return {"errors":e.errors(include_url=False)}
        return{"message":"Appointment muvaffaqiyatli yaratildi","appointment":new_appointment._dict()},201