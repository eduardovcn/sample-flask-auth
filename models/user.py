from database import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    #id (int), username (str), email (text), password (text)
    id = db.Column(db.Integer, primary_key=True)#essa é a chave primaria da minha tabela de usuarios: é uma chave qque identifica os registros na tabela e é uma chave unica.
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False , default='user')