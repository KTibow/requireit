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
