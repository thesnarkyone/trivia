from flask import Flask, url_for, request, render_template;
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
    if request.method == 'GET':
        #send the user the form
        return render_template('createquestion.html');
    elif request.method =='POST':
        #read for data and save it
        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];
    #store this in the database
        return render_template('createdquestion.html',question=question);
  
    else: 
        return "<h2>Invalid request</h2>";


# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        #send the user the form

        question = 'Question here.';
        #read question from the data store
        return render_template('answerquestion.html', question = question);

    elif request.method == 'POST':
        #User has submitted Question
        submittedanswer - request.form['submittedanswer'];

        #read answer from form
        answer = 'answer';

        if submittedanswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('incorrect.html', submittedanswer = submittedanswer, answer = answer);

    else:

        return '<h2>Invalid Request</h2>';