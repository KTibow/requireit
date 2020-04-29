#https://github.com/KTibow/requireit
from pip._internal import main as n
class VersionError(Exception): pass
def requireit(m):
  for l in m:
    try: import importlib
    except ImportError: raise VersionError("Please upgrade Python")
    try: globals()[l]=importlib.import_module(l)
    except ModuleNotFoundError: try: n(["install",l if isinstance(l, str) else l[1]]); globals()[l]=importlib.import_module(l)
    except Exception: return False
