import secrets


class BaseConfig:
    SECRET_KEY = secrets.token_hex(40)
    TESTING = False


class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = False


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False


configs = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
