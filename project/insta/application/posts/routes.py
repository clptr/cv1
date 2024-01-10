from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from application import db
from application.posts.models import Post


posts = Blueprint('posts', __name__)

@posts.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    form = EditPostForm()

    post = Post.query.get(post_id)
    if form.validate_on_submit():
        post.caption = form.caption.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('index', username=current_user.username))

    elif request.method == 'GET':
        form.caption.data = post.caption

    return render_template('edit_post.html', title='Edit Post', form=form, post=post)
