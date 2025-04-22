
class Config:
    SECRET_KEY = 'merosmeros123'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD='123'
    MYSQL_DB = 'flask'


config = {
    'development': DevelopmentConfig
}