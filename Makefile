TESTRUNNER = $(shell which nosetests)
nosetest:
	nosetests -s --with-coverage --cover-erase --cover-package=vdt.simpleaptrepo --cover-xml --logging-level=INFO --with-doctest --verbosity=2

install:
	python setup.py develop
	pip install -e .[test] 

test: install nosetest
	