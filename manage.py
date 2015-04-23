import os
from flask.ext.script import Manager
from dejavu import Dejavu
import warnings
import json
warnings.filterwarnings("ignore")

from clunkr import app

from clunkr import djv


manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)


@manager.command
def fingerprint():
    with open("database.cnf") as f:
        config = json.load(f)

	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("mp3", [".mp3"])
    return print "Finished fingerprinting files."


if __name__ == "__main__":
    manager.run()