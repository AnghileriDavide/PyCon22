SRC_DIR = src

install: ## Install dependencies
	poetry run pip install --upgrade pip
	poetry install -v

update: ## Update python dependencies
	poetry update -vvv

format: ## Format repository code
	poetry run black $(SRC_DIR)
	poetry run isort $(SRC_DIR)

format-check: ## Check the code format
	poetry run black --check $(SRC_DIR)
	poetry run isort --check $(SRC_DIR)

lint: ## Launch the linting tool
	poetry run pylint -j 0 $(SRC_DIR)

type-check: ## Launch the type checking tool
	poetry run mypy $(SRC_DIR)

check: format-check lint type-check ## Launch all check to approve the code
