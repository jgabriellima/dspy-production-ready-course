# Proposta de Limpeza do Projeto

Após migração do projeto de extração de dados para `dspy-data-extraction-optimization`, os seguintes itens podem ser removidos do projeto `dspy-production-ready-course`.

## Resumo Executivo

- **Total estimado para remoção**: ~474MB
- **Itens**: 13 arquivos/diretórios
- **Impacto**: Nenhum (já migrados para novo projeto)

---

## 1. DIRETÓRIO data/ COMPLETO (474MB)

**Ação**: REMOVER INTEIRO

```bash
rm -rf data/
```

**Conteúdo**:
- `data/pdfs/` - 91 PDFs de termos de convênio
- `data/images/` - 223 imagens JPG extraídas dos PDFs
- `data/ground_truth/` - Ground truth dataset (se gerado)
- `data/GROUND_TRUTH_README.md` - Documentação

**Justificativa**: 
- Já copiado para `dspy-data-extraction-optimization/data/`
- Específico do projeto de extração de dados
- Não relacionado ao curso de DSPy Multi-Agent
- Ocupa 474MB de espaço

**Status**: ✅ SEGURO REMOVER

---

## 2. SCRIPTS DE EXTRAÇÃO DE DADOS

**Ação**: REMOVER

```bash
rm -rf scripts/
```

**Conteúdo**:
- `scripts/data_preparation.py` - Script de conversão PDF→Imagem
- `scripts/generate_ground_truth.py` - Script de geração de ground truth
- `scripts/README_DATA_PREPARATION.md` - Documentação

**Justificativa**:
- Scripts copiados para `dspy-data-extraction-optimization/scripts/`
- Específicos do projeto de extração
- Não fazem parte do curso

**Status**: ✅ SEGURO REMOVER

---

## 3. NOTEBOOK DE EXTRAÇÃO DE DADOS

**Ação**: REMOVER

```bash
rm notebooks/dspy_data_extraction_optimization.ipynb
```

**Justificativa**:
- Copiado para `dspy-data-extraction-optimization/notebooks/`
- Específico do projeto de extração
- Não faz parte do conteúdo do curso

**Status**: ✅ SEGURO REMOVER

---

## 4. ARQUIVOS DE RESULTADO DA EXTRAÇÃO

**Ação**: REMOVER

```bash
rm notebooks/result.extracted_data-google.json
rm notebooks/result.extracted_data-groq.json
rm notebooks/OTIMIZACAO_GROQ_MIPROV2.md
```

**Justificativa**:
- Arquivos de teste/resultado do projeto de extração
- Não necessários para o curso
- Provavelmente obsoletos

**Status**: ✅ SEGURO REMOVER

---

## 5. DOCUMENTAÇÃO DE EXTRAÇÃO DE DADOS

**Ação**: REMOVER

```bash
rm WORKFLOW_OTIMIZACAO.md
rm docs/DATA_PREPARATION.md
```

**Justificativa**:
- Documentação copiada para `dspy-data-extraction-optimization/docs/`
- Específica do projeto de extração
- Não faz parte da documentação do curso

**Status**: ✅ SEGURO REMOVER

---

## 6. IMAGENS DE EXEMPLO EM docs/assets/

**Ação**: REMOVER

```bash
rm -rf docs/assets/images/pdf_to_image_extraction/
```

**Conteúdo**:
- 12 imagens JPG de exemplo (TERMO CONVENIO 169-2022)

**Justificativa**:
- Usadas APENAS no notebook `dspy_data_extraction_optimization.ipynb`
- Como o notebook será removido, as imagens não são mais necessárias
- Específicas do projeto de extração

**Status**: ✅ SEGURO REMOVER
- ✅ Verificado: Referências encontradas apenas no notebook de extração

---

## 7. COMANDOS DO MAKEFILE

**Ação**: REMOVER COMANDOS (não o arquivo inteiro)

**Comandos a remover**:
- `check-poppler`
- `prepare-data`
- `prepare-data-test`
- `data-preparation`
- `check-gemini-key`
- `gt-generate` / `generate-ground-truth`
- `gt-force` / `generate-ground-truth-force`
- `gt-stats` / `ground-truth-stats`

**Justificativa**:
- Comandos específicos do projeto de extração
- Já estão no Makefile do novo projeto
- Não necessários para o curso

**Status**: ✅ SEGURO REMOVER

---

## 8. DEPENDÊNCIAS EM pyproject.toml

**Ação**: REVISAR DEPENDÊNCIAS (opcional)

**Dependências que podem ser removidas** (se não usadas no curso):
- `pdf2image` - Conversão PDF para imagem (específica de extração)
- `toons` - Visualização de JSON (pode ser útil no curso)

**Status**: ⚠️ REVISAR
- Verificar se notebooks do curso usam estas libs
- Manter se usadas, remover se não

---

## NOTEBOOKS QUE DEVEM PERMANECER

