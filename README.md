# requireit
A simple bit of code to make sure you have all of your libraries. It streamlines user experience by automatically installing libraries the user doesn't have, and then importing. It has all of the features of pip, and you can dynamically import because it takes a list of strings as what to import.
## Quick start:
Copy everything from [requireit.py](https://raw.githubusercontent.com/KTibow/requireit/master/requireit.py) into the top of your code. The reason you can't import it is if you import it, requireit can only install not import. (When you import python code, it's kind of in a sandbox.)
Here's how to do it, in a real-life situation:
```python3
#This is requireit, a way to simplify user experience by automatically installing libraries.
#Find out about it at https://github.com/KTibow/requireit
from pip._internal import main as pipmain
# pipit is just a way to run pip
pipit = lambda theargs: pipmain(theargs.split(" "))
# just a custom exception
class VersionError(Exception):
  pass
def requireit(libs):
  """Libs is a list of libraries, like ["requests", "ffsend"]. Returns True if everything went right and False elsewise.
  If there's an error importing one library, it'll keep on importing. 
  The other nice thing about requireit is that packages can be dynamic. You don't need to manually type import a whole bunch of times.
  requireit is not a replacement for requirements.txt; it's just a way to streamline user experience by not making them open a command prompt.
  The reason that you can't import requireit is that it'll only import libraries in its own file, not your code."""
  worked = True
  for lib in libs:
    try:
      import importlib
    except ImportError:
    	raise VersionError("Please upgrade your Python interpreter.")
    try:
    	globals()[lib] = importlib.import_module(lib)
    except ModuleNotFoundError as e:
      try:
        pipit("install "+lib)
        globals()[lib] = importlib.import_module(lib)
      except Exception as f:
        worked = False
  return worked
# Code starts here
requireit(["notificationcenter", "shutdown"])
notificationcenter = NotificationCenter()
notificationcenter.post_notification(sender=None, with_name="Restarting soon to help performance, make sure you finish up")
shutdown(time=120)
```
## How it works
I worked hard to make requireit.
First, it `import`s `importlib`. If it doesn't work, then they're probably using Python 2. I throw a `VersionError` exception. By now, Python 2's deprecated anyway.
Then, it does `globals()[lib] = importlib.import_module(lib)`. Something cool about Python is that you can dynamically name a variable. Try this:
```python3
a
# error because a hasn't been defined yet
a = 1
a
# 1
b
# error because b hasn't been defined yet
globals()['b'] = 2
b
# 2
```
Did you see that? We made a variable from a string. Now, try this:
```python3
time
# error because time hasn't been defined yet
globals()['time']
# error because time hasn't been defined yet
import time
time
# <module 'time' (built-in)>
globals()['time']
# <module 'time' (built-in)>
```
Did you see that? `import` assigned the module `time` to the variable `time`. I mimic that behavior by running `globals()[lib] = importlib.import_module(lib)`. (`lib` is a string that is the library's name.) Now you're probably thinking "We can't just pull out a library out of nowhere!" Actually, we can. Let me prove it:
```python3
import importlib
time = importlib.import_module("time")
time.time()
# seconds since the epoch
del time
# that removes the time that we imported
import time
time.time()
# seconds since the epoch
```
See? It works. That's how I can import stuff out of a string. Thanks, `importlib`!
Now, what about if they don't already have the library installed? Well, then we reverse-engineer pip.
You see, when you run `pip install whatever`, you run the source file of pip. Here's what it basically looks like:
```python3
def main(what-to-do):
  do(what-to-do)
```
Okay, maybe not exactly. But if you run, say, `pip install whatever`, you're calling `main(["install", "whatever"])`. That means we can install stuff by doing this:
```python3
from pip._internal import main as pipmain
pipmain(["install", "whatever"])
```
Yes, I know it's usually a bad idea to go into stuff that says `internal` and stuff that starts with a `_`. But hey, it's the only way I could find to run pip without using `os.system` (which is less dependable), and it works! I simplified this down to a lambda that automatically splits at the spaces:
```python3
pipit = lambda theargs: pipmain(theargs.split(" "))
```
So that's basically how requireit works. The rest is normal python stuff. Now that you've read about it, how about you remember it and when you need it you can use it? Or don't. I did a lot of research on it, though, so enjoy!
