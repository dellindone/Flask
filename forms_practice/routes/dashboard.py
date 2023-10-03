from flask import Blueprint, render_template, request, redirect,  url_for, session
from models.user import Users, db

dashboard_bp = Blueprint('dashboard', __name__, url_prefix = '/dashboard')

@dashboard_bp.route('/dashboard')
def dashboard():
    if session['email']:
        user = Users.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    return redirect('/api/login')