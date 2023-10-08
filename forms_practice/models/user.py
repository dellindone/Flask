from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import bcrypt

db = SQLAlchemy()

def init_db(app):
    try:
        db.init_app(app)
        with app.app_context():
            db.create_all()
    except OperationalError as e:
    # Attempt to reconnect to the database and retry the operation
        db.session.rollback()
        db.session.close()
        db.engine.dispose()  # Dispose of the current database engine
        db.create_all()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
