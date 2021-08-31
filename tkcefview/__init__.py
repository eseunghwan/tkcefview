# -*- coding: utf-8 -*-

__author__ = "eseunghwan"
__email__ = "shlee0920@naver.com"
__version__ = "2021.09.01"

from .core import Application, BrowserWindow, BrowserAPI
__app = None


__all__ = [
    "initialize", "create_window", "start",
    "BrowserAPI"
]


def initialize(settings:dict = {}):
    """
    initialize webview environment

    :param settings: dictionary type of environment settings
    more details in "https://github.com/cztomczak/cefpython/blob/master/api/ApplicationSettings.md"
    """
    global __app
    __app = Application(settings)

def create_window(url:str, js_api:BrowserAPI = None, title:str = "tkcefview", icon:str = None, width:int = 600, height:int = 400, x:int = 0, y:int = 0) -> BrowserWindow:
    """
    create webview window

    :param url: url to show in webview. file, http url available
    :param js_api: javascript api for webview. inherits from 'BrowserAPI'
    :param title: webview window title
    :param icon: webview window title. default is 'assets/icon.png'
    :param width: width of window. default is 600
    :param height: height of window. default is 400
    :param x: x position of window. default is 0
    :param y: y position of window. default is 0
    :return: BrowserWindow object
    """
    if not __app:
        raise RuntimeError("run initialize first!")

    return BrowserWindow(url, js_api, title, icon, width, height, x, y)

def start(on_start:object = None, on_stop:object = None, debug:bool = False):
    """
    start webview services

    :param on_start: function on service started
    :param on_stop: function on service stopped
    :param debug: enable/disable debug. if 'True', show devtool automatically. default is 'False'
    """

    if not __app:
        raise RuntimeError("run initialize first!")

    if debug:
        for window in __app.windows:
            window.debug = True

    if on_start:
        from threading import Thread
        Thread(target = on_start, daemon = True).start()

    __app.run(on_stop)
