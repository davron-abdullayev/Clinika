from flask import Blueprint,request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.doctorsxm import DoctorCreateSchemas,DoctorUpdateSchemas
from app.models.doctor import Doctor
from app.models import db
from pydantic import BaseModel,Field
from app.routes.decorators import rol_required
from flask_bcrypt import generate_password_hash,check_password_hash


doctor_bp=Blueprint('doctors',__name__,url_prefix='/doctors')

class DoctorResource(Resource):

    def get(self,doctor_id):
        doctor=Doctor.query.filter_by(id=doctor_id).first()
        if doctor is None:
            return {"message":"Bunday idli doctor mavjud emas"},404
        return {
            "doctors":[{
                "id":doctor.id,
                "specialty":doctor.specialty,
                "room":doctor.room,
                "experience_years":doctor.experience_years,
                "bio":doctor.bio
                }]
                },200


    def delete(self,doctor_id):
            doctor=Doctor.query.filter_by(id=doctor_id).first()
            if doctor is None:
                return {"message":"Bunday idli doctor mavjud emas"},404
            db.session.delete(doctor)
            db.session.commit()
            return {"message":"Doctor muvaffaqiyatli uchirildi"},200
    
    def patch(self,doctor_id):
        try:
            data=DoctorUpdateSchemas.model_validate(request.get_json())
            
            doctor=Doctor.query.filter_by(id=doctor_id).first()
            if doctor is None:
                return {"message":"Bunday idli doctor mavjud emas"},404
            if data.specialty is not None:
                doctor.specialty=data.specialty
            if data.room is not None:
                doctor.room=data.room
            if data.experience_yaers is not None:
                doctor.experience_yaers=data.experience_yaers
            if data.bio is not None:
                doctor.bio=data.bio
            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        return {"message":"Doctor muvaffaqiyatli yangilandi","doctor":doctor._dict()},200


    def put(self,doctor_id):
        try:
            data=DoctorUpdateSchemas.model_validate(request.get_json())
            
            doctor=Doctor.query.filter_by(id=doctor_id).first()
            if doctor is None:
                return {"message":"Bunday idli doctor mavjud emas"},404
            
            doctor.specialty=data.specialty
            doctor.room=data.room
            doctor.experience_years=data.experience_years
            doctor.bio=data.bio

            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        
        return {"message":"Doctor muvaffaqiyatli tuliq yangilandi","doctor":doctor._dict()},200

class DoctorCreateResource(Resource):
    @rol_required(['admin'])

    def get(self):
        doctors=Doctor.query.all()
        return({
            "doctors":[doctor._dict() for doctor in doctors]},200)

    @rol_required(['admin'])
    def post(self):
        try:
            data=DoctorCreateSchemas.model_validate(request.get_json())
            new_doctor=Doctor(
                specialty=data.specialty,
                room=data.room,
                experience_years=data.experience_years,
                bio=data.bio)

            db.session.add(new_doctor)
            db.session.commit()
        except ValidationError as e:
            return {"errors":e.errors(include_url=False)}
        return{"message":"Doctor muvaffaqiyatli yaratildi","doctor":new_doctor._dict()},201