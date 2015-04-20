import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
"""
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer
import warnings
import json
warnings.filterwarnings("ignore")
"""

from clunkr import app


manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

"""
@manager.command
def fingerprint():
    with open("database.cnf") as f:
        config = json.load(f)
        
    djv = Dejavu(config)

	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("mp3", [".mp3"])
    return print "Finished fingerprinting files."

    
class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata
        
migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)
"""

if __name__ == "__main__":
    manager.run()