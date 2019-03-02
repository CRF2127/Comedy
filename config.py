# default config
import os
import psycopg2

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "laugh_god_damnit"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False
