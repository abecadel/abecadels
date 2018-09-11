all:
	python setup.py sdist bdist_wheel
upload_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
upload:
	twine upload --repository-url https://pypi.org/legacy/ dist/*
clean:
	rm -rf build dist Abecadels.egg-info
