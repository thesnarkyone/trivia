from flask import Flask, url_for;
from app import app;

# Server /
@app.route('/')
def hello():
    createLink = "<a href='" + url_for('create') + "'>Create a Question</a>";
    return """<html>
                    <head>
                        <title>Hello, World!</title>
                    </head>
                    <body>
                      """ + createLink + """ 
                    </body>
                </html>""";


# server/create
@app.route('/create')
def create():
    return "<h2>This is the create page!</h2>";


# server/question/<title>
@app.route('/question/<title>')
def question(title):
    return '<h2>' + title + '</h2>';