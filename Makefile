.PHONY: format lint test sec

format:
	@black src/pypdtools/
	@black tests/
	@isort -m 3 src/pypdtools/
	@isort -m 3 tests/

lint:
	@black src/pypdtools/ --check
	@black tests/ --check
	@flake8 src/pypdtools/
	@flake8 tests/
	@isort -m 3 src/pypdtools/ --check
	@isort -m 3 tests/ --check


test:
	@pytest -v
	
sec:
	@pip-audit