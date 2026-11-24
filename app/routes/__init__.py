from flask import Flask
from .auth import auth_bp
from .base import base_bp
from ..resources.patient import patient_bp
from ..resources.doctor import doctor_bp
from ..resources.schedule import schedule_bp
from ..resources.appointment import appointment_bp

def register_bp(app:Flask):
    app.register_blueprint(auth_bp)
    app.register_blueprint(base_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(schedule_bp)
    app.register_blueprint(appointment_bp)
    


