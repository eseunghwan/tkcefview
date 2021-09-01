# -*- coding: utf-8 -*-
import os, sys
__import_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(__import_dir)

import tkcefview as tc

tc.initialize()
tc.create_window("http://www.google.com", title = "debug_test")
tc.start(debug = True)
