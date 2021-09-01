
<hr>
<p align="center">
<img src="https://github.com/eseunghwan/tkcefview/blob/master/tkcefview/assets/tkcefview.png?raw=true" width=150 /><br>
<font size="7">tkcefview</font>
</p>
<hr>
<p align="center"><font size="5">pywebview inspired tkinter framed cefpython3</font></p>

<br><br><br>
## Installation
```powershell
<# from master branch(git) #>
pip3 install git+https://github.com/eseunghwan/tkcefview.git
<# from pypi #>
pip3 install tkcefview
```
<img src="https://github.com/eseunghwan/tkcefview/blob/master/tests/installation.png?raw=true" width=400 >

<br><br>

## Basic Usage
```python
import tkcefview as tc

tc.initialize()
tc.create_window("http://www.google.com")
tc.start()
```
<img src="https://github.com/eseunghwan/tkcefview/blob/master/tests/base_test.png?raw=true" width=400 >

<br><br>

## Debug Mode
```python
import tkcefview as tc

tc.initialize()
tc.create_window("[{my_html_file}](http://www.google.com)")
tc.start(debug = True)
```
<img src="https://github.com/eseunghwan/tkcefview/blob/master/tests/debug_test.png?raw=true" width=400 >

<br><br>

## Javascript API
```python
import tkcefview as tc

class MyAPI(tc.BrowserAPI):
    # properties, methods, and so on

tc.initialize()
tc.create_window("{my_html_file}", js_api = MyAPI)
tc.start()
```
<img src="https://github.com/eseunghwan/tkcefview/blob/master/tests/jsapi_test.png?raw=true" width=400 >
