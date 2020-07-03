from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from models.models import User, Manager, Store, Good
from db import db


homePage = Blueprint('homePage', __name__)


@homePage.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')


@homePage.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        print(remember)
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash('Please check you login deteails and try again.')
            return redirect(url_for('homePage.login_get'))
        login_user(user, remember=remember)
        return redirect(url_for('homePage.index'))


@homePage.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homePage.login_get'))

@homePage.route('/registration', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        u = User(name=name, email=email)
        u.set_password(password)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('homePage.index'))
    return render_template('registration.html')

@homePage.route('/')
@login_required
def index():
    u = Manager.query.count()
    g = Good.query.count()
    s = Store.query.count()
    return render_template('index.html', u = u, g = g, s = s)
