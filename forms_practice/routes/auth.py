from flask import Blueprint, render_template, request, redirect,  url_for, session
from models.user import Users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password'] 
        user = Users.query.filter_by(email = email).first()
        print(user)
        if user and Users.check_password(password):
            session['email'] = user.email
            return redirect(url_for('/dashboard'))
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('index.html')