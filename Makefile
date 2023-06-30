.PHONY: format lint test sec

format:
	@black pypdtools/
	@black tests/
	@isort -m 3 pypdtools/
	@isort -m 3 tests/

lint:
	@black pypdtools/ --check
	@black tests/ --check
	@flake8 pypdtools/
	@flake8 tests/
	@isort -m 3 pypdtools/ --check
	@isort -m 3 tests/ --check


test:
	@pytest -v
	
sec:
	@pip-audit