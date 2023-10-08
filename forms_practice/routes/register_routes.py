from flask import Flask, Blueprint, render_template, request, redirect,  url_for, session
from models.user import Users, db

register_bp = Blueprint('register_routes', __name__, url_prefix='/register', template_folder='templates')

@register_bp.route('/', methods = ["POST", "GET"])
def register():
    if request.method == 'POST':
        user_name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = Users(user_name, email, password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html', error='Invalid data or user already taken')