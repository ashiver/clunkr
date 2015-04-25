from flask import render_template, request, redirect, url_for, flash
from clunkr import app, djv
from dejavu.recognize import FileRecognizer
from werkzeug import secure_filename

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET'])
def record():
    return render_template("record.html")


@app.route("/", methods=['POST'])
def upload():
    file = request.files['file'] # sample must be mp3
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # for debugging purposes, to see whether file is uploaded or not
    recognizer = FileRecognizer(djv)
    match = recognizer.recognize_file(file) # recognizer returns filename
    flash("Uploading and looking for a match.", "info")
    os.popen("rm -f ~/root/recordings") # deletes file after match is made
    return render_template("result.html",
                          match=match
                          )




