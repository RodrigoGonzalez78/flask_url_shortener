from flask import Flask
from config import Config
from routes.short_url_routes import short_url_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(short_url_bp, url_prefix='/')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)