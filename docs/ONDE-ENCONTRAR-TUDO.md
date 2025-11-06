# 🗺️ ONDE ENCONTRAR TUDO - Guia Rápido de Navegação

**Última atualização:** 05 de Novembro de 2025

---

## 📍 ARQUIVOS PRINCIPAIS (COMECE AQUI)

### 1. Fonte da Verdade (STATUS DO PROJETO)
```
📄 docs/_planejamento/00-FONTE-DA-VERDADE.md
```
**O QUE É:** Status real de todos os capítulos, progresso, próximos passos
**QUANDO USAR:** Sempre, antes de fazer qualquer coisa

### 2. Índice Visual (NAVEGAÇÃO)
```
📄 docs/00-INDICE-VISUAL.md
```
**O QUE É:** Mapa visual do livro, estrutura, navegação
**QUANDO USAR:** Para navegar pelo projeto

### 3. Cursor Rules (GUIA DE DESENVOLVIMENTO)
```
📄 .cursorrules
```
**O QUE É:** Convenções, tom, estilo, regras do projeto
**QUANDO USAR:** Durante desenvolvimento, escrita, revisão

---

## 📚 CAPÍTULOS DO LIVRO

### ✅ COMPLETOS (100%)

**Cap 2: DSPy Essentials & Single Agent**
```
📄 docs/parte-1-fundamentos/cap-02-COMPLETO.md (1100 linhas)
```
- Teoria DSPy completa
- ReAct Agent implementation
- Testes simples e complexos
- Análise de limitações
- Pronto para converter em notebook

**Cap 4: Sequential/Pipeline Architecture**
```
📄 docs/parte-2-arquiteturas/04-CONTEUDO-CAP-04-SEQUENTIAL.md (1100 linhas)
```
- Teoria multi-agent
- 4 agentes em pipeline
- Testes e comparações
- Pronto para converter em notebook

---

### ✅ ESTRUTURADOS (Prontos para Expansão)

**Caps 1, 3 (Fundamentos):**
```
📄 docs/CONTEUDO-BATCH-CAPS-1-3-14-17.md
```
- Cap 1: Enterprise aos Agentes
- Cap 3: Primeiro Multi-Agent

**Caps 5, 6, 7 (Arquiteturas):**
```
📄 docs/CONTEUDO-BATCH-CAPS-5-6-7.md
```
- Cap 5: Hierarchical
- Cap 6: Collaborative/Debate
- Cap 7: Reflexive/Self-Critique

**Caps 8-13 (Otimização):**
```
📁 docs/parte-3-otimizacao/
   ├── cap-08-fundamentos-otimizacao-multiagent.md (8.7KB)
   ├── cap-09-bootstrap-fewshot-mipro.md (8.5KB)
   ├── cap-10-optimizers-customizados.md (2.1KB)
   ├── cap-11-metricas-datasets-evaluation.md (1.4KB)
   ├── cap-12-optimization-mastery.md (1.1KB)
   └── cap-13-finetuning-multiagent.md (1.7KB + Research)
```

**Caps 14-17 (Enterprise):**
```
📁 docs/parte-4-avancado/
   ├── cap-14-arquiteturas-referencia-enterprise.md (2.7KB)
   ├── cap-15-llmops-continuous-learning.md (2.7KB + Research)
   ├── cap-16-scaling-multiagent.md (2.2KB)
   └── cap-17-case-studies-decision-framework.md (2.7KB)
```

---

## 📋 PLANEJAMENTO E DOCS

```
📁 docs/_planejamento/
   ├── 00-FONTE-DA-VERDADE.md           ⭐ STATUS REAL
   ├── 01-BOOK-OUTLINE.md               (Estrutura do livro)
   ├── 02-MAPEAMENTO-NOTEBOOKS.md       (Notebooks → Capítulos)
   ├── 03-WRITING-GUIDE.md              (Convenções PT/EN)
   ├── 04-KNOWLEDGE-GAPS.md             (Conceitos a explicar)
   ├── 05-PROGRESS-TRACKER.md           (Progresso detalhado)
   ├── 06-RESEARCH-FINETUNING.md        (Research Cap 13)
   ├── 07-RESEARCH-LLMOPS.md            (Research Cap 15)
   ├── 08-REFERENCIAS-ACADEMICAS.md     (Bibliografia)
   └── 99-SESSAO-PROGRESSO.md           (Sessão atual)
```

---

## 📄 SUMÁRIOS E RELATÓRIOS

**Progresso Geral:**
```
📄 docs/MISSAO-COMPLETA-TODOS-CAPITULOS.md
```
- Resumo de tudo que foi feito
- Conteúdo de cada capítulo
- Métricas e estatísticas

**Pastas Preenchidas:**
```
📄 docs/PASTAS-PREENCHIDAS-COMPLETO.md
```
- Como resolvemos o problema das pastas vazias
- Estrutura final do projeto

**Este Arquivo:**
```
📄 docs/ONDE-ENCONTRAR-TUDO.md
```
- Guia de navegação rápida

---

## 🔍 COMO ENCONTRAR...

### "Quero ver o status real do projeto"
→ `docs/_planejamento/00-FONTE-DA-VERDADE.md`

### "Quero começar a escrever um capítulo"
→ Consultar `.cursorrules` primeiro
→ Depois `_planejamento/03-WRITING-GUIDE.md`

