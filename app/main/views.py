from flask import render_template, redirect, url_for, session
from flask.ext.login import login_required
from datetime import datetime
from . import main
from .. import db
from ..models import User
from .forms import NameForm, EditProfileForm


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
                           form=form, name=session.get('name'),
                           know=session.get('know', False))


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username)
    print user.member.since
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)
