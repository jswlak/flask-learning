from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# Define User model/table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Home form page
@app.route('/')
def home():
    return render_template('index.html')

#About page
@app.route('/about')
def about():
    return render_template('about.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    if username:
        user = User(name=username)
        db.session.add(user)
        db.session.commit()
    return redirect('/users')

# Show all users
@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run(debug=True)


