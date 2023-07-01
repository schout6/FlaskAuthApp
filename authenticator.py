from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Dummy in-memory storage for demonstration purposes
users = []

# Helper function for password hashing
def hash_password(password):
    # Implement your preferred password hashing algorithm here
    # For example, you can use the bcrypt library: bcrypt.hashpw(password, bcrypt.gensalt())
    return password

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Perform form validation
        errors = []
        if not username:
            errors.append('Username is required.')
        if not email:
            errors.append('Email is required.')
        if not password:
            errors.append('Password is required.')
        
        # Perform additional form validation (e.g., password strength, email format)
        # Add appropriate error messages to the 'errors' list
        
        if errors:
            return render_template('register.html', errors=errors)
        
        # Hash the password before storing it
        hashed_password = hash_password(password)
        
        # Save user data to the in-memory storage
        users.append({'username': username, 'email': email, 'password': hashed_password})
        
        return "Registration successful!"
    
    # If it's a GET request, render the registration form
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        
        # Find the user in the in-memory storage
        user = next((user for user in users if user['username'] == username), None)
        
        # Check if the user exists and validate the password
        if user and hash_password(password) == user['password']:
            return "Login successful!"
        else:
            return render_template('login.html', error="Invalid username or password.")
    
    # If it's a GET request, render the login form
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

