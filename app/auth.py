"""
Dummy Flask Authentication Blueprint.
@author Brian Wojtczak
"""

import functools
import logging

from flask import Blueprint, request, session, abort

logger = logging.getLogger(__name__)
bp = Blueprint('auth', __name__)


def is_logged_in():
    return True


def login_required(view):
    """
    View decorator that sends an error to anonymous users.
    Use the error handler to provide a friendly user experience.
    """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not is_logged_in():
            abort(401)

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    pass  # Not implemented