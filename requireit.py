# This is requireit. It auto installs things you're missing before you import them. https://github.com/KTibow/requireit
from pip._internal import main as pip
import __main__
class VersionError(Exception):
    pass
class InstallError(Exception):
    pass
isMain = __name__ == '__main__'
installErrorMessage = "Couldn't auto-install "
pipCommand = 'install'
def requireit(libs):
    """Pass a list of libraries to requireit.
    If something needs a different source, then use a sublist.
    Example: ["frompip", "importedtoo", ["fromgithub", "git+https://github.com/fromgithub.git"]]"""
    for lib in libs:
        if isinstance(lib,str):
            libName = lib
        else:
            libName = lib[0]
        try:
            from importlib import import_module
        except ImportError:
            raise VersionError('Please upgrade Python')
        try:
            if isMain:
                globals()[libName] = import_module(libName)
            else:
                __main__.__dict__[libName] = import_module(libName)
        except ModuleNotFoundError:
            try:
                if isinstance(lib, str):
                    pip([pipCommand, lib])
                else:
                    pip([pipCommand, lib[1]])
                if isMain:
                    globals()[libName] = importModule(libName)
                else:
                    __main__.__dict__[libName] = importModule(libName)
            except Exception:
                raise InstallError(installErrorMessage + libName)
