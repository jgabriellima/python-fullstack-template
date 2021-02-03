import webview
from typing import Dict, Any
from app import Singleton
from webview.window import Window
from flask import Flask

@Singleton
class Desktop:
    windows:Dict[str, Window]
    
    def __init__(self):
        """Initialize your database connection here."""
        pass
    
    def new_window(key:str, title:str, app: Flask=None, settings:dict=None, func:any=None):
        window = webview.create_window(title, app, **settings)
        self.get_windows().update(key, window)
        return window
    def get_window(key:str):
        return self.get_windows()[key]
    
    def get_windows():
        if windows is None:
            windows = {}
    def __str__(self):
        return 'Database connection object'