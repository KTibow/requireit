#https://github.com/KTibow/requireit
from pip._internal import main as n
q = lambda a: n(a.split(" "))
class VersionError(Exception):
  pass
def requireit(m):
  w = True
  for l in m:
    try:
      import importlib
    except ImportError:
      w = False
      raise VersionError("Please upgrade Python")
    try:
      globals()[l] = importlib.import_module(l)
    except ModuleNotFoundError:
      try:
        q("install "+l)
        globals()[l] = importlib.import_module(l)
      except Exception:
        w = False
        return w
