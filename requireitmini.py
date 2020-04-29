#https://github.com/KTibow/requireit
from pip._internal import main as m
pipit = lambda a: pipmain(a.split(" "))
class VersionError(Exception):
	pass
def requireit(m):
  w = True
  for l in m:
    try:
      import importlib
    except ImportError:
    	raise VersionError("Please upgrade your Python interpreter.")
    try:
    	globals()[l] = importlib.import_module(l)
    except ModuleNotFoundError as e:
      try:
        pipit("install "+l)
        globals()[l] = importlib.import_module(l)
      except Exception as f:
        w = False
  return w
