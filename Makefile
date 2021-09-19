install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=brain_games --cov-report xml

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck lint

build: check
	rm ./dist/*
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-upgrade:
	python3 -m pip install --user --upgrade dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

.PHONY: install test lint selfcheck check build