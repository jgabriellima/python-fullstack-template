
import os
from os.path import join, dirname
import sys
import threading
import webview
import platform
from time import time, sleep
import uuid
import subprocess
import asyncio
from app.desktop.desktop import Desktop
import click
from app.utils import find_port

# Platforms
WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")

# Settings
MAC = (platform.system() == "Darwin")
PROD = "production"
DEV = "development"
window = None
TITLE = 'OBTurbo - Catálogo'
URL = None
port = None


def call_after_load_app(window):
    window.toggle_fullscreen()
    window.evaluate_js('alert("Nice one brother")')

@click.command()
@click.option('--mode', default="production", help='Choose between production and development')
@click.option('--web_mode', default="True", help='Defaut: True | If true will not load desktop version', type=bool)
def run(mode="production", web_mode=True):
    print(f"mode: {mode} only_server:")
    port = find_port()
    from app.start_server import start, start_web_client
    start(environment=mode, port=port, is_async=True)
    sleep(3)
    if not web_mode:
        settings = {
            "background_color": '#333333',
            "width": 200, "height": 500,
            "confirm_close": False,
            "resizable": True,
            "frameless": False,
            "easy_drag": False,
            "on_top": True
        }
        def load(window):
            print("window::load", window)
            pass
        # window = Desktop.Instance().new_window(title=TITLE, app=get_app(), settings=settings)
        from app.start_server import get_app
        app = get_app()
        window = webview.create_window(TITLE, app, **settings)
        webview.start(load, window)
    else:
        start_web_client()
    # # update dotenv
    
    # if mode == PROD:
    #     URL = 
    # else:
    #     # from pynpm import NPMPackage
    #     # pkg = NPMPackage('./client/package.json').run_script('serve', '--',f"--port={str(port+1)}" )
    #     URL = f"http://{host}:{str(port+1)}"
    #     print(URL)
    
    # if mode == PROD:

    #     print(settings)
    #     window = webview.create_window(**settings)
    #     webview.start(call_after_load_app, gui="cef", debug=True, http_server=False)


if __name__ == '__main__':
    """
    Catalogo - OBTurbo
    """
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
