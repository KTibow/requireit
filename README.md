# requireit
![requireit logo](requireit.png)  
Ever tried to get people to run your great code only to find out that they don't have all of the required packages? Requireit streamlines user experience by automatically installing libraries you don't have. It's as easy as pasting in less than 12 lines at the top of your code.  
![Lint and test](https://github.com/KTibow/requireit/workflows/Lint%20and%20test/badge.svg)  
## How to use
There are three versions of requireit. The first version is the [full version](requireit.py?raw=true). It has docstrings and works if you paste it at the top of your code or if you include it. The second version is the [mini version](requireitmini.py?raw=true). It's half as small as the full version, but has everything except docstrings and nice formatting. The other option is the [mini inline version](requireitmini-inline.py?raw=true), only 13 lines. It is hard-coded so you have to paste it at the top of your code, or do this instead of an import:
```python3
exec(open("requireitmini-inline.py", "r").read())
```
Note: You might see a `WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.` Don't worry about that. It won't actually fail. If it does, I'll update this.
