.PHONY: install install-dev jupyter clean test lint format

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

# Help
help:
	@echo "Available commands:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install with development dependencies"
	@echo "  jupyter      Start Jupyter Lab"
	@echo "  notebook     Start Jupyter Notebook"
	@echo "  clean        Clean up cache and temporary files"
	@echo "  test         Run tests"
	@echo "  lint         Run linting"
	@echo "  format       Format code"
	@echo "  setup-dev    Set up development environment"