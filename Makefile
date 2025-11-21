.PHONY: install install-dev jupyter clean test lint format check-setup install-poppler prepare-data help

# Cores para output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[1;33m
RED := \033[0;31m
NC := \033[0m # No Color

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

# =============================================================================
# PREPARAÇÃO DE DADOS
# =============================================================================

check-poppler: ## Verificar se Poppler está instalado
	@if [ -x /usr/bin/pdfinfo ] || [ -x /usr/local/bin/pdfinfo ]; then \
		PDFINFO_PATH=$$([ -x /usr/bin/pdfinfo ] && echo /usr/bin/pdfinfo || echo /usr/local/bin/pdfinfo); \
		echo "$(GREEN)✓ Poppler está instalado ($$PDFINFO_PATH)$(NC)"; \
	else \
		echo "$(RED)✗ ERRO: Poppler não está instalado!$(NC)"; \
		echo ""; \
		echo "$(YELLOW)O Poppler é NECESSÁRIO para converter PDFs em imagens.$(NC)"; \
		echo ""; \
		echo "$(BLUE)Instale manualmente:$(NC)"; \
		echo "  $(GREEN)Ubuntu/Debian:$(NC)  sudo apt-get install -y poppler-utils"; \
		echo "  $(GREEN)RHEL/CentOS:$(NC)   sudo yum install -y poppler-utils"; \
		echo "  $(GREEN)macOS:$(NC)          brew install poppler"; \
		echo ""; \
		exit 1; \
	fi

prepare-data: check-poppler ## Preparar dados: converte PDFs em imagens (INPUT_DIR=data/pdfs BATCH=10)
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo "$(GREEN)  📄 Preparação de Dados: PDF → Imagens$(NC)"
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo ""
	@echo "$(GREEN)Configuração:$(NC)"
	@echo "  • Input:  $(or $(INPUT_DIR),data/pdfs)"
	@echo "  • Output: $(or $(OUTPUT_DIR),data/images)"
	@echo "  • DPI:    $(or $(DPI),200)"
	@echo "  • Format: $(or $(FORMAT),jpg)"
	@echo "  • Batch:  $(or $(BATCH),10) PDFs por vez"
	@echo ""
	@uv run python scripts/data_preparation.py \
		--input-dir $(or $(INPUT_DIR),data/pdfs) \
		--output-dir $(or $(OUTPUT_DIR),data/images) \
		--dpi $(or $(DPI),200) \
		--format $(or $(FORMAT),jpg) \
		--batch $(or $(BATCH),10) \
		$(if $(VERBOSE),--verbose,)
	@echo ""
	@echo "$(GREEN)✓ Preparação de dados concluída!$(NC)"

prepare-data-test: check-poppler ## Testar preparação com 1 PDF em modo verbose
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo "$(YELLOW)  🧪 TESTE: Preparação de Dados (1 PDF, verbose)$(NC)"
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo ""
	@uv run python scripts/data_preparation.py \
		--input-dir $(or $(INPUT_DIR),data/pdfs) \
		--output-dir $(or $(OUTPUT_DIR),data/images_test) \
		--dpi 150 \
		--format jpg \
		--batch 1 \
		--verbose
	@echo ""
	@echo "$(GREEN)✓ Teste concluído!$(NC)"
	@echo "$(YELLOW)Verifique: data/images_test/$(NC)"

data-preparation: prepare-data ## Alias para prepare-data (retrocompatibilidade)

# =============================================================================
# GROUND TRUTH DATASET
# =============================================================================

check-gemini-key: ## Verificar se GEMINI_API_KEY está configurada
	@if [ -z "$$GEMINI_API_KEY" ]; then \
		echo "$(RED)✗ ERRO: GEMINI_API_KEY não está configurada!$(NC)"; \
		echo ""; \
		echo "$(YELLOW)Configure a chave da API Gemini no arquivo .env:$(NC)"; \
		echo "  $(GREEN)GEMINI_API_KEY=your_api_key_here$(NC)"; \
		echo ""; \
		echo "$(BLUE)Obtenha sua chave em:$(NC) https://ai.google.dev/"; \
		echo ""; \
		exit 1; \
	else \
		echo "$(GREEN)✓ GEMINI_API_KEY está configurada$(NC)"; \
	fi

gt-generate: check-gemini-key ## [ATALHO] Gerar ground truth dataset com Gemini (idempotente)
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo "$(GREEN)  📊 Geração de Ground Truth Dataset$(NC)"
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo ""
	@uv run python scripts/generate_ground_truth.py $(if $(FORCE),--force,) $(if $(VERBOSE),--verbose,)

gt-force: check-gemini-key ## [ATALHO] Reprocessar TODAS as imagens (ignora cache)
	@echo "$(YELLOW)⚠️  MODO FORCE: Reprocessando TODAS as imagens$(NC)"
	@uv run python scripts/generate_ground_truth.py --force $(if $(VERBOSE),--verbose,)

gt-stats: ## [ATALHO] Mostrar estatísticas do ground truth dataset
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo "$(GREEN)  📊 Estatísticas do Ground Truth Dataset$(NC)"
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo ""
	@if [ -f data/ground_truth/metadata.json ]; then \
		echo "$(GREEN)Metadata:$(NC)"; \
		cat data/ground_truth/metadata.json | jq -r 'to_entries[] | "  • \(.key): \(.value)"' 2>/dev/null || cat data/ground_truth/metadata.json; \
		echo ""; \
		TOTAL=$$(wc -l < data/ground_truth/dataset.jsonl 2>/dev/null || echo 0); \
		echo "$(GREEN)Dataset JSONL:$(NC)"; \
		echo "  • Total de exemplos: $$TOTAL"; \
		echo "  • Arquivo: data/ground_truth/dataset.jsonl"; \
		echo ""; \
	else \
		echo "$(YELLOW)⚠️  Ground truth dataset ainda não foi gerado$(NC)"; \
		echo "   Execute: make gt-generate ou make generate-ground-truth"; \
		echo ""; \
	fi

# Aliases longos (retrocompatibilidade)
generate-ground-truth: gt-generate ## Alias longo para gt-generate
generate-ground-truth-force: gt-force ## Alias longo para gt-force
ground-truth-stats: gt-stats ## Alias longo para gt-stats

# Help
help:
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo "$(BLUE)  DSPy Production-Ready Course - Comandos$(NC)"
	@echo "$(BLUE)═══════════════════════════════════════════════════$(NC)"
	@echo ""
	@echo "$(GREEN)Setup & Dependências:$(NC)"
	@echo "  install           Instalar dependências de produção"
	@echo "  install-dev       Instalar com dependências de desenvolvimento"
	@echo "  setup-dev         Configurar ambiente de desenvolvimento"
	@echo ""
	@echo "$(GREEN)Jupyter:$(NC)"
	@echo "  jupyter           Iniciar Jupyter Lab"
	@echo "  notebook          Iniciar Jupyter Notebook"
	@echo ""
	@echo "$(GREEN)Preparação de Dados:$(NC)"
	@echo "  check-poppler          Verificar se Poppler está instalado"
	@echo "  prepare-data           Converter PDFs em imagens (INPUT_DIR=data/pdfs BATCH=10)"
	@echo "  prepare-data-test      Testar preparação com 1 PDF (verbose)"
	@echo ""
	@echo "$(GREEN)Ground Truth Dataset:$(NC)"
	@echo "  check-gemini-key    Verificar se GEMINI_API_KEY está configurada"
	@echo "  gt-generate         Gerar ground truth com Gemini (idempotente)"
	@echo "  gt-force            Reprocessar TODAS as imagens"
	@echo "  gt-stats            Mostrar estatísticas do dataset"
	@echo ""
	@echo "$(GREEN)Qualidade de Código:$(NC)"
	@echo "  test              Executar testes"
	@echo "  lint              Executar linting"
	@echo "  format            Formatar código"
	@echo "  clean             Limpar arquivos temporários"
	@echo ""
	@echo "$(YELLOW)Exemplos de uso - Preparação:$(NC)"
	@echo "  $$ make prepare-data-test                 # TESTE: 1 PDF com verbose"
	@echo "  $$ make prepare-data                      # Processar 10 PDFs (padrão)"
	@echo "  $$ make prepare-data BATCH=0              # Processar TODOS os PDFs"
	@echo "  $$ make prepare-data BATCH=5              # Processar 5 PDFs"
	@echo "  $$ make prepare-data VERBOSE=1            # Modo verbose"
	@echo "  $$ make prepare-data INPUT_DIR=my_pdfs    # Diretório customizado"
	@echo ""
	@echo "$(YELLOW)Exemplos de uso - Ground Truth:$(NC)"
	@echo "  $$ make gt-generate             # Gerar dataset (apenas novas imagens)"
	@echo "  $$ make gt-generate VERBOSE=1   # Modo verbose"
	@echo "  $$ make gt-force                # Reprocessar TODAS as imagens"
	@echo "  $$ make gt-stats                # Ver estatísticas do dataset"
	@echo ""

.DEFAULT_GOAL := help