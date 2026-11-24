from flask import Flask 
from flask_restful import Api 
from .routes import register_bp
import logging
from logging.handlers import RotatingFileHandler
from app.routes.auth import auth_bp
from app.resources.main import UserCreateResource,UserResource
from app.resources.doctor import DoctorCreateResource,DoctorResource
from app.resources.patient import PatientCreateResource,PatientResource
from app.resources.schedule import ScheduleCreateResource,ScheduleResource
from app.resources.appointment import AppointmentCreateResource,AppointmentResource
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required


def get_error(message,result,status_code):
    return{"message":message,"result":result,"status_code":status_code}









from .models import db,bcrypt,migrate,jwt
def create_app():
    app=Flask(__name__)

    file_handler=RotatingFileHandler("main.log")
    file_handler.setLevel(logging.INFO)


    formatter=logging.Formatter(
        "%(asctime)s- %(levelname)s-%(message)s",datefmt="%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)


    @app.errorhandler(404)
    def error_404(error):
        return get_error("Page not found",None,404)

    api=Api(app)

    


    app.config['SECRET_KEY']='jdjhgjchmdsbxjmchb'

    app.config['SQLALCHEMY_DATABASE_URI']=(
    "postgresql://postgres:davron5021@localhost:5432/flask_clinika")

    app.config["WTF_CSRF_SECRET_KEY"]='yugduyejwdhgvhdwjsghvajhb'

    app.config["JWT_ACCESS_TOKEN_EXPIRES"]=7200 


    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app,db)
   


    register_bp(app)

    return app
