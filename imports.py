
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,LoginManager, login_required, current_user, login_user, logout_user
import datetime
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash