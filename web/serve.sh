#!/bin/bash

# Script para servir a landing page localmente

echo "🚀 Iniciando servidor local para DSPy Course Landing Page..."
echo ""
echo "📍 URL: http://localhost:8000"
echo "⏹️  Para parar: Pressione Ctrl+C"
echo ""

# Verifica se Python 3 está instalado
if command -v python3 &> /dev/null; then
    cd "$(dirname "$0")"
    python3 -m http.server 8000
else
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3 ou use outro método."
    echo ""
    echo "Alternativas:"
    echo "  - npx serve"
    echo "  - php -S localhost:8000"
    exit 1
fi


