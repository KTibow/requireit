# This is requireit. It auto installs things you're missing before you import them. https://github.com/KTibow/requireit
from subprocess import check_output as pip
import __main__
import sys
class VersionError(Exception):
    pass
class InstallError(Exception):
    pass
isMain = __name__ == "__main__"
installErrorMessage = "Couldn't auto-install "
pipCommand = [sys.executable, "-m", "pip", "install"]
def requireit(libs):
    """Pass a list of libraries to requireit.
    If something needs a different source, then use a sublist.
    Example: ["frompiplibname", "importedtoolibname", ["fromgithublibname", "git+https://github.com/fromgithub.git"]]"""
    for lib in libs:
        if isinstance(lib,str):
            libName = lib
        else:
            libName = lib[0]
        try:
            from importlib import import_module
        except ImportError:
            raise VersionError("Please upgrade Python")
        try:
            if isMain:
                globals()[libName] = import_module(libName)
            else:
                __main__.__dict__[libName] = import_module(libName)
        except ModuleNotFoundError if sys.version_info.minor > 5 else ImportError:
            try:
                if isinstance(lib, str):
                    pip(pipCommand + [lib])
                else:
                    pip(pipCommand + [lib[1]])
                if isMain:
                    globals()[libName] = import_module(libName)
                else:
                    __main__.__dict__[libName] = import_module(libName)
            except Exception:
                raise InstallError(installErrorMessage + libName)
