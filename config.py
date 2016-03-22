import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """docstring for Config"""
    SECRET_KEY = 'hello world'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <jin.huang@anytum.com>'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = "jin.huang@anytum.com"
    MAIL_PASSWORD = "huangjin0912"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """docstring for DevelopmentCongig"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductConfig(object):
    """docstring for Producrt"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig
}


