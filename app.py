from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from database import get_db

app = Flask(__name__)

# Home page - sagle employees dakhavel
@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', employees=employees)

# New employee add karnyasathi
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        position
