import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from logic.extensions import db, ma
from logic.routes import products_bp   # import your Blueprint
from flask_migrate import Migrate
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Load environment variables
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")  
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///farmers_inventory.db")

    # Config
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    ma.init_app(app)

    # Register blueprints
    app.register_blueprint(products_bp, url_prefix="/api")

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
# Expose the app for Gunicorn
app = create_app()
