install:
	python setup.py develop
	pip install -e .[test] 

test: install
	nosetests --with-coverage  --cover-erase --cover-package=vdt.simpleaptrepo  --cover-xml --logging-level=INFO --with-doctest
