# -*- coding: utf-8 -*-
from flask import (Blueprint, render_template, url_for, redirect)
from flask_login import login_required, logout_user, current_user
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer

from web.extensions import mail
from web.forms.user import PasswordForm, EmailForm, UsernameForm
from web.models.user import User
from web.utils import flash_errors, render_extensions

blueprint = Blueprint("user", __name__, url_prefix='/users',
                      static_folder="../static")


@blueprint.route("/")
@login_required
def profile():
    return render_extensions("users/profile.html")

@blueprint.route('/reset', methods=["GET", "POST"])
def reset():
    form = EmailForm()
    if form.validate_on_submit():
        emailuser = User.query.filter_by(email=form.email.data).first_or_404()

        subject = "Password reset requested"
        from common.settings import Config

        ts = URLSafeTimedSerializer(Config.SECRET_KEY)
        token = ts.dumps(emailuser.email, salt='recover-key')

        recover_url = url_for('user.reset_with_token', token=token, _external=True)
        html = render_template('email/recover.html', recover_url=recover_url)

        msg = Message(html=html, recipients=[emailuser.email], subject=subject)
        mail.send(msg)

        return redirect(url_for('public.home'))
    else:
        flash_errors(form)

    return render_extensions('users/reset.html', resetform=form)

@blueprint.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
    try:
        from common.settings import Config

        ts = URLSafeTimedSerializer(Config.SECRET_KEY)
        email = ts.loads(token, salt="recover-key", max_age=86400)
    except:
        return render_template("404.html")

    form = PasswordForm()

    if form.validate_on_submit():
        emailuser = User.query.filter_by(email=email).first_or_404()
        emailuser.set_password(form.password.data)
        emailuser.save()
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)

    return render_extensions('users/reset_with_token.html', resetform=form, token=token)


@blueprint.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = PasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        current_user.save()
        return redirect(url_for('user.profile'))
    else:
        flash_errors(form)

    return render_extensions('users/change_password.html', resetform=form)


@blueprint.route('/change_username', methods=['GET', 'POST'])
@login_required
def change_username():
    form = UsernameForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.save()
        return redirect(url_for('user.profile'))
    else:
        flash_errors(form)

    return render_extensions('users/change_username.html', resetform=form)

@blueprint.route('/unsubscribe')
@login_required
def unsubscribe():
    return render_extensions('users/unsubscribe.html')


@blueprint.route('/unsubscribe_confirm')
@login_required
def unsubscribe_confirm():
    user = current_user
    user.username = '%s (Unsubscribed)' % (user.username,)
    user.email = '%s (Unsubscribed)' % (user.email,)
    user.is_admin = False
    user.active = False
    user.save()
    logout_user()
    return redirect(url_for('public.home'))
