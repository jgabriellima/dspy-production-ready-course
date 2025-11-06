# Production-Ready Multi-Agent Systems with DSPy

**Livro Técnico Completo sobre Sistemas Multi-Agente com DSPy**

---

## 📚 Sobre Este Diretório

Este é o diretório raiz do livro **"Production-Ready Multi-Agent Systems with DSPy: Cognitive Architectures, Optimization, and Real-World Patterns"**.

O livro está sendo construído usando **Jupyter Book** e contém 17 capítulos + 7 apêndices sobre como implementar sistemas multi-agent production-ready com DSPy.

---

## 🗂️ Estrutura

```
docs/
├── _config.yml                          # Configuração Jupyter Book
├── _toc.yml                             # Table of Contents
├── requirements.txt                      # Dependências
│
├── index.md                             # Landing page
├── prefacio.md                          # Prefácio
├── introducao.md                        # Introdução
├── como-usar-este-livro.md              # Guia de uso
├── recursos-adicionais.md               # Recursos
├── sobre-o-autor.md                     # Autor
│
├── parte-1-fundamentos/                 # PARTE 1 (3 capítulos)
│   ├── cap-01-enterprise-aos-agentes.ipynb
│   ├── cap-02-dspy-essentials-single-agent.ipynb
│   └── cap-03-primeiro-multiagent.ipynb
│
├── parte-2-arquiteturas/                # PARTE 2 (4 capítulos)
│   ├── cap-04-sequential-pipeline.ipynb
│   ├── cap-05-hierarchical.ipynb
│   ├── cap-06-collaborative-debate.ipynb
│   └── cap-07-reflexive-self-critique.ipynb
│
├── parte-3-otimizacao/                  # PARTE 3 (6 capítulos)
│   ├── cap-08-fundamentos-otimizacao.ipynb
│   ├── cap-09-bootstrap-mipro.ipynb
│   ├── cap-10-optimizers-customizados.ipynb
│   ├── cap-11-metricas-datasets-evaluation.ipynb
│   ├── cap-12-optimization-mastery.ipynb
│   └── cap-13-finetuning-multiagent.ipynb
│
├── parte-4-avancado/                    # PARTE 4 (4 capítulos)
│   ├── cap-14-arquiteturas-referencia-enterprise.ipynb
│   ├── cap-15-llmops-continuous-learning.ipynb
│   ├── cap-16-scaling-multiagent.ipynb
│   └── cap-17-case-studies-decision-framework.md
│
├── apendices/                           # APÊNDICES (7)
│   ├── apendice-a-api-reference.md
│   ├── apendice-b-deployment.md
│   ├── apendice-c-observability.md
│   ├── apendice-d-security.md
│   ├── apendice-e-troubleshooting.md
│   ├── apendice-f-bibliografia.md
│   └── apendice-g-glossario.md
│
├── codigo/                              # Código modular reutilizável
│   ├── architectures/
│   ├── optimizers/
│   ├── metrics/
│   ├── tools/
│   ├── finetuning/
│   ├── llmops/
│   └── utils/
│
├── assets/                              # Assets (imagens, diagramas)
│   ├── images/
│   └── diagrams/
│
└── [ARQUIVOS DE PLANEJAMENTO]           # Gestão do projeto
    ├── BOOK_OUTLINE.md
    ├── MAPEAMENTO_NOTEBOOKS.md
    ├── WRITING_GUIDE.md
    ├── KNOWLEDGE_GAPS.md
    ├── PROGRESS_TRACKER.md
    ├── RESEARCH_FINETUNING.md
    ├── RESEARCH_LLMOPS.md
    ├── REFERENCIAS_ACADEMICAS.md
    └── SESSAO_PROGRESSO.md
```

---

## 🚀 Quick Start

### 📍 PRIMEIRO ACESSO - COMECE AQUI:

1. **Leia o Status Real:**
   ```bash
   cat _planejamento/00-FONTE-DA-VERDADE.md
   ```

2. **Navegue pelo Índice Visual:**
   ```bash
   cat 00-INDICE-VISUAL.md
   ```

3. **Consulte as Diretrizes:**
   ```bash
   cat ../.cursorrules
   ```

### Desenvolvimento:

1. **Instalar Dependências:**
   ```bash
   cd docs/
   pip install -r requirements.txt
   ```

2. **Executar Notebooks:**
   ```bash
   jupyter lab
   ```

3. **Build do Livro:**
   ```bash
   jupyter-book build .
   ```
   
   O livro será gerado em `_build/html/index.html`.

---

## 📖 Conteúdo do Livro

