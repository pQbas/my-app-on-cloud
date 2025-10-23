.PHONY: dev run install help

# Default target
.DEFAULT_GOAL := help

install: ## Install dependencies
	pip install -e .

dev: ## Run API in development mode
	uvicorn src.main:app --reload

run: ## Run API in production mode
	uvicorn src.main:app --host 0.0.0.0 --port 8000

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-10s %s\n", $$1, $$2}'