### "Quero ver um capítulo completo de exemplo"
→ `parte-1-fundamentos/cap-02-COMPLETO.md` OU
→ `parte-2-arquiteturas/04-CONTEUDO-CAP-04-SEQUENTIAL.md`

### "Quero expandir um capítulo estruturado"
→ **Caps 8-13:** `parte-3-otimizacao/cap-XX-*.md`
→ **Caps 14-17:** `parte-4-avancado/cap-XX-*.md`
→ **Caps 1,3,5-7:** Batch files em `docs/`

### "Quero saber de qual notebook extrair"
→ `_planejamento/02-MAPEAMENTO-NOTEBOOKS.md`

### "Quero adicionar referências acadêmicas"
→ `_planejamento/08-REFERENCIAS-ACADEMICAS.md`

### "Quero saber o que pesquisar sobre fine-tuning"
→ `_planejamento/06-RESEARCH-FINETUNING.md`

### "Quero saber o que pesquisar sobre LLMOps"
→ `_planejamento/07-RESEARCH-LLMOPS.md`

---

## 🎯 WORKFLOW RECOMENDADO

### Para Continuar o Livro:

1. **Ler status atual:**
   ```
   cat docs/_planejamento/00-FONTE-DA-VERDADE.md
   ```

2. **Escolher próximo capítulo:**
   - Ver "Próximos Passos" na Fonte da Verdade
   - Decidir: Expandir estruturado OU Converter Cap 2/4

3. **Consultar guias:**
   ```
   cat .cursorrules
   cat docs/_planejamento/03-WRITING-GUIDE.md
   ```

4. **Trabalhar no capítulo:**
   - Usar estrutura existente como base
   - Seguir convenções PT/EN
   - Adicionar código testável
   - Incluir referências

5. **Atualizar status:**
   ```
   # Sempre atualizar:
   docs/_planejamento/00-FONTE-DA-VERDADE.md
   docs/_planejamento/05-PROGRESS-TRACKER.md
   ```

---

## 📊 ESTRUTURA COMPLETA

```
ai_materials/
│
├── .cursorrules                    ⭐ GUIA PRINCIPAL
│
├── notebooks/                      (Fontes originais)
│   ├── dspy_agents_basic_handson_final.ipynb
│   ├── dspy_multiagent_cognitive_architectures.ipynb
│   ├── dspy_multiagent_optimization.ipynb
│   ├── dspy_optimization_mastery.ipynb
│   └── dspy_tool_use_enterprise.ipynb
│
└── docs/                           (LIVRO)
    │
    ├── 00-INDICE-VISUAL.md         ⭐ NAVEGAÇÃO
    ├── ONDE-ENCONTRAR-TUDO.md      ⭐ ESTE ARQUIVO
    │
    ├── _planejamento/              ⭐ PLANEJAMENTO
    │   ├── 00-FONTE-DA-VERDADE.md  ⭐⭐⭐ STATUS REAL
    │   ├── 01-BOOK-OUTLINE.md
    │   ├── 02-MAPEAMENTO-NOTEBOOKS.md
    │   ├── 03-WRITING-GUIDE.md
    │   ├── 04-KNOWLEDGE-GAPS.md
    │   ├── 05-PROGRESS-TRACKER.md
    │   ├── 06-RESEARCH-FINETUNING.md
    │   ├── 07-RESEARCH-LLMOPS.md
    │   ├── 08-REFERENCIAS-ACADEMICAS.md
    │   └── 99-SESSAO-PROGRESSO.md
    │
    ├── parte-1-fundamentos/        ✅ 2 arquivos
    │   └── cap-02-COMPLETO.md      (100%)
    │
    ├── parte-2-arquiteturas/       ✅ 2 arquivos
    │   └── 04-CONTEUDO-CAP-04-*.md (100%)
    │
    ├── parte-3-otimizacao/         ✅ 6 arquivos
    │   ├── cap-08-*.md
    │   ├── cap-09-*.md
    │   ├── cap-10-*.md
    │   ├── cap-11-*.md
    │   ├── cap-12-*.md
    │   └── cap-13-*.md
    │
    ├── parte-4-avancado/           ✅ 4 arquivos
    │   ├── cap-14-*.md
    │   ├── cap-15-*.md
    │   ├── cap-16-*.md
    │   └── cap-17-*.md
    │
    ├── CONTEUDO-BATCH-CAPS-5-6-7.md
    ├── CONTEUDO-BATCH-CAPS-8-13.md
    ├── CONTEUDO-BATCH-CAPS-1-3-14-17.md
    ├── MISSAO-COMPLETA-TODOS-CAPITULOS.md
    └── PASTAS-PREENCHIDAS-COMPLETO.md
```

---

## 🎉 STATUS FINAL

✅ **Todos os 17 capítulos têm conteúdo**
✅ **Todas as pastas preenchidas**
✅ **Fonte da Verdade atualizada**
✅ **Guias e documentação completos**
✅ **Progresso: 55%**

**Pronto para:**
- Expandir capítulos estruturados
- Converter markdowns em notebooks
- Fazer research (Caps 13 e 15)
- Build MVP do livro

---

**SEMPRE COMECE PELA FONTE DA VERDADE:** `docs/_planejamento/00-FONTE-DA-VERDADE.md` 📍
