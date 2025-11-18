.PHONY: install install-dev jupyter clean test lint format data-preparation

# Install production dependencies
install:
	uv sync

# Install with development dependencies
install-dev:
	uv sync --dev

# Start Jupyter Lab
jupyter:
	uv run jupyter lab

# Start Jupyter Notebook
notebook:
	uv run jupyter notebook

# Clean up cache and temporary files
clean:
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name "*.egg-info" -delete

# Run tests (when available)
test:
	uv run pytest

# Run linting
lint:
	uv run ruff check .

# Format code
format:
	uv run ruff format .

# Set up development environment
setup-dev: install-dev
	uv run python -m ipykernel install --user --name=ai-materials

# Data preparation: convert PDFs to images
data-preparation:
	@echo "Preparando dados: convertendo PDFs em imagens..."
	uv run python scripts/data_preparation.py

# Help
help:
	@echo "Available commands:"
	@echo "  install           Install production dependencies"
	@echo "  install-dev       Install with development dependencies"
	@echo "  jupyter           Start Jupyter Lab"
	@echo "  notebook          Start Jupyter Notebook"
	@echo "  clean             Clean up cache and temporary files"
	@echo "  test              Run tests"
	@echo "  lint              Run linting"
	@echo "  format            Format code"
	@echo "  setup-dev         Set up development environment"
	@echo "  data-preparation  Convert PDFs to images for data preparation"