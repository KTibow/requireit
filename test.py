def test_docstring():
  import requireit
  assert len(requireit.requireit.__doc__) > 0
  del requireit
def test_valid():
  import requireit
  import requireitmini
  assert hasattr(requireit, "requireit")
  assert hasattr(requireitmini, "requireit")
  del requireit
  del requireitmini
  exec(open("requireitmini-inline.py", "r").read())
  assert "requireit" in locals()
  del A
  del VersionError
  del InstallError
  del E
  del F
  del requireit
