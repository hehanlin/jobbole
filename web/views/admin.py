# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, request

from flask_login import login_required, current_user
from web.utils import flash_errors, render_extensions
from web.models.post import Post

blueprint = Blueprint('admin', __name__, static_folder="../static")


@blueprint.route("/new_blog", methods=["GET", "POST"])
@login_required
def new_blog():
    if not current_user.is_admin:
        return render_extensions('401.html')

    if request.method == 'POST':
        try:
            content = str(request.form['content'])
        except Exception:
            content = ''

        try:
            slug = str(request.form['slug'])
        except Exception:
            slug = ''

        try:
            title = str(request.form['title'])
        except Exception:
            title = ''

        post = Post(title=title, body=content, slug=slug)
        post.save()

        current_user.posts.append(post)
        current_user.save()

    return render_extensions('admin/new_blog.html')

@blueprint.route("/edit_blog/<blog_id>/", methods=["GET", "POST"])
@login_required
def edit_blog(blog_id):
    if not current_user.is_admin:
        return render_extensions('401.html')

    if request.method == 'POST':
        try:
            content = str(request.form['content'])
        except Exception:
            content = ''

        try:
            slug = str(request.form['slug'])
        except Exception:
            slug = ''

        try:
            title = str(request.form['title'])
        except Exception:
            title = ''

        post = Post(title=title, body=content, slug=slug)
        post.save()

        current_user.posts.append(post)
        current_user.save()

    post_obj = Post.query.filter_by(id=int(blog_id)).first()
    post_content = {
        'title': str(post_obj.title),
        'slug': str(post_obj.slug),
        'body': str(post_obj.body),
    }

    return render_extensions('admin/edit_blog.html', post=post_content)
