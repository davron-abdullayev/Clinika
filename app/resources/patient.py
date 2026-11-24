from flask import Blueprint,request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.patientsm import PatientCreateSchemas,PatientUpdateSchemas
from app.models.patient import Patient
from app.models import db
from pydantic import BaseModel,Field
from app.routes.decorators import rol_required
from flask_bcrypt import generate_password_hash,check_password_hash

patient_bp=Blueprint('patients',__name__,url_prefix='/patients')

class PatientResource(Resource):

    def get(self,patient_id):
        patient=Patient.query.filter_by(id=patient_id).first()
        if patient is None:
            return {"message":"Bunday idli patient mavjud emas"},404
        return {
            "patients":[{
                "id":patient.id,
                "phone":patient.phone,
                "birth_date":patient.birth_date,
                "address":patient.address
                }]
                },200

    def delete(self,patient_id):
        patient=Patient.query.filter_by(id=patient_id).first()
        if patient is None:
            return {"message":"Bunday idli patient mavjud emas"},404
        db.session.delete(patient)
        db.session.commit()
        return {"message":"Patient muvaffaqiyatli uchirildi"},200

    def patch(self,patient_id):
        try:
            data=PatientUpdateSchemas.model_validate(request.get_json())
            
            patient=Patient.query.filter_by(id=patient_id).first()
            if patient is None:
                return {"message":"Bunday idli patient mavjud emas"},404
            if data.phone is not None:
                patient.full_name=data.phone
            if data.birth_date is not None:
                patient.birth_date=data.birth_date
            if data.address is not None:
                patient.address=data.address
            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        return {"message":"Patient muvaffaqiyatli yangilandi","patient":patient._dict()},200


    def put(self,patient_id):
        try:
            data=PatientUpdateSchemas.model_validate(request.get_json())
            
            patient=Patient.query.filter_by(id=patient_id).first()
            if patient is None:
                return {"message":"Bunday idli patient mavjud emas"},404
            
            patient.full_name=data.phone
            
            patient.birth_date=data.birth_date
            
            patient.address=data.address

            db.session.commit()
        except ValidationError as e:
            return{"errors":e.errors(include_url=False)}
        
        return {"message":"Patient muvaffaqiyatli tuliq yangilandi","patient":patient._dict()},200

class PatientCreateResource(Resource):
    @rol_required(['admin'])

    def get(self):
        patients=Patient.query.all()
        return({
            "patients":[patient._dict() for patient in patients]},200)

    @rol_required(['admin'])
    def post(self):
        try:
            data=PatientCreateSchemas.model_validate(request.get_json())
            new_patient=Patient(
                phone=data.phone,
                birth_date=data.birth_date,
                address=data.address)

            db.session.add(new_patient)
            db.session.commit()
        except ValidationError as e:
            return {"errors":e.errors(include_url=False)}
        return{"message":"Patient muvaffaqiyatli yaratildi","user":new_patient._dict()},201
