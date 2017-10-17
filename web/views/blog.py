# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint

from web.services.blog import get_page, get_post_detail
from web.utils import flash_errors, render_extensions

blueprint = Blueprint('blog', __name__, static_folder="../static")


@blueprint.route("/blog/<page>/", methods=["GET"])
def blog_page(page=None):
    """

    :param page:
    :return:
    """

    page = int(page)
    _page_size = 3  # TODO: move into settings

    if page is None or page <= 0:
        next_page = 0
        prev_page = 1
        current = True
    else:
        next_page = page - 1
        prev_page = page + 1
        current = False

    posts = get_page(_page_size, page)

    return render_extensions("blog/blog_page.html", posts=posts, next_page=next_page, prev_page=prev_page, current=current)


@blueprint.route("/post_detail/<pk>/", methods=["GET"])
def blog_detail(pk):
    """

    :param pk:
    :return:
    """

    post = get_post_detail(int(pk))
    return render_extensions("blog/blog_detail.html", post=post)