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
def quiz():
    
    return render_template('quiz.html')
    
@app.route('/Redo')
def Redo():
    return redirect(url_for('home'))
    
@app.route('/E')
def end():
    session.clear()
    return render_template('end.html')
    
@app.route('/P2', methods=['GET', 'POST'])
def page2():
    
    return render_template('page2.html')
    
@app.route('/P3', methods=['GET', 'POST'])
def page3():
  
    return render_template('page3.html')    
    
@app.route('/P4', methods=['GET','POST'])
def page4():
    return render_template('page4.html')
    
@app.route('/P5', methods=['GET','POST'])
def page5():
    return render_template('page5.html')    

if __name__ == '__main__':
    app.run(debug=True) # change to False when running in producti