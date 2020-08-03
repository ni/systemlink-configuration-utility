pyfiles = slconf test *.py
test_files = slconf

test:
	pytest -s -v tests/test_$(test_files).py --doctest-modules --cov slconf --cov-config=.coveragerc --cov-report term-missing

lint:
	flake8 ./ --exclude basic_scripts

fix:
	autopep8 --in-place -r ./

install:
	pip install -U -r requirements.txt -r test-requirements.txt

report:
	codecov

build: slconf
	rm -rf dist
	python setup.py sdist bdist_wheel

publish:
	make build
	twine upload --config-file ~/.pypirc -r pypi dist/*

.PHONY: test build
