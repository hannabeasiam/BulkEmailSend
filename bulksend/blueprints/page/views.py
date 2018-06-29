from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/login')
def login():
    return render_template('page/login.html')


@page.route('/register')
def register():
    return render_template('page/register.html')