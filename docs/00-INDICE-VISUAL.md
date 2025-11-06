# 📚 ÍNDICE VISUAL - Organização do Livro

**Última atualização:** Janeiro 2025

---

## 🎯 COMO NAVEGAR

### 📍 SEMPRE COMECE AQUI:
👉 **`_planejamento/00-FONTE-DA-VERDADE.md`** ← STATUS REAL DO PROJETO

### Para ESCREVER o livro:
👉 Vá para as pastas `parte-X-*` e trabalhe nos capítulos

### Para PLANEJAR/GERENCIAR:
👉 Vá para `_planejamento/` e consulte os documentos de gestão

### Para CONFIGURAR:
👉 Use `_config.yml` e `_toc.yml`

---

## 📖 ESTRUTURA DO LIVRO (Conteúdo)

```
docs/
│
├── 00-index.md                          ← Landing page
├── 01-prefacio.md                       ← Prefácio
├── 02-introducao.md                     ← Introdução geral
├── 03-como-usar-este-livro.md           ← Guia de uso
│
├── parte-1-fundamentos/                 ← PARTE 1 (3 capítulos)
│   ├── cap-01-*.ipynb                   📝 A criar
│   ├── cap-02-*.ipynb                   🟡 50% pronto
│   └── cap-03-*.ipynb                   📝 A criar
│
├── parte-2-arquiteturas/                ← PARTE 2 (4 capítulos)
│   ├── cap-04-*.ipynb                   📝 A modelar
│   ├── cap-05-*.ipynb                   📝 A modelar
│   ├── cap-06-*.ipynb                   📝 A modelar
│   └── cap-07-*.ipynb                   📝 A modelar
│
├── parte-3-otimizacao/                  ← PARTE 3 (6 capítulos)
│   ├── cap-08-*.ipynb                   📝 A modelar
│   ├── cap-09-*.ipynb                   📝 A modelar
│   ├── cap-10-*.ipynb                   📝 A modelar
│   ├── cap-11-*.ipynb                   📝 A modelar
│   ├── cap-12-*.ipynb                   📝 A modelar
│   └── cap-13-*.ipynb                   📝 A criar + research
│
├── parte-4-avancado/                    ← PARTE 4 (4 capítulos)
│   ├── cap-14-*.ipynb                   📝 A modelar
│   ├── cap-15-*.ipynb                   📝 A criar + research
│   ├── cap-16-*.ipynb                   📝 A criar
│   └── cap-17-*.md                      📝 A criar
│
├── apendices/                           ← APÊNDICES (7)
│   ├── apendice-a-*.md                  📝 A criar
│   ├── apendice-b-*.md                  📝 A criar
│   ├── apendice-c-*.md                  📝 A criar
│   ├── apendice-d-*.md                  📝 A criar
│   ├── apendice-e-*.md                  📝 A criar
│   ├── apendice-f-*.md                  📝 A criar
│   └── apendice-g-*.md                  📝 A criar
│
├── 98-recursos-adicionais.md            ← Recursos extras
├── 99-sobre-o-autor.md                  ← Biografia
│
└── codigo/                              ← Código modular reutilizável
    ├── architectures/
    ├── optimizers/
    ├── metrics/
    ├── tools/
    ├── finetuning/
    ├── llmops/
    └── utils/
```

---

## 🗂️ PLANEJAMENTO E GESTÃO

```
docs/_planejamento/
│
├── 00-FONTE-DA-VERDADE.md               ← 📍 STATUS REAL (COMECE AQUI!)
├── 01-BOOK-OUTLINE.md                   ← Estrutura completa do livro
├── 02-MAPEAMENTO-NOTEBOOKS.md           ← Fonte → Destino
├── 03-WRITING-GUIDE.md                  ← Convenções PT/EN
├── 04-KNOWLEDGE-GAPS.md                 ← Conceitos a explicar
├── 05-PROGRESS-TRACKER.md               ← Status por capítulo
├── 06-RESEARCH-FINETUNING.md            ← Research Cap 13
├── 07-RESEARCH-LLMOPS.md                ← Research Cap 15
├── 08-REFERENCIAS-ACADEMICAS.md         ← Bibliografia
└── 99-SESSAO-PROGRESSO.md               ← Progresso última sessão
```

---

## ⚙️ CONFIGURAÇÃO

```
docs/
│
├── _config.yml                          ← Config Jupyter Book
├── _toc.yml                             ← Table of Contents
├── requirements.txt                     ← Dependências
├── README.md                            ← Documentação geral
└── CHANGELOG.md                         ← Histórico de versões
```

---

## 📊 PROGRESSO ATUAL

**Progresso Geral:** ~8%

```
✅ Planejamento:        100%
🟡 Cap 2:                50%
📝 Demais capítulos:      0%
```

---

## 🎯 QUICK START

### Ver progresso:
```bash
cat _planejamento/05-PROGRESS-TRACKER.md
```

### Trabalhar em capítulo:
```bash
cd parte-1-fundamentos/
jupyter lab cap-02-*.ipynb
```

### Ver plano geral:
```bash
cat _planejamento/01-BOOK-OUTLINE.md
```

### Build do livro:
```bash
jupyter-book build .
```

---

## 📝 CONVENÇÕES DE NOMENCLATURA

### Notebooks (Capítulos):
```
cap-XX-nome-descritivo.ipynb
```

Exemplo: `cap-02-dspy-essentials-single-agent.ipynb`

### Arquivos Auxiliares:
```
XX-NOME-DESCRITIVO.md
```

Exemplo: `02-CONTEUDO-RESTANTE-PARA-ADICIONAR.md`

### Planejamento:
```
XX-NOME-ARQUIVO.md
```

Onde XX = ordem (01, 02, ..., 99)

---

## 🆘 PRECISA DE AJUDA?

- **📍 STATUS REAL:** `_planejamento/00-FONTE-DA-VERDADE.md` ← **SEMPRE COMECE AQUI**
- **Ver estrutura:** Este arquivo (`00-INDICE-VISUAL.md`)
- **Ver progresso:** `_planejamento/05-PROGRESS-TRACKER.md`
- **Ver outline:** `_planejamento/01-BOOK-OUTLINE.md`
- **Ver convenções:** `_planejamento/03-WRITING-GUIDE.md`
- **Cursor Rules:** `.cursorrules` (raiz do projeto)

---

**Última sessão:** Cap 2 50% completo
**Próximo:** Completar Cap 2 com conteúdo de `parte-1-fundamentos/02-CONTEUDO-RESTANTE-PARA-ADICIONAR.md`

