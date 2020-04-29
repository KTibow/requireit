import pytest
def test_docstring():
  import requireit
  assert len(requireit.requireit.__doc__) > 0
  del requireit
def test_full_requireit():
  import requireit
  assert isinstance(requireit.requireit, object)
  with pytest.raises(ModuleNotFoundError):
    import onedrivesdk
  with pytest.raises(ModuleNotFoundError):
    import test0408
  requireit.requireit([["onedrivesdk", "git+https://github.com/OneDrive/onedrive-sdk-python.git"], "test0408"])
  assert isinstance(onedrivesdk, object)
  assert isinstance(test0408, object)
