
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route("/login/<string:api_email>/<string:api_password>/<string:api_key>", methods=['GET', 'POST'])
def api_login(api_email, api_password, api_key):
  email = api_email
  password = api_password
  key = api_key

  if key == "8x7bty112(8jIj8*22@P21=+~-+1.m":
    user = User.query.filter_by(email=email).first()
    # print(f"Hash: {generate_password_hash('78xcb11565')}")
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True) 
            return redirect(url_for('views.home'))
        else:
            return "Incorrect password."
    else:
        return "Inturder"
  
  else:
    return "Incorrect or no key :("

@auth.route("/login", methods=['GET', 'POST']) 
def login():
  if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')

      user = User.query.filter_by(email=email).first()
      # print(f"Hash: {generate_password_hash('78xcb11565')}")
      if user:
          if check_password_hash(user.password, password):
              flash("Logged in successfully.", category='Success')
              login_user(user, remember=True) 
              return redirect(url_for('views.home'))
          else:
              flash("Incorrect password.", category="Error occurred")
      else:
          flash("Inturder", category="Error occurred")
  return render_template('login.html')

@auth.route("/logout")
@login_required
def logout():
  logout_user()
  flash("Logged out successfully.", category='Success')
  return redirect(url_for('auth.login'))

# @auth.route("/signup", methods=['GET', 'POST'])
# def register():
#   if request.method == 'POST':
#       name = request.form.get('name')
#       email = request.form.get('email')
#       password1 = request.form.get('password')
#       password2 = request.form.get('password2')

#       user = User.query.filter_by(email=email).first()

#       if user:
#           flash("Email is already taken. Please use a different email.", category='Error occurred')
#       elif len(email) < 4:
#           flash('Invalid email: Email must be at least 4 characters long.', category='Error occurred')
#       elif len(name) < 2:
#           flash('Invalid name: Name must be at least 2 characters long.', category='Error occurred')
#       elif password1 != password2:
#           flash('Passwords do not match. Please re-enter your password.', category='Error occurred')
#       elif len(password1) < 8:
#           flash('Password is too short. It must be at least 8 characters long.', category='Error occurred')
#       else:
#           new_user = User(email=email, name=name, password=generate_password_hash(password1))
#           db.session.add(new_user)
#           db.session.commit()
#           flash('Account created successfully.', category='Success')
#           login_user(new_user, remember=True)  # Log in the newly created user
#           return redirect(url_for('views.home'))

#   return render_template("signup.html")

    