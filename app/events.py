"""
Flask Blueprint for handling events on the SocketIO stream.
@author Brian Wojtczak
"""

import functools
import logging
import time

from flask import request
from flask_socketio import emit, ConnectionRefusedError, disconnect

from .auth import is_logged_in
from .io_blueprint import IOBlueprint

logger = logging.getLogger(__name__)
bp = IOBlueprint('events', __name__)


def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not is_logged_in():
            disconnect()
        else:
            return f(*args, **kwargs)

    return wrapped


@bp.on('connect')
def connect():
    if not is_logged_in():
        raise ConnectionRefusedError('unauthorized!')
    emit('flash', 'Welcome ')  # context aware emit


@bp.on('echo')
def on_alive(data):
    logger.debug(data)
    emit('echo', data)  # context aware emit


@bp.on('broadcast')
@authenticated_only
def on_broadcast(data):
    logger.debug(data)
    bp.emit('broadcast', data)  # bp.emit same as socketio.emit
    
    
@bp.on('ping')
def on_ping(data):
    logger.debug(data)
    bp.emit('pong', {"time": time.time()})  # bp.emit same as socketio.emit