from flask import (
    Blueprint, request, redirect
)
from flask_sqlalchemy import sqlalchemy

from models import db, Demo

demo_blueprint = Blueprint('demo', __name__, url_prefix='/demo')


@demo_blueprint.route("/")
def demo():
    return {"status": 200, "data": str(Demo.query.all())}


@demo_blueprint.route('/add/<name>', methods=['GET', 'POST'])
def demo_add(name):
    if request.method == 'GET':
        m = Demo(name=name)
        db.session.add(m)
        db.session.commit()
        return redirect("/demo")
    return "Add false!"


@demo_blueprint.route('/delete/<name>', methods=['GET', 'POST'])
def demo_delete(name):
    Demo.query.filter(Demo.name == name).delete()
    db.session.commit()
    return redirect('/demo')


@demo_blueprint.route('/update', methods=['GET', 'POST'])
def demo_update():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        name = request.form['demo_name']
        old_name = request.form['old_demo_name']
        try:
            m = Demo.query.get(old_name)
            m.name = name
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return redirect('/demo/')
        return redirect('/demo/')


@demo_blueprint.route('/edit/<demo_name>', methods=['GET', 'POST'])
def demo_edit(demo_name):
    m = Demo.query.get(demo_name)
    return "Edit Success!"
