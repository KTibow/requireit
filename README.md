<a href="#" class="readmelogo"><img alt="requireit logo" src="https://github.com/KTibow/requireit/raw/master/assets/requireit.png" /></a>  
Requireit is smart on-run package install for your Python code. Basically you add 13 lines of code to the top of your code, switch out `import bla` for `requireit(['bla'])`, and missing packages get installed on run with `pip`.  
  
![Lint and test](https://github.com/KTibow/requireit/workflows/Lint%20and%20test/badge.svg)  
## How to use
There are three versions of requireit:
1. The [full version](requireit.py?raw=true). It has docstrings and works if you paste it at the top of your code or if you include it.
2. The [mini version](requireitmini.py?raw=true). It's half as small as the full version, but has everything except docstrings and nice formatting.
3. The [mini inline version](requireitmini-inline.py?raw=true), only 13 lines. It is hard-coded so you have to paste it at the top of your code, or do this instead of an import:
```python3
exec(open("requireitmini-inline.py", "r").read())
```
  
Requireit is easy to use, no matter which version you choose. The mini inline version is recommended.
## Example
```python3
from subprocess import check_output as A;import sys#git.io/JUVEE
class VersionError(Exception):0
class InstallError(Exception):0
E="Couldn't auto-install ";F=[sys.executable,"-m","pip","install"]
def requireit(B):
	for C in B:
		J=C if isinstance(C,str)else C[0]
		try:from importlib import import_module as L
		except ImportError:raise VersionError("⬆🐍")
		try: globals()[J]=L(J)
		except ModuleNotFoundError if sys.version_info.minor > 5 else ImportError:
			try:A(F+[C]) if isinstance(C,str)else A(F+[C[1]]);globals()[J]=L(J)
			except Exception:raise InstallError(E+J)

requireit([["onedrivesdk", "git+https://github.com/OneDrive/onedrive-sdk-python.git"], "shutdown"])
# Requireit automatically imports and installs!
shutdown(time=120)
```
## (Tiny) Docs
Use the instructions [from earlier](#how-to-use). To require something, call `requireit` with your list of stuff.  
For custom sources, use a sub array. The first item is the name of the library, and the second is the pip command.  
Example to install `shutdown` and `onedrivesdk`:
```python3
# Do your other code and add requireit here...
requireit([["shutdown", "shutdown==0.0.1"],
           ["onedrivesdk", "git+https://github.com/OneDrive/onedrive-sdk-python.git"]])
```
## What I think you'll frequently ask... (WITYFA)
### `emailHelpers`, one of your other projects is available on pip. Why isn't `requireit` available there too?
Because it wouldn't make sense to install a package that installs other packages.
### What should I do now?
- I'd appreciate it if you'd contribute to the repo, by letting me know about bugs in issues, by making pull requests that make things better, or just the simple act of [![Saying Thanks!](https://img.shields.io/badge/Saying%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/kendell.r@outlook.com)
- Bundle `requireit` with your example code for your `pip` package, or with your code for anything that requires something installable from `pip`. 
- Spread the word. If you think `requireit` makes writing and running code easier, tell your friends.
  
### Badge me!
You can use `shields.io` for your badges. Here's some URLs for requireit. The first one is longer, and the second one is shorter.
  
<details><summary>Click to show badge URLs</summary>

```
https://img.shields.io/badge/smart%20dependency%20install-powered%20by%20requireit-099
https://img.shields.io/badge/dependencies-auto--installed-099
https://img.shields.io/badge/dependencies%20auto--installed-by%20requireit-099
```
</details>
In Markdown, use this:
  
<details><summary>Click to show Markdown</summary>

```
[![Smart dependency install powered by requireit](https://img.shields.io/badge/smart%20dependency%20install-powered%20by%20requireit-099)](https://github.com/KTibow/requireit/)  
[![Dependencies are auto-installed](https://img.shields.io/badge/dependencies-auto--installed-099)](https://github.com/KTibow/requireit/)  
[![Dependencies are auto-installed by requireit](https://img.shields.io/badge/dependencies%20auto--installed-by%20requireit-099)](https://github.com/KTibow/requireit/)  
```
</details>
They produce this:   
  
  - [![Smart dependency install powered by requireit](https://img.shields.io/badge/smart%20dependency%20install-powered%20by%20requireit-099)](https://github.com/KTibow/requireit/)  
  - [![Dependencies are auto-installed](https://img.shields.io/badge/dependencies-auto--installed-099)](https://github.com/KTibow/requireit/)  
  - [![Dependencies are auto-installed by requireit](https://img.shields.io/badge/dependencies%20auto--installed-by%20requireit-099)](https://github.com/KTibow/requireit/)  
  
### Aah! It says:
```
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
```
Upgrade requireit, this is fixed.
### My lint fails when I use `requireit`!
  
<details><summary>Click to expand explanation and fix</summary>
Requireit uses something I (unoficially) like to call "dynamic variable assignment". Let's look at the source:
```python3
try:
    if isMain:
	    globals()[libName] = import_module(libName)
    else:
	    __main__.__dict__[libName] = import_module(libName)
```
This is **very** hacky, but it is still real Python code. Basically, we found out if we were included inline or imported seperately from this:
```python3
isMain = __name__ == '__main__'
```
We get the module as a variable from `importlib`'s `import_module`. Then if we are main, we set the module globally to that name. Otherwise, we import `__main__`, and access its `__dict__`.  
The thing is, **your lint wasn't built for dynamic variable assignment**. To fix this, and be safe, do something like this:
```python3
shutdown, onedrivesdk = [None] * 2
# Requireit stuff here
# Require them
if shutdown is None or onedrivesdk is None:
    print("Error with requireit. Try changing all of this to:")
    print("import shutdown, onedrivesdk")
    exit()
# Your code here
```
That should make your lint happy!
</details>
  
### It's hard to switch to `requireit`.
Well, I've designed the `requireIt Helper` for that purpose. It's **only for development**, but it can make things easier.  
It uses [Import Hooks](https://www.google.com/search?q=import+hooks) to intercept when you import a package.  
If you import something, and it asks you if you want to install something other than the original thing you imported, say no.  
Anyway, here it is:  
```python3
# requireIt Helper (dev only) https://ktibow.github.io/requireit/#requireit-helper
import sys # Import sys for importing
from importlib.abc import MetaPathFinder # Subclassing
from importlib.util import find_spec # Other imports
importing = False
importingName = ""
class RequireItHelper(MetaPathFinder):
    def find_spec(self, fullname, path, target=None): # Import hook for finding
        global importing
        global importingName
        if not importing:
            importing = True
            importingName = fullname
        try:
            try:
                del sys.meta_path[0] # Remove myself
                res = find_spec(fullname) # Try importing
            finally:
                sys.meta_path.insert(0, self) # Add myself
            if res is not None: # If found, return
                importing = False
                return res
        except Exception as e: # If exception, return
            importing = False
            return None
        if "._" in fullname or (importing and importingName != fullname) or fullname in list(sys.modules.keys()):
            importing = False
            return None # Attempt to find internals and not nother asking for install.
        shouldinstall = input("=== Should I try to install "+fullname+" with pip because I couldn't import it? (Beware of typosquatting) y/n: ") # Confirm
        if shouldinstall.lower()[0] == "y":
	    print("Loading pip...")
            try:
                del sys.meta_path[0] # Remove myself
                from subprocess import check_output as pip # Import pip
            finally:
                sys.meta_path.insert(0, self) # Add myself
            pipmain([sys.executable, "-m", "pip", "install", input("What is this package called on pip? ")]) # Run pip to install
            print("Done, I'll try again...")
            try:
                try:
                    del sys.meta_path[0]
                    res = find_spec(fullname)
                finally:
                    sys.meta_path.insert(0, self)
                if res is not None:
                    importing = False
                    print("Successful import!")
                    return res
            except Exception as e:
                res = None
                print("Error importing due to this exception:")
                print(e)
                print("Try manually running pip install " + fullname + ".")
                importing = False
                return None
            if res == None:
                print("Error importing. Try manually importing or manually running pip install " + fullname + ".")
            importing = False
            return res
        importing = False
        return None
sys.meta_path.insert(0, RequireItHelper()) # Install requireIt Helper
```
  
## Bye! 👋  
