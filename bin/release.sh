pipx install .
python3 -m build
python3 -m twine upload --repository testpypi dist/*
pipx uninstall mio-client
pipx install -i https://test.pypi.org/simple/ mio-client
python3 -m twine upload --repository pypi dist/*
pipx uninstall mio-client
pipx install   mio-client