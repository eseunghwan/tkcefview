# -*- coding: utf-8 -*-
import tkcefview

tkcefview.initialize()

class API(tkcefview.BrowserAPI):
    count = 0

    def count_up(self):
        self.count += 1
        self.update_count()

    def count_down(self):
        if self.count > 0:
            self.count -= 1
            self.update_count()

    def update_count(self):
        self.execute_javascript("update_count", self.count)

tkcefview.create_window("index.html", title = "tkcefview_test", js_api = API)
tkcefview.start(debug = True)
