# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash, render_template, current_app

def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                  .format(getattr(form, field).label.text, error), category)


def render_extensions(template_path, **kwargs):
    """
    Wraps around the standard render template method and shoves in some other stuff out of the config.

    :param template_path:
    :param kwargs:
    :return:
    """

    return render_template(template_path,
                           _GOOGLE_ANALYTICS=current_app.config['GOOGLE_ANALYTICS'],
                           **kwargs)

