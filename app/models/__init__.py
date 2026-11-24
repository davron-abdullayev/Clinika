
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


db=SQLAlchemy()
migrate=Migrate()
bcypt=Bcrypt()
jwt=JWTManager()

from .user import User
from .doctor import Doctor
from .patient import Patient
from .schedule import Schedule
from .appointment import Appointment


