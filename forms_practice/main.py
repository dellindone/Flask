from flask import Flask, render_template
from models.user import init_db
from routes.auth import auth_bp
from routes.register_routes import register_bp
from routes.dashboard import dashboard_bp
from routes.home import home_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://aditya:root@localhost/aditya'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'DX0fSItYzrpHitFWVJsUC6YUSf836ZIY'
init_db(app)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True)