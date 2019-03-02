# default config
import os
import psycopg2

class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "laugh_god_damnit"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	#SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/laugh_tracker'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False
