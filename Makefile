run:
	poetry run python $(name)

shell:
	poetry shell

lint:
	@poetry run python -m black *.py

