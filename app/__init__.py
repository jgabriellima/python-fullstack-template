import click
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_socketio import SocketIO, emit
from .factory import Factory

from .utils import Singleton
async_mode = "threading"

def create_app(environment='development'):
    f = Factory(environment)
    f.set_flask()
    f.set_db()
    f.set_migration()
    # f.set_api()

    from .models.base import Example

    app = f.flask
    
    if app.config['TESTING']:  # pragma: no cover
        # Setup app for testing
        @app.before_first_request
        def initialize_app():
            pass

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE')

        return response

    app.wsgi_app = ProxyFix(app.wsgi_app)

    @app.cli.command()
    @click.argument('command')
    def setup(command):
        pass
    
    socketio = SocketIO(async_mode=async_mode, cors_allowed_origins='*', logger=True, engineio_logger=True, allow_upgrades=False)
    socketio.init_app(app)

    from .views import sample_page
    from . import auth, events
    
    app.register_blueprint(sample_page, url_prefix='/')
    app.register_blueprint(events.bp, url_prefix='/ws')

    return app, socketio
