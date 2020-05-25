from pip._internal import main as A;import __main__,sys#https://github.com/KTibow/requireit
class VersionError(Exception):0
class InstallError(Exception):0
D=__name__=='__main__';E="Couldn't auto-install ";F='install'
def requireit(B):
	for C in B:
		J=C if isinstance(C,str)else C[0]
		try:from importlib import import_module as Z
		except ImportError:raise VersionError('Please upgrade Python')
		try:
			if D:globals()[J]=Z(J)
			else:__main__.__dict__[J]=Z(J)
		except ModuleNotFoundError if sys.version_info.minor>5 else ImportError:
			try:
				A([F,C]) if isinstance(C,str) else A([F,C[1]])
				if D:globals()[J]=Z(J)
				else:__main__.__dict__[J]=Z(J)
			except Exception:raise InstallError(E+J)
