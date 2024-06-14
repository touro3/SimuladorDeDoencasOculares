from flask import Flask
from app.routes.simulate import simulate_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(simulate_bp, url_prefix='/api')
    return app
