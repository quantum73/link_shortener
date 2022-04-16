import os
import uuid

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', uuid.uuid4())
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = os.environ.get('HOST', '127.0.0.1')
    PORT = os.environ.get('PORT', 5000)

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL',
        f"sqlite:///{os.path.join(basedir, 'data_dev.sqlite')}"
    )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL',
        f"sqlite:///{os.path.join(basedir, 'data_test.sqlite')}"
    )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f"sqlite:///{os.path.join(basedir, 'data_prod.sqlite')}"
    )


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
