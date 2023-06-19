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

# Add your code here
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Rest of the code...

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Rest of the code...

if __name__ == '__main__':
    app.run(debug=True)

