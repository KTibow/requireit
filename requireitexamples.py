# NOT A NECESSARY FILE
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
# your code here!
print("libraries installed:")
# same as pip freeze
print(pipit("freeze"))
print("making sure asyncio is installed")
# same is checking if asyncio is in the output of pip freeze, and if it isn't, running pip install asyncio
# note the quotes!
makeSure("asyncio")
print("importing asyncio")
# note the quotes again!
importIt("asyncio")
print("making sure asyncio is installed, and then importing it")
# it says it all
makeSureAndImport("asyncio")
print("making sure aiohttp and asyncio is installed")
# it says it all, but the second parameter is verbose or not
requireExists(["aiohttp", "asyncio"], True)
print("making sure aiohttp and asyncio is imported")
# the signature move! (the second parameter is verbose or not)
requireit(["aiohttp", "asyncio"], True)
