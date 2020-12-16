clean:
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' -delete

nosetest:
	nosetests -s --with-coverage --cover-erase --cover-package=vdt.simpleaptrepo --cover-xml --logging-level=INFO --with-doctest --verbosity=2

install:
	pip install -e .[dev]

test: nosetest

docker-test:
	docker run --rm -v $(PWD):/usr/local/src maerteijn/simpeapt-test-image ./docker/run-tests.sh

clean_release: clean
	if [ -d "dist" ]; then rm dist/*; fi

release_testpypi: clean_release
	python setup.py sdist
	twine upload --repository pypitest dist/*

release: clean_release
	python setup.py sdist
	twine upload --repository pypi dist/*
