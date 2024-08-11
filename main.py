import secrets
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = secrets.token_hex(16)  # Change this to a random secret key

# Connect to MongoDB
client = MongoClient('mongodb+srv://finance:finance123@finance.o1wni.mongodb.net/?retryWrites=true&w=majority&appName=finance')
db = client['user_database']
users = db.users

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = users.find_one({'email': email})
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['user_id'] = str(user['_id'])
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid email or password')
    
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = users.find_one({'email': email})
        
        if existing_user:
            return render_template('register.html', error='Email already exists')
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        user_id = users.insert_one({
            'name': name,
            'email': email,
            'password': hashed_password
        }).inserted_id
        
        session['user_id'] = str(user_id)
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = users.find_one({'_id': ObjectId(session['user_id'])})
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        if 'user_id' in session:
            user_id = session['user_id']
            # Delete the user from the database
            users.delete_one({'_id': ObjectId(user_id)})
            # Clear the session
            session.clear()
        return redirect(url_for('register'))
    return render_template('logout.html')

@app.route('/income')
def income():
    # Add logic for income page
    return render_template('income.html')

@app.route('/update_form')
def update_form():
    # Add logic for update form
    return render_template('form.html')

@app.route('/recommendations')
def recommendations():
    # Add logic for recommendations page
    return render_template('recommendations.html')

@app.route('/savings')
def savings():
    # Add logic for savings page
    return render_template('savings.html')

if __name__ == '__main__':
    app.run(debug=True)

