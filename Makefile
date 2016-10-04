TESTRUNNER = $(shell which nosetests)

install:
	python setup.py develop
	pip install -e .[test] 

test: install
	coverage run $(TESTRUNNER) -s --logging-level=INFO --with-doctest
	coverage report -m --include=vdt/simpleaptrepo/*
	coverage xml --include=vdt/simpleaptrepo/* -o coverage.xml
