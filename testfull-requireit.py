import requireit
assert onedrivesdk not in globals()
assert test0408 not in globals()
requireit.requireit([["onedrivesdk", "git+https://github.com/OneDrive/onedrive-sdk-python.git"], "test0408"])
assert isinstance(onedrivesdk, object)
assert isinstance(test0408, object)
del requireit
del onedrivesdk
del test0408
