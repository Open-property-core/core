# Dev: install deps with dev extras first — uv sync --extra dev
.PHONY: format lint typecheck test check

test:
	uv run pytest

format:
	uv run isort .
	uv run black .

lint:
	uv run flake8 .

typecheck:
	uv run mypy opc

check: format lint typecheck test
	@echo "All checks passed."