✅ **MANTER** (parte do curso de DSPy Multi-Agent):
- `notebooks/dspy_agents_advanced_handson_final.ipynb`
- `notebooks/dspy_memory_react_agent.ipynb`
- `notebooks/dspy_multiagent_cognitive_architectures.ipynb`
- `notebooks/dspy_multiagent_optimization.ipynb`
- `notebooks/dspy_optimization_mastery.ipynb`
- `notebooks/dspy_vision_language_models.ipynb`
- `notebooks/multiagent_code_examples.py`
- `notebooks/saved_models/` (modelos treinados do curso)

---

## ARQUIVOS QUE DEVEM PERMANECER

✅ **MANTER** (estrutura do projeto do curso):
- `README.md`
- `pyproject.toml`
- `Makefile` (após limpar comandos de extração)
- `uv.lock`
- `main.py`
- `helpers/`
- `services/`
- `docs/requirements.txt` (se usado pelo curso)

---

## SCRIPT DE LIMPEZA AUTOMÁTICA

```bash
#!/bin/bash
# cleanup.sh - Script para limpar projeto após migração

set -e

echo "🧹 Limpando projeto dspy-production-ready-course..."
echo ""

# 1. Remover data/ completo
echo "Removendo data/ (474MB)..."
rm -rf data/

# 2. Remover scripts/
echo "Removendo scripts/..."
rm -rf scripts/

# 3. Remover notebook de extração
echo "Removendo notebook de extração..."
rm -f notebooks/dspy_data_extraction_optimization.ipynb

# 4. Remover arquivos de resultado
echo "Removendo arquivos de resultado..."
rm -f notebooks/result.extracted_data-google.json
rm -f notebooks/result.extracted_data-groq.json
rm -f notebooks/OTIMIZACAO_GROQ_MIPROV2.md

# 5. Remover documentação de extração
echo "Removendo documentação de extração..."
rm -f WORKFLOW_OTIMIZACAO.md
rm -f docs/DATA_PREPARATION.md

# 6. Remover imagens de exemplo
echo "Removendo imagens de exemplo..."
rm -rf docs/assets/images/pdf_to_image_extraction/

echo ""
echo "✅ Limpeza concluída!"
echo ""
echo "📊 Espaço liberado: ~474MB"
echo ""
echo "⚠️  PRÓXIMOS PASSOS:"
echo "  1. Revisar Makefile e remover comandos de extração"
echo "  2. Verificar se imagens em docs/assets/ são usadas"
echo "  3. Revisar dependências em pyproject.toml"
echo "  4. Testar notebooks do curso"
echo ""
```

---

## CHECKLIST DE EXECUÇÃO

Executar nesta ordem:

```
[ ] 1. Fazer backup do projeto (git commit ou cp -r)
[ ] 2. Confirmar que novo projeto está funcionando
[ ] 3. Buscar referências às imagens em docs/assets/
[ ] 4. Executar script de limpeza (ou comandos manuais)
[ ] 5. Limpar comandos do Makefile
[ ] 6. Revisar dependências em pyproject.toml
[ ] 7. Executar make clean
[ ] 8. Testar notebooks do curso
[ ] 9. Commit das mudanças
[ ] 10. Celebrar! 🎉
```

---

## IMPACTO DA LIMPEZA

### Antes
```
dspy-production-ready-course/
├── data/                    # 474MB - DADOS DE EXTRAÇÃO
├── scripts/                 # Scripts de extração
├── notebooks/               # Inclui notebook de extração
├── WORKFLOW_OTIMIZACAO.md  # Doc de extração
└── ... (curso)
```

### Depois
```
dspy-production-ready-course/
├── notebooks/               # Apenas notebooks do curso
├── helpers/
├── services/
├── docs/                    # Apenas docs do curso
└── ... (estrutura do curso)
```

### Benefícios
- ✅ **474MB de espaço liberado**
- ✅ **Projeto focado apenas no curso**
- ✅ **Menos confusão sobre o que é o quê**
- ✅ **Makefile mais limpo**
- ✅ **Separação clara de responsabilidades**

---

## RESUMO DE REMOÇÕES

| Item | Tipo | Tamanho | Status |
|------|------|---------|--------|
| data/ | Diretório | 474MB | ✅ Remover |
| scripts/ | Diretório | <1MB | ✅ Remover |
| dspy_data_extraction_optimization.ipynb | Arquivo | <1MB | ✅ Remover |
| result.extracted_data-*.json | Arquivos | <1MB | ✅ Remover |
| OTIMIZACAO_GROQ_MIPROV2.md | Arquivo | <1MB | ✅ Remover |
| WORKFLOW_OTIMIZACAO.md | Arquivo | <1MB | ✅ Remover |
| DATA_PREPARATION.md | Arquivo | <1MB | ✅ Remover |
| docs/assets/images/pdf_to_image_extraction/ | Diretório | <10MB | ✅ Remover |
| Comandos Makefile | Comandos | - | ✅ Remover |

**Total**: ~480MB liberados

---

**Última atualização**: Novembro 2025  
**Status**: Aguardando revisão e aprovação

