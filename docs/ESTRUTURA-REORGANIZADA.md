# ✅ ESTRUTURA REORGANIZADA - docs/

## 🎯 OBJETIVO

Reorganização completa com **numeração clara** para fácil identificação.

---

## 📊 ANTES vs DEPOIS

### ❌ ANTES (Confuso):
```
docs/
├── prefacio.md                    ← Sem ordem
├── introducao.md                  ← Sem ordem
├── BOOK_OUTLINE.md                ← Misturado com conteúdo
├── MAPEAMENTO_NOTEBOOKS.md        ← Misturado
├── WRITING_GUIDE.md               ← Misturado
├── ... (todos misturados)
```

### ✅ AGORA (Organizado):
```
docs/
│
├── 00-INDICE-VISUAL.md            ← 📍 COMECE AQUI!
├── 01-prefacio.md                 ← Numerado
├── 02-introducao.md               ← Numerado
├── 03-como-usar-este-livro.md     ← Numerado
│
├── _planejamento/                 ← SEPARADO! Gestão aqui
│   ├── README-PLANEJAMENTO.md     ← Guia desta pasta
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
├── parte-1-fundamentos/
│   ├── cap-02-dspy-essentials-single-agent.ipynb  (50% pronto)
│   └── 02-CONTEUDO-RESTANTE-PARA-ADICIONAR.md     (material para copiar)
│
├── 98-recursos-adicionais.md      ← Numerado
├── 99-sobre-o-autor.md            ← Numerado
│
└── [outras pastas e configs]
```

---

## 🗺️ NAVEGAÇÃO RÁPIDA

### Para TRABALHAR no livro:
```bash
cd docs/
cat 00-INDICE-VISUAL.md           # Ver estrutura geral
cd parte-1-fundamentos/            # Ir para capítulos
```

### Para VER PLANEJAMENTO:
```bash
cd docs/_planejamento/
cat README-PLANEJAMENTO.md         # Ver o que tem aqui
cat 05-PROGRESS-TRACKER.md         # Ver progresso
```

### Para COMPLETAR Cap 2:
```bash
cd docs/parte-1-fundamentos/
# 1. Abrir: cap-02-dspy-essentials-single-agent.ipynb (notebook)
# 2. Ver: 02-CONTEUDO-RESTANTE-PARA-ADICIONAR.md (material)
# 3. Copiar conteúdo do arquivo .md para o notebook
```

---

## 📋 SISTEMA DE NUMERAÇÃO

### Arquivos Principais (raiz docs/):
- `00-*` → Índices e guias
- `01-03` → Front matter (prefácio, intro, como usar)
- `04-96` → [reservado para capítulos se necessário]
- `98-99` → Back matter (recursos, autor)

### Planejamento (_planejamento/):
- `01-08` → Documentos de planejamento
- `99` → Status atual/temporário

### Capítulos (parte-X-*/):
- `cap-XX-*.ipynb` → Notebooks dos capítulos
- `XX-*.md` → Arquivos auxiliares do capítulo

---

## ✅ BENEFÍCIOS DA REORGANIZAÇÃO

1. **✨ Clareza:** Numeração mostra ordem
2. **📁 Separação:** Planejamento separado de conteúdo
3. **🔍 Fácil encontrar:** Nomes descritivos + números
4. **📊 Visual:** `00-INDICE-VISUAL.md` mostra tudo
5. **🎯 Focado:** Trabalha em conteúdo sem distração

---

## 🎯 PRÓXIMOS PASSOS

1. **Ver estrutura:** `00-INDICE-VISUAL.md`
2. **Completar Cap 2:**
   - Abrir `parte-1-fundamentos/cap-02-*.ipynb`
   - Copiar de `parte-1-fundamentos/02-CONTEUDO-RESTANTE-*.md`
3. **Ver progresso:** `_planejamento/05-PROGRESS-TRACKER.md`

---

## 📝 ARQUIVOS IMPORTANTES

| Arquivo | Função | Quando Usar |
|---------|--------|-------------|
| `00-INDICE-VISUAL.md` | Mapa da estrutura | Para navegar |
| `_planejamento/01-BOOK-OUTLINE.md` | Estrutura do livro | Ver outline |
| `_planejamento/05-PROGRESS-TRACKER.md` | Status | Ver progresso |
| `_planejamento/03-WRITING-GUIDE.md` | Convenções | Ao escrever |

---

**Status:** ✅ Reorganização completa!

**Próximo:** Completar Cap 2 usando o material em `02-CONTEUDO-RESTANTE-PARA-ADICIONAR.md`

