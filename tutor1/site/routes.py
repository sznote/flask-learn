from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from functools import wraps


mod = Blueprint('site', __name__, template_folder='templates', static_folder='statics')


def login_required(f):
    @wraps(f)
    def  wrap(*args, **kwargs):
    	if 'logged_in'  in session:
    		return f(*args, **kwargs)
    	else:
    		flash('You need  to login first.')
    		return redirect(url_for('site.login'))
    return wrap

    # def decorated_function(*args, **kwargs):
    #     if g.user is None:
    #         return redirect(url_for('login', next=request.url))
    #     return f(*args, **kwargs)
    # return decorated_function



@mod.route('/')
@login_required
def home():
	return render_template('index.html')

@mod.route('/welcome')
def welcome():
	return render_template('welcome.html')

@mod.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if  request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = "Invalid credentials. Please Try again"
		else:
			session['logged_in'] =  True
			flash('You ware just loggin !!')

			return redirect(url_for('site.home'))
	# if request.method == 'POST':
	# 	username =  request.form['username']
	# 	password =  request.form['password']
	# 	return redirect( url_for('site.welcome'))
	return render_template('login.html', error=error)

@mod.route('/logout')
@login_required
def logout():
	# if 'logged_in' in session:
	session.pop('logged_in', None)
	flash('You ware just logged out !!')
	return  render_template('logout.html')

@mod.route('/homepage')
def homepage():

	return render_template('index.html')
	#return '<h1> You are on the home page !!! </h1>'
	
