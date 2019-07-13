from flask import Flask, render_template, url_for, abort, request, redirect
from dyslexia import *

app = Flask(__name__)

@app.route('/404')
@app.errorhandler(404)
def page_note_found(e=None):
    return render_template('404.html'), 404

@app.route('/')
def hello_world():
    return "Hello, world"

@app.route('/test')
def test():
    preLine = "I got green eggs"
    currLine = "and Ham sam!"
    postLine = "this is postline!"
    return render_template('test.html', preLine = preLine, currLine = currLine, postLine = postLine)


@app.route('/lineByLine', methods=["GET","POST"])
def lineByLine():

    if request.method=="POST":  # If post request i.e. client clicks
        clientSaid = Record(data)
        return render_template('lineByLine.html', textSaid = clientSaid)

    # OTHERWISE
    fileName = getFile()
    with open(fileName, 'r') as file:
        data = file.read()
        dataLower = data.lower()
    return render_template('lineByLine.html', textSaid="", textToRead = data)
