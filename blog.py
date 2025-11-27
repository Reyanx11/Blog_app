from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # loading dotenv file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(40), unique = True, nullable = False)
    image_file = db.Column(db.String(30),nullable=False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = "author", lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30),nullable = False)
    content = db.Column(db.Text, nullable = False)
    date_posted = db.Column(db.DateTime , nullable = False , default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author':'reyan khan',
        'title': 'post 1',
        'content': 'first blog post',
        'posted_on':'October 12, 2025'
    },
    {
        'author':'abc',
        'title': 'post 2',
        'content': 'Demo post',
        'posted_on':'October 15, 2025'
    }
]

#routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title ='About')

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account has been created {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'register', form = form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '123':
            flash('successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('login failed, check your email and password', 'danger')
    return render_template('login.html', title = 'register', form = form)


if __name__ == "__main__":
    app.run(debug=True)