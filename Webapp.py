import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)


# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
#The value should be set on the server. 
#To run locally, set in env.bat (env.sh on Macs) and include that file in gitignore so the secret key is not made public.

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/Q', methods=['GET', 'POST'])
def quiz1():
    return render_template('quiz.html')
    
@app.route('/Redo')
def Redo():
    return redirect(url_for('home'))
    
@app.route('/E', methods=['GET', 'POST'])
def end():

    if "optradio5" not in session:
        session["optradio5"] = request.form["optradio5"]
        
    points = 0

    if session["optradio1"] == "option4":
        question1 = "correct"
        points = points + 1
    else :
        question1 = "incorrect"
        points = points + 0

    if session["optradio2"] == "option3":
        question2 = "correct"
        points = points + 1
    else :
        question2 = "incorrect"
        points = points + 0    
    
    if session["optradio3"] == "option1":
        question3 = "correct"
        points = points + 1
    else :
        question3 = "incorrect"
        points = points + 0
     
    if session["optradio4"] == "option3":
        question4 = "correct"
        points = points + 1
    else :
        question4 = "incorrect"
        points = points + 0
        
    if session["optradio5"] == "option4":
        question5 = "correct"
        points = points + 1
    else :
        question5 = "incorrect"
        points = points + 0
        
    qst1 = "Question 1 is " + question1
    qst2 = "Question 1 is " + question2
    qst3 = "Question 1 is " + question3
    qst4 = "Question 1 is " + question4
    qst5 = "Question 1 is " + question5
        
    score = str(points) + "/5"
    session.clear()
    return render_template('end.html', Result=score,answer1=qst1, answer2=qst2, answer3=qst3, answer4=qst4, answer5=qst5)
    
@app.route('/P2', methods=['GET', 'POST'])
def page2():
    if "optradio1" not in session:
        session["optradio1"] = request.form["optradio1"]
    return render_template('page2.html')
    
@app.route('/P3', methods=['GET', 'POST'])
def page3():
    if "optradio2" not in session:
        session["optradio2"] = request.form["optradio2"]
    return render_template('page3.html')    
    
@app.route('/P4', methods=['GET','POST'])
def page4():
    if "optradio3" not in session:
        session["optradio3"] = request.form["optradio3"]
    return render_template('page4.html')
    
@app.route('/P5', methods=['GET','POST'])
def page5():
    if "optradio4" not in session:
        session["optradio4"] = request.form["optradio4"]
    return render_template('page5.html')    

if __name__ == '__main__':
    app.run(debug=True) # change to False when running in producti