from flask import render_template, redirect, url_for, session
from flask.ext.login import login_required
from datetime import datetime
from . import main
from .. import db
from ..models import User
from .forms import NameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            new_user = User(username=form.name.data)
            db.session.add(new_user)
            session['know'] = False
        else:
            session['know'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return render_template('index.html', currrent_time=datetime.utcnow(),
            form=form, name=session.get('name'), know=session.get('know', False))


@main.route('/user/<name>/', methods=['POST', 'GET'])
def user(name):
    return render_template('user.html', name=name)
