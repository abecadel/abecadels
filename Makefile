all:
	python setup.py sdist bdist_wheel

test:
	tox

upload_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install_test:
	pip install --index-url https://test.pypi.org/simple/ abecadels
	
upload:
	twine upload --repository-url https://pypi.org/legacy/ dist/*

install:
	pip install abecadels

clean:
	rm -rf build dist Abecadels.egg-info .tox .pytest_cache
