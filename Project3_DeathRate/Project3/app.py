# Project:Develop a Python Flask application for death mortality rates of world till 2017
# Program By:Ayush Pandey
# Email Id:1805290@kiit.ac.in
# DATE:19-Oct-2021
# Python Version:3.7
# CAVEATS:None
# LICENSE:None


from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# About the Dataset

# Home Page


@app.route('/')
def index():
    return render_template('Home.html')

# Graph for Country having most death and least death due to all features


@app.route('/First')
def get1():
    return render_template('First.html')

# Graph of Diiferent Factors causing Death worldwide,India and Pakistan


@app.route('/Second')
def get2():
    return render_template('Second.html')

# Regression Analysis


@app.route('/Third')
def get3():
    return render_template('Third.html')

# Conclusion


@app.route('/Forth')
def get4():
    return render_template('Forth.html')


if __name__ == "__main__":
    app.run(debug=True)
