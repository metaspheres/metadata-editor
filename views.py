from main import app
from flask import render_template, request, redirect, url_for
from models import *


@app.route("/")

def homepage():
    library = get_library("C:/Users/anagr/Music")
    return render_template("homepage.html", data=library)

@app.route("/edit", methods=["GET", "POST"])

def edit():
    path = request.args.get('path')
    song_data = read_metadata(path)

    return render_template("edit.html", song=song_data)

@app.route("/save", methods=["POST"])

def save():
    path = request.form.get('path')
    artist = request.form.get('artist')
    title = request.form.get('title')
    album = request.form.get('album')
    tracknumber = request.form.get('track-number')
    date = request.form.get('date')


    file = File(path)

    file['artist'] = [artist]
    file['title'] = [title]
    file['album'] = [album]
    file['tracknumber'] = [tracknumber]
    file['date'] = [date]

    file.save()

    return redirect(url_for("homepage"))