from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from application import db
from application.users.forms import EditProfileForm, ForgotPasswordForm, ResetPasswordForm
from application.users.models import User

users = Blueprint('users', __name__)

@users.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()

    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        if form.username.data != user.username:
            user.username = form.username.data
        user.fullname = form.fullname.data
        user.bio = form.bio.data


        if form.profile_pic.data:
            pass


        db.session.commit()
        flash("profile updated", 'success')
        return redirect(url_for('project.profile', username=current_user.username))
        
    form.username.data = current_user.username
    form.fullname.data = current_user.fullname
    form.bio.data = current_user.bio

    return render_template('edit.html', title="Edit {current_user.username} Profile", form=form)

@users.route('/forgotPass', methods=['GET', 'POST'])
def forgotPass():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        email = User.query.filter_by(email=email)
    return render_template('forgotpass.html', title='Forgot Password', form=form)

@users.route('/respass', methods=['GET', 'POST'])
@login_required
def respass():
    form = ResetPasswordForm()

    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        if user.password != form.old_password.data:
            flash("ur old password is wrong", "error")
            return redirect(url_for("users.respass"))
        user.password = form.new_password.data
        user.password_Confirm = form.confirm_new_password.data

        if form.old_password.data == form.new_password.data:
            flash("ur password is the same as the old one", "error")
            return redirect(url_for("users.respass"))

        db.session.commit()
        flash("password has been reset", 'success')
        return redirect(url_for('project.profile', username=current_user.username))
    
    return render_template('resetpass.html', title='ResetPassword', form=form)
