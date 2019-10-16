from cost.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)

from cost import routes


