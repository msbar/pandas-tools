.PHONY: format lint test sec

format:
	@black pandastools/
	@black tests/
	@isort -m 3 pandastools/
	@isort -m 3 tests/

lint:
	@black pandastools/ --check
	@black tests/ --check
	@flake8 pandastools/
	@flake8 tests/
	@isort -m 3 pandastools/ --check
	@isort -m 3 tests/ --check


test:
	@pytest -v
	
sec:
	@pip-audit