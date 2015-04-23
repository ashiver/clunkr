import os
from flask import Flask
from dejavu import Dejavu
import json

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "clunkr.config.DevelopmentConfig")
app.config.from_object(config_path)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

with open("database.cnf") as f:
    config = json.load(f)
    
djv = Dejavu(config)

from . import views
from . import filters