# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from logic.extensions import db, ma
# from logic.routes import products_bp   # import your Blueprint
# from flask_migrate import Migrate
# from flask_cors import CORS

# def create_app():
#     app = Flask(__name__)
#     CORS(app, resources={r"/api/*": {"origins": "*"}})

#     # Configure Database URI
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmers_inventory.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # Initialize extensions
#     db.init_app(app)
#     migrate = Migrate(app, db)
#     ma.init_app(app)

#     # Register blueprints
#     app.register_blueprint(products_bp, url_prefix="/api")  #better with a prefix

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     with app.app_context():
#         db.create_all()  # Create database tables
#     app.run(debug=True)

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from logic.extensions import db, ma
from logic.routes import products_bp
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

def create_app():
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Load settings from env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "DATABASE_URL", "sqlite:///farmers_inventory.db"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret")

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(products_bp, url_prefix="/api")

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
