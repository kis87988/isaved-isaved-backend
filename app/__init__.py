from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + config.database_user + ':' + config.database_passwd +'@' + config.database_host + ":" + str(config.database_port) + "/" + config.database_db

db = SQLAlchemy(app)

import account
import authorization
import search
import social
import tag
import visualization
import database
import display