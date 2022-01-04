# -*- coding: utf-8 -*-
import os, sys, typing, threading
import tkinter as tk
from cefpython3 import cefpython as cef
from .assets import base_icon_file, base_js_file


class BrowserAPI:
    """
    BrowserAPI base class

    func execute_javascript: execute javascript code in webview
    func execute_function: execute defined javascript function in webview
    """
    def __init__(self, browser_window, browser):
        self.window:BrowserWindow = browser_window
        self.__browser = browser

    def execute_javascript(self, js_script):
        """
        execute javascript in webview

        :param js_script: javascript script to execute
        """
        self.__browser.ExecuteJavascript(js_script)

    def execute_function(self, name:str, *args):
        """
        execute defined javascript function in webview

        :param name: name of javascript function to execute
        :param args: arguments for javascript function
        """
        self.__browser.ExecuteFunction(name, *args)


class BrowserWindow(tk.Toplevel):
    """
    BrowserWindow class

    :param url: url to show in webview. file, http url available
    :param js_api: javascript api for webview. inherits from 'BrowserAPI'
    :param title: webview window title
    :param icon: webview window title.
    :param width: width of window.
    :param height: height of window.
    :param x: x position of window.
    :param y: y position of window.

    event on_load: function to trigger on webview page is loaded
    event on_close: function to trigger on webview window is closed
    """
    debug:bool = False

    class BrowserWindowHandler:
        def __init__(self, browser_window):
            self.browser_window:BrowserWindow = browser_window

        def OnLoadingStateChange(self, browser, is_loading, **_):
            if not is_loading:
                if sys.platform == "win32":
                    self.browser_window.geometry(f"{self.browser_window.wb_width}x{self.browser_window.wb_height}+{self.browser_window.wb_x}+{self.browser_window.wb_y}")

                self.browser_window.on_load(browser)

    def __init__(self, url:str, js_api_cls:typing.Union[BrowserAPI, typing.List[BrowserAPI]], title:str, icon:str, width:int, height:int, x:int, y:int):
        super().__init__()

        self.__is_cef_init = False
        self.__js_api_cls = js_api_cls
        self.icon = base_icon_file if icon is None else os.path.realpath(icon)
        if url.startswith("http://") or url.startswith("https://"):
            self.url = url
        elif url.startswith("file://"):
            self.url = "file://" + os.path.realpath(url[7:])
        else:
            self.url = "file://" + os.path.realpath(url)

        self.title(title)
        self.iconphoto(False, tk.PhotoImage(file = self.icon))

        width, height = int(width), int(height)
        if x == -1:
            x = int((self.winfo_screenwidth() - width) / 2)
        else:
            x = int(x)

        if y == -1:
            y = int((self.winfo_screenheight() - height) / 2)
        else:
            y = int(y)

        self.wb_width, self.wb_height, self.wb_x, self.wb_y = width, height, x, y
        if not sys.platform == "win32":
            self.geometry(f"{width}x{height}+{x}+{y}")

        self.bind("<Configure>", self.__on_tk_configure)
        self.protocol("WM_DELETE_WINDOW", self.__on_tk_close)

        Application.windows.insert(0, self)

    def show_devtools(self):
        """
        show devtools
        """
        self.__browser.ShowDevTools()
        self.focus()

    def close_devtools(self):
        """
        close devtools
        """
        self.__browser.CloseDevTools()

    def register_js_api(self, js_api_cls:BrowserAPI):
        """
        register additional BrowserAPI class

        :param js_api_cls: BrowserAPI inherited api class
        """
        if js_api_cls is not None:
            js_api = js_api_cls(self, self.__browser)
            self.register_object(js_api.__class__.__name__, js_api)

    def register_object(self, name, object):
        self.__bindings.SetObject(name, object)
        self.__bindings.Rebind()

    def on_load(self, browser):
        pass

    def on_close(self, browser):
        pass

    def __on_tk_configure(self, _):
        if not self.__is_cef_init:
            self.__is_cef_init = True

            winfo = cef.WindowInfo()
            if sys.platform == "win32":
                geometry = [ 0, 0, self.wb_width, self.wb_height ]
            else:
                geometry = [ 0, 0, self.winfo_width(), self.winfo_height() ]

            winfo.SetAsChild(self.__get_handle(), geometry)
            self.__browser = browser = cef.CreateBrowserSync(winfo, url = self.url)
            assert browser

            self.__bindings = bindings = cef.JavascriptBindings(bindToFrames = False, bindToPopups = False)
            browser.SetJavascriptBindings(bindings)

            if isinstance(self.__js_api_cls, list):
                for api_cls in self.__js_api_cls:
                    self.register_js_api(api_cls)
            else:
                self.register_js_api(self.__js_api_cls)

            browser.SetClientHandler(BrowserWindow.BrowserWindowHandler(self))

            if self.debug:
                self.show_devtools()

            # threading.Thread(target = self.__on_load).start()
            self.__cef_loop()

    def __on_tk_close(self):
        Application.windows.remove(self)
        self.on_close(self.__browser)
        self.__browser.CloseBrowser(True)
        self.destroy()

        if len(Application.windows) == 0:
            self.master.destroy()

    def __get_handle(self):
        if sys.platform == "darwin":
            from AppKit import NSApp
            import objc

            tk_windows = [ win for win in NSApp.windows() if str(win).startswith("<TKWindow: ") ][:-1]
            mac_self = tk_windows[Application.windows.index(self)]

            return objc.pyobjc_id(mac_self.contentView())
        else:
            return self.winfo_id()

    def __cef_loop(self):
        try:
            cef.MessageLoopWork()
            self.after(5, self.__cef_loop)
        except:
            pass

class Application(tk.Tk):
    """
    Base Application environment for webview

    :param settings: dictionary type of environment settings
    more details in "https://github.com/cztomczak/cefpython/blob/master/api/ApplicationSettings.md"
    """
    windows:typing.List[BrowserWindow] = []

    def __init__(self, settings:dict = {}, **kwargs):
        super().__init__(**kwargs)

        self.withdraw()

        if sys.platform == "darwin":
            settings["external_message_pump"] = True

        sys.excepthook = cef.ExceptHook
        cef.Initialize(settings)

    def run(self, on_stop:object = None):
        """
        run webview environment

        :param on_stop: function when environment stopped
        """
        self.mainloop()
        cef.Shutdown()

        if on_stop:
            on_stop()
