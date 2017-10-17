import markdown
from flask import Markup

from web.models.post import Post
from web.models.tag import Tag


def get_post_detail(pk):
    """
    Returns the details of one specific post

    :param pk:
    :return:
    """

    post = Post.query.filter_by(id=int(pk)).first()

    if post.users is not None:
        author = post.users.first_name + ' ' + post.users.last_name
    else:
        author = ''

    post_blob = {
        'id': post.id,
        'title': post.title,
        'author': author,
        'date': post.created_at.strftime('%Y-%m-%d at %H:%M'),
        'body': Markup(markdown.markdown(post.body)),
        'tags': post.tags
    }

    return post_blob


def get_page(page_size, page_num):
    """
    Returns a page of slugs

    :param page_size:
    :param page_num:
    :return:
    """

    posts = Post.query.order_by(Post.created_at.desc()).offset(page_num * page_size).limit(page_size).all()
    posts_blob = []
    for post in posts:

        if post.users is not None:
            author = post.users.first_name + ' ' + post.users.last_name
        else:
            author = ''

        posts_blob.append({
            'id': post.id,
            'title': post.title,
            'author': author,
            'date': post.created_at.strftime('%Y-%m-%d at %H:%M'),
            'slug': Markup(markdown.markdown(post.slug)),
            'tags': post.tags
        })

    return posts_blob


def get_top_tags(n):
    """
    Returns N top tags
    :param n:
    :return:
    """

    raise NotImplementedError


def get_tagged_posts(tag, limit):
    """
    Gets the most recent limit posts with a certain tag
    :param tag:
    :param limit:
    :return:
    """

    raise NotImplementedError
