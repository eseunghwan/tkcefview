
<hr>
<p align="center">
<img src="https://github.com/eseunghwan/tkcefview/blob/master/tkcefview/assets/tkcefview.png?raw=true" width=30 />
<font size="20">&nbsp;tkcefview</font>
</p>
<hr>
<p align="center"><font size="5">pywebview inspired tkinter framed cefpython3</font></p>

<br><br><br>
## Installation
```powershell
<# from master branch(git) #>
pip3 install https://github.com/eseunghwan/tkcefview.git
<# from pypi #>
pip3 install tkcefview
```
<br>

## Basic Usage
```python
import tkcefview as tc

tc.initialize()
tc.create_window("http://www.google.com")
tc.start()
```
<br>

## Debug Mode
```python
import tkcefview as tc

tc.initialize()
tc.create_window("[{my_html_file}](http://www.google.com)")
tc.start(debug = True)
```
<br>

## Javascript API
```python
import tkcefview as tc

class MyAPI(tc.BrowserAPI):
    # properties, methods, and so on

tc.initialize()
tc.create_window("{my_html_file}", js_api = MyAPI)
tc.start()
```
