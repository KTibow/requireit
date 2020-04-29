# https://github.com/KTibow/requireit
from pip._internal import main as pip
import __main__
class VersionError(Exception):
  pass
class InstallError(Exception):
  pass
def requireit(libs):
  for lib in libs:
    try:
      import importlib
    except ImportError:
      raise VersionError('Please upgrade Python')
    try:
      if __name__ == '__main__':
        if isinstance(lib, str):
          globals()[lib] = importlib.import_module(lib)
        else:
          globals()[lib[0]] = importlib.import_module(lib[0])
      else:
        if isinstance(lib, str):
          __main__.__dict__[lib] = importlib.import_module(lib)
        else:
          __main__.__dict__[lib[0]] = importlib.import_module(lib[0])
    except ModuleNotFoundError:
      try:
        if isinstance(lib, str):
          n(['install', lib])
        else:
          n(['install', lib[1])
        if __name__ == '__main__':
          if isinstance(lib, str):
            globals()[lib] = importlib.import_module(lib)
          else:
            globals()[lib[0]] = importlib.import_module(lib[0])
        else:
          if isinstance(lib, str):
            __main__.__dict__[lib] = importlib.import_module(lib)
          else:
            __main__.__dict__[lib[0]] = importlib.import_module(lib[0])
      except Exception:
        if isinstance(lib, str):
          raise InstallError("Couldn't auto-install " + lib)
        else:
          raise InstallError("Couldn't auto-install " + lib[0])
