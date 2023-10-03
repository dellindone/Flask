from flask import Blueprint, render_template, request, redirect,  url_for, session
from models.user import Users, db

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('index.html')