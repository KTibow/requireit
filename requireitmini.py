#https://github.com/KTibow/requireit
from pip._internal import main as n
class VersionError(Exception): pass
def requireit(m):
  for l in m:
    try: import importlib
    except ImportError: raise VersionError("Please upgrade Python")
    try: globals()[l if isinstance(l, str) else l[0]]=importlib.import_module(l if isinstance(l, str) else l[0])
    except ModuleNotFoundError: try: n(["install",l if isinstance(l, str) else l[1]]); globals()[l if isinstance(l, str) else l[0]]=importlib.import_module(l if isinstance(l, str) else l[0])
    except Exception: return False
    
