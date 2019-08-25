from pip._internal import main as pipmain
# pipit is just a way to run pip
pipit = lambda theargs: pipmain(theargs.split(" "))
# just a custom exception
class VersionError(Exception):
	pass
# downloads if not there
def makeSure(libname):
	try:
		import importlib
	except ImportError:
		raise VersionError("Please upgrade your Python interpreter.")
	try:
		importlib.import_module(libname)
	except ModuleNotFoundError as e:
		try:
			pipit("install "+libname)
			importlib.import_module(libname)
		except Exception as f:
	return f
# imports string
def importIt(libname):
	try:
		import importlib
	except ImportError:
		raise VersionError("Please upgrade your Python interpreter.")
	globals()[libname] = importlib.import_module(libname)
# the thing you probably want
def makeSureAndImport(libname):
	f = makeSure(libname)
	importIt(libname)
	return f
# the thing you really want
def requireit(libs, verbose):
	for lib in libs:
		f = makeSureAndImport(lib)
		if verbose and f is not None:
			print("Auto installation failed for "+lib)
		elif verbose:
			print("Auto installation succeded for "+lib)
		
# the thing you might want
def requireExists(libs, verbose):
	for lib in libs:
		f = makeSure(lib)
		if verbose and f is not None:
			print("Auto installation failed for "+lib)
		elif verbose:
			print("Auto installation succeded for "+lib)
    

