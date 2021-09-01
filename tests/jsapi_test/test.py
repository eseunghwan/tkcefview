# -*- coding: utf-8 -*-
import os, sys
__import_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(__import_dir)

import tkcefview as tc

tc.initialize()

class MyAPI(tc.BrowserAPI):
    count = 0

    def count_up(self):
        self.count += 1
        self.update_count()

    def count_down(self):
        if self.count > 0:
            self.count -= 1
            self.update_count()

    def update_count(self):
        self.execute_function("update_count", self.count)

tc.create_window("index.html", title = "jsapi_test", js_api = MyAPI)
tc.start()