### Parte 1: Fundamentos (3 capítulos)
- Cap 1: Do Enterprise aos Agentes Multi-Agent
- Cap 2: DSPy Essentials & Primeiro Single Agent
- Cap 3: Primeiro Sistema Multi-Agent

### Parte 2: Arquiteturas Cognitivas (4 capítulos)
- Cap 4: Sequential/Pipeline Architecture
- Cap 5: Hierarchical Architecture
- Cap 6: Collaborative/Debate Architecture
- Cap 7: Reflexive/Self-Critique Architecture

### Parte 3: Otimização & Fine-Tuning (6 capítulos)
- Cap 8: Fundamentos de Otimização Multi-Agent
- Cap 9: BootstrapFewShot & MIPRO
- Cap 10: Optimizers Customizados
- Cap 11: Métricas, Datasets e Evaluation
- Cap 12: Optimization Mastery
- Cap 13: Fine-Tuning Multi-Agent Systems

### Parte 4: Enterprise & Production (4 capítulos)
- Cap 14: Arquiteturas de Referência Enterprise
- Cap 15: LLMOps & Continuous Learning
- Cap 16: Scaling Multi-Agent Systems
- Cap 17: Case Studies & Decision Framework

---

## 🛠️ Desenvolvimento

### Status Atual

Ver: `_planejamento/05-PROGRESS-TRACKER.md` para status detalhado de cada capítulo.

**Progresso Geral:** ~12% completo

**Completo:**
- ✅ Estrutura completa (17 capítulos + 7 apêndices)
- ✅ Sistema de planejamento e tracking
- ✅ Cap 2: 50% → material pronto para finalizar
- ✅ Cap 4: 40% → teoria + setup completos

**Próximo:** Completar Cap 2 e Cap 4

### Workflow

1. **Modelar** notebooks existentes (`notebooks/`)
2. **Criar** notebooks novos conforme necessário
3. **Testar** cada notebook célula por célula
4. **Revisar** para garantir qualidade
5. **Integrar** com livro completo

### Arquivos de Planejamento

📁 **`_planejamento/`** (todos arquivos de gestão):
- **`00-FONTE-DA-VERDADE.md`:** 📍 **STATUS REAL - COMECE AQUI**
- **`01-BOOK-OUTLINE.md`:** Estrutura completa do livro
- **`02-MAPEAMENTO-NOTEBOOKS.md`:** Fonte → Destino
- **`03-WRITING-GUIDE.md`:** Convenções e estilo
- **`04-KNOWLEDGE-GAPS.md`:** Conceitos a explicar
- **`05-PROGRESS-TRACKER.md`:** Status por capítulo
- **`06/07-RESEARCH-*.md`:** Planos de research
- **`08-REFERENCIAS-ACADEMICAS.md`:** Bibliografia
- **`99-SESSAO-PROGRESSO.md`:** Última sessão

🔧 **`.cursorrules`** (raiz do projeto): Diretrizes completas

---

## 🎯 Princípios do Livro

1. **Técnico e Honesto:** Sem sensacionalismo, trade-offs explícitos
2. **Hands-On:** Código funcional e testável
3. **Didático:** Narrativa progressiva, conceitos explicados
4. **Production-Ready:** Além de "hello world", foco em produção

---

## 🤝 Contribuindo

### Como Contribuir

1. **Reportar erros:** GitHub Issues
2. **Sugerir melhorias:** GitHub Discussions
3. **Corrigir código:** Pull Requests
4. **Melhorar explicações:** PRs bem-vindos

### Guidelines

- Seguir `WRITING_GUIDE.md` para convenções
- Testar todo código antes de commitar
- Adicionar referências quando necessário
- Manter consistência com estilo existente

---

## 📝 Licença

Creative Commons BY-NC-SA 4.0

Ver: LICENSE file na raiz do repositório.

---

## 📞 Contato

- **GitHub:** https://github.com/joaogabriellima/ai_materials
- **Issues:** https://github.com/joaogabriellima/ai_materials/issues
- **Discussions:** https://github.com/joaogabriellima/ai_materials/discussions

---

## 🎓 Citação

Se usar este livro em pesquisa ou trabalho acadêmico:

```bibtex
@book{lima2025multiagent,
  title={Production-Ready Multi-Agent Systems with DSPy: Cognitive Architectures, Optimization, and Real-World Patterns},
  author={Lima, João Gabriel},
  year={2025},
  publisher={Self-published},
  url={https://github.com/joaogabriellima/ai_materials}
}
```

---

**Status:** Em desenvolvimento ativo 🚧

**Última atualização:** 05 de Novembro de 2025  
**Versão:** 0.12 (12% completo)

---

*"The best way to learn is to teach."* — Richard Feynman

