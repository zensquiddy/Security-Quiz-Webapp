from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/Q')
def quiz():
    return render_template('quiz.html')
    
@app.route('/E')
def end():
    return render_temaple('end.html')


if __name__ == '__main__':
    app.run(debug=True) # change to False when running in producti