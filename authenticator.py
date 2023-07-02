from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import User
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///instance/database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

users = []

def hash_password(password):
    return password

@app.route('/')
def home():
    return "Welcome to our authentication application."

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        errors = []
        if not username:
            errors.append('Username is required.')
        if not email:
            errors.append('Email is required.')
        if not password:
            errors.append('Password is required.')
        
        if errors:
            return render_template('register.html', errors=errors)
        
        hashed_password = hash_password(password)
        
        users.append({'username': username, 'email': email, 'password': hashed_password})
        
        return "Registration successful!"
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = next((user for user in users if user['username'] == username), None)
        
        if user and hash_password(password) == user['password']:
            return "Login successful!"
        else:
            return render_template('login.html', error="Invalid username or password.")
    
    return render_template('login.html')

if __name__ == '__main__':
    connection_string = os.environ.get('DATABASE_CONNECTION_STRING')
    app.run(host='0.0.0.0', port=5000, debug=True)
