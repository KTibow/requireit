from subprocess import check_output as A;import sys#git.io/JUVEE
class VersionError(Exception):0
class InstallError(Exception):0
E="Couldn't auto-install ";F=[sys.executable,"-m","pip","install"]
def requireit(B):
	for C in B:
		J=C if isinstance(C,str)else C[0]
		try:from importlib import import_module as L
		except ImportError:raise VersionError("⬆🐍")
		try: globals()[J]=L(J)
		except ModuleNotFoundError if sys.version_info.minor > 5 else ImportError:
			try:A(F+[C]) if isinstance(C,str)else A(F+[C[1]]);globals()[J]=L(J)
			except Exception:raise InstallError(E+J)
