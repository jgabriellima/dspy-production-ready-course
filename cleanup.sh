#!/bin/bash
# cleanup.sh - Script para limpar projeto após migração do projeto de extração
# 
# ATENÇÃO: Este script remove ~480MB de dados relacionados ao projeto
# de extração de dados que foi movido para dspy-data-extraction-optimization
#
# Execute apenas após confirmar que o novo projeto está funcionando!

set -e

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  Limpeza do Projeto: dspy-production-ready-course              ║"
echo "║  Removendo arquivos migrados para dspy-data-extraction-opt     ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar se estamos no diretório correto
if [ ! -f "CLEANUP_PROPOSAL.md" ]; then
    echo "❌ ERRO: Execute este script no diretório raiz do projeto!"
    exit 1
fi

echo "⚠️  ATENÇÃO: Este script irá remover ~480MB de dados."
echo ""
echo "Itens a serem removidos:"
echo "  • data/ (474MB) - PDFs, imagens, ground truth"
echo "  • scripts/ - Scripts de extração"
echo "  • notebooks/dspy_data_extraction_optimization.ipynb"
echo "  • Arquivos de resultado de extração"
echo "  • Documentação de extração"
echo "  • Imagens de exemplo em docs/assets/"
echo ""
read -p "Continuar? (digite 'sim' para confirmar): " confirm

if [ "$confirm" != "sim" ]; then
    echo "❌ Cancelado pelo usuário"
    exit 0
fi

echo ""
echo "🧹 Iniciando limpeza..."
echo ""

# 1. Remover data/ completo
if [ -d "data" ]; then
    echo "  → Removendo data/ (474MB)..."
    rm -rf data/
    echo "    ✓ Removido"
else
    echo "  ⊘ data/ não encontrado (já removido?)"
fi

# 2. Remover scripts/
if [ -d "scripts" ]; then
    echo "  → Removendo scripts/..."
    rm -rf scripts/
    echo "    ✓ Removido"
else
    echo "  ⊘ scripts/ não encontrado"
fi

# 3. Remover notebook de extração
if [ -f "notebooks/dspy_data_extraction_optimization.ipynb" ]; then
    echo "  → Removendo notebook de extração..."
    rm -f notebooks/dspy_data_extraction_optimization.ipynb
    echo "    ✓ Removido"
else
    echo "  ⊘ Notebook de extração não encontrado"
fi

# 4. Remover arquivos de resultado
echo "  → Removendo arquivos de resultado..."
rm -f notebooks/result.extracted_data-google.json 2>/dev/null || true
rm -f notebooks/result.extracted_data-groq.json 2>/dev/null || true
rm -f notebooks/OTIMIZACAO_GROQ_MIPROV2.md 2>/dev/null || true
echo "    ✓ Removido"

# 5. Remover documentação de extração
echo "  → Removendo documentação de extração..."
rm -f WORKFLOW_OTIMIZACAO.md 2>/dev/null || true
rm -f docs/DATA_PREPARATION.md 2>/dev/null || true
echo "    ✓ Removido"

# 6. Remover imagens de exemplo
if [ -d "docs/assets/images/pdf_to_image_extraction" ]; then
    echo "  → Removendo imagens de exemplo..."
    rm -rf docs/assets/images/pdf_to_image_extraction/
    echo "    ✓ Removido"
else
    echo "  ⊘ Imagens de exemplo não encontradas"
fi

# 7. Limpar cache Python
echo "  → Limpando cache Python..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true
echo "    ✓ Cache limpo"

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  ✅ Limpeza concluída com sucesso!                             ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "📊 Espaço liberado: ~480MB"
echo ""
echo "⚠️  PRÓXIMOS PASSOS MANUAIS:"
echo ""
echo "  1. Revisar e limpar comandos de extração no Makefile:"
echo "     • check-poppler"
echo "     • prepare-data, prepare-data-test"
echo "     • gt-generate, gt-force, gt-stats"
echo "     • Seção 'Ground Truth Dataset' completa"
echo ""
echo "  2. Revisar dependências em pyproject.toml (opcional):"
echo "     • pdf2image (se não usado no curso)"
echo ""
echo "  3. Testar notebooks do curso:"
echo "     make jupyter"
echo ""
echo "  4. Commit das mudanças:"
echo "     git add -A"
echo "     git commit -m 'Removidos arquivos de extração migrados para dspy-data-extraction-optimization'"
echo ""

