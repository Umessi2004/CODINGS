from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from appl.config import Config

db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from .routes import employee_bp
    app.register_blueprint(employee_bp)
    return app