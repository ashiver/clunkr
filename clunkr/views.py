import os
from flask import render_template, request, redirect, url_for, flash
from clunkr import app, djv
from dejavu.recognize import FileRecognizer
from werkzeug import secure_filename
import subprocess

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET'])
def record():
    return render_template("record.html")


@app.route("/", methods=['POST'])
def upload():
    subprocess.call("php ~/root/clunkr/static/upload.php") # runs the php upload script
    directory_list = os.listdir("~/root/recordings") # grabs the files from the recording directory
    file_name = directory_list.pop # pulls filename of the most recent recording from recordings
    recognizer = FileRecognizer(djv)
    match = ""
    with open("~/root/recordings" + file_name) as f: # opens file as f
        match = recognizer.recognize_file(f) # recognizer returns filename
    flash("Uploading and looking for a match.", "info")
    os.popen("rm -f ~/root/recordings") # deletes file after match is made
    return render_template("result.html",
                          match=match
                          )




