from flask import Flask

from .config import configs
from .api import register_blueprints


def create_app(config_name: str = 'development') -> Flask:
    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    register_blueprints(app)
    return app
