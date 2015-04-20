from flask import render_template, request, redirect, url_for, flash
from clunkr import app


@app.route("/")
def record():
    return render_template("record.html")




