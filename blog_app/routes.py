from flask import render_template,url_for,flash,redirect,request
from blog_app.forms import RegistrationForm, LoginForm
from blog_app import app,db,bcrypt
from blog_app.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required


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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has been created {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'register', form = form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password , form.password.data):
            login_user (user,remember=form.Remember.data)
            next_page = request.args.get('next')
            return redirect('next_page')if next_page else redirect(url_for('home'))
        else:
            flash('login failed, check your email and password', 'danger')
    return render_template('login.html', title = 'login', form = form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html',title = 'Account')