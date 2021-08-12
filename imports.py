
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,LoginManager, login_required, current_user, login_user, logout_user
import datetime
from werkzeug.exceptions import HTTPException
from werkzeug.security import generate_password_hash, check_password_hash
import geopy
from geopy.geocoders import Yandex
# geolocator = Yandex(user_agent="jurody_some", api_key='052b91fc-68f2-4f88-a083-d671560734ff')
# location = geolocator.reverse("41.367727, 69.309874")
# print(location.raw['metaDataProperty']['GeocoderMetaData']['Address']['country_code'])