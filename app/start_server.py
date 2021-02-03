from multiprocessing import Process
import uvicorn
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv
from io import StringIO
from os.path import join, dirname
import os
proc = None
app = None

def get_port():
    if port:
        return port
    else:
        raise Exception("Port can be not Null")
    
def get_app():
    if app:
        return app
    else:
        raise Exception("Application can be not Null")
        
def run(app, socketio, host, environment, _port): 
    """
    This function to run configured uvicorn server.
    """
    update_client_env(_port)
    socketio.run(app, port=_port)

def start_web_client():
    def run_client():
        from pynpm import NPMPackage
        pkg = NPMPackage(join(dirname(__file__), '../web/package.json')).run_script('serve')
        
    proc = Process(target=run_client, args=(), daemon=True)
    proc.start()
    proc.join()
    
    
def update_client_env(port=None):
    if port:
        # os.putenv("VUE_APP_API_PORT", port)
        # os.putenv("VUE_APP_SOCKET_PORT", port)
        # print(f"join(dirname(__file__): {join(dirname(__file__), '../web/.env')}: {stream}")
        with open(join(dirname(__file__), '../web/.env'), "w") as f:
            f.write(f"VUE_APP_API_PORT={port}\n")
            f.write(f"VUE_APP_SOCKET_PORT={port}")
        # load_dotenv(dotenv_path=join(dirname(__file__), '../web/.env'), stream=stream, override=True)

def start(host="localhost", environment='development', port=None, is_async=False):
    """
    This function to start a new process (start the server).
    """
    from . import create_app
    global proc
    global app
    app, socketio = create_app(environment=environment)
    if is_async:
        # create process instance and set the target to run function.
        # use daemon mode to stop the process whenever the program stopped.
        proc = Process(target=run, args=(app, socketio, host, environment, port), daemon=True)
        proc.start()
        # proc.join()
    else:
        run(app, socketio, host, environment, port)
    return proc

def stop(): 
    """
    This function to join (stop) the process (stop the server).
    """
    global proc
    # check if the process is not None
    if proc: 
        # join (stop) the process with a timeout setten to 0.25 seconds.
        # using timeout (the optional arg) is too important in order to
        # enforce the server to stop.
        proc.join(0.25)


def start_gevent(app_port):
    uvicorn.run(app, port=app_port,debug=True)


if __name__ == "__main__":
    start_gevent(5000)