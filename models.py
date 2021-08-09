from imports import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost:5432/refregirator'

db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sh[irjnhagodhj2384h9hn;jk'
app.config['DEBUG'] = True

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    district_id = db.Column(db.ForeignKey('district.id'), nullable=False)
    passport = db.Column(db.String, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    surname = db.Column(db.String(100), nullable=True)
    father = db.Column(db.String(100), nullable=True)
    created_time = db.Column(db.DateTime, default=datetime.datetime.now)
    login_count = db.Column(db.Integer, nullable=True)
    last_login = db.Column(db.DateTime, default=datetime.datetime.now, nullable=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500))
    role = db.Column(db.String(100), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def format(self):
        return {
            "id" : self.id,
            "username" : self.username,
            "email" : self.email,
            'role' : self.role,
            'name' : self.name,
            'surname' : self.surname,
            'father' : self.father,
            'login_count' : self.login_count,
        }

    def Get_UserType(self):
        if self.role == 'admin':
            return 'Супер Админ'
        elif self.role == 'province':
            return 'Вилоят Админи'
        return 'Фойдаланувчи'
    def getFullName(self):
        name = ""
        if self.surname is not None:
            name += str(self.surname) + " "
        if self.name is not None:
            name += str(self.name) + " "
        if self.father is not None:
            name += str(self.father)
        return name



class Province(db.Model):
    __tablename__ = 'province'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    code = db.Column(db.Integer, nullable=True)
    districts = db.relationship("District", backref="province", lazy=True)

    def format(self):
        return {
            "id" : self.id,
            "name" : self.name
        }

class District(db.Model):
    __tablename__ = 'district'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    province_id = db.Column(db.Integer, db.ForeignKey('province.id'), nullable=False)
    code = db.Column(db.Integer, nullable=True)
    users = db.relationship("User", backref="district", lazy=True)
    storages = db.relationship("Storage", backref="district", lazy=True)
    def format(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "province_id" : self.province_id
        }

    

class Storage(db.Model):
    __tablename__ = 'storage'
    id = db.Column(db.Integer, primary_key=True)
    storage_type = db.Column(db.String, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    district_id = db.Column(db.ForeignKey('district.id'), nullable=False)
    address = db.Column(db.String, nullable=False)
    organization_name = db.Column(db.String, nullable=False)
    owner_stir = db.Column(db.Integer, nullable=False)
