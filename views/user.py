import hashlib

from flask import (
    Blueprint, request, session
)

from models import db, User

user_blueprint = Blueprint('User', __name__, url_prefix='/user')


@user_blueprint.route("/")
def UserIndex():
    if session.get('username') is not None:
        return {"status": 200, "data": session.get('username')}
    else:
        return {"status": 403}


@user_blueprint.route('/create', methods=['GET', 'POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    password = hashlib.md5(str(password).encode("utf8")).hexdigest()
    m = User(username=username, password=password)
    db.session.add(m)
    db.session.commit()
    return {"status": 200}


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    password = hashlib.md5(str(password).encode("utf8")).hexdigest()
    user = User.query.filter_by(username=username, password=password).first()
    if user is not None:
        session['username'] = username
        return {"status": 200}
    return {"status": 403}


@user_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('username') is not None:
        session.pop('username')
    return {'status': 200}


@user_blueprint.route('/update', methods=['GET', 'POST'])
def update():
    username = request.form['username']
    password = request.form['password']
    reset = request.form['reset']
    password = hashlib.md5(str(password).encode("utf8")).hexdigest()
    reset = hashlib.md5(str(reset).encode("utf8")).hexdigest()
    user = User.query.filter_by(username=username, password=password).first()
    if user is not None:
        user.password = reset
        db.session.commit()
        return {"status": 200}
    else:
        return {"status": 403}
