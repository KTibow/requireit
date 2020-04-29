# https://github.com/KTibow/requireit
from pip._internal import main as A
import __main__
class VersionError(Exception): 0
class InstallError(Exception): 0
D = __name__ == '__main__'
E = "Couldn't auto-install "
def requireit(B):
  for C in B:
    F = isinstance(C, str)
    try: import importlib as il
    except ImportError: raise VersionError('Please upgrade Python')
    try:
      if D:
        if F: globals()[C]=il.import_module(C)
        else: globals()[C[0]]=il.import_module(C[0])
      else:
        if F: __main__.__dict__[C]=il.import_module(C)
        else: __main__.__dict__[C[0]]=il.import_module(C[0])
    except ModuleNotFoundError:
      try:
        if F: A(['install',C])
        else: A(['install',C[1]])
        if D:
          if F: globals()[C]=il.import_module(C)
          else: globals()[C[0]]=il.import_module(C[0])
        else:
          if F: __main__.__dict__[C]=il.import_module(C)
          else: __main__.__dict__[C[0]]=il.import_module(C[0])
      except Exception:
        if F: raise InstallError(E+lib)
        else: raise InstallError(E+lib[0])
