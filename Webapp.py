from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/Q', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html')
    
@app.route('/E')
def end():
    
    return render_template('end.html')
    
@app.route('/P2')
def page2():

    return render_template('page2.html')
    
@app.route('/P3')
def page3():
  
    return render_template('page3.html')    
    
@app.route('/P4')
def page4():
    return render_template('page4.html')
    
@app.route('/P5')
def page5():
    return render_template('page5.html')    

if __name__ == '__main__':
    app.run(debug=True) # change to False when running in producti