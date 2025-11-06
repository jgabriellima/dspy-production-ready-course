# Capítulo 13: Fine-Tuning Multi-Agent Systems

**Status:** ✅ Estrutura completa + ⚠️ RESEARCH NEEDED
**Research:** Ver `docs/_planejamento/06-RESEARCH-FINETUNING.md`

## Conceito Principal
Quando otimização de prompts não basta: fine-tune o LLM base.

## Por que Fine-Tune?
- Otimização de prompts: melhora até certo ponto (plateau)
- Fine-tuning: melhora weights do modelo
- **Quando?**
  - Dataset grande e específico (1000+ exemplos)
  - Budget para treinar
  - Performance crítica
  - Diferencial competitivo

## DSPy + Fine-Tuning (RESEARCH NEEDED)

```python
# PLACEHOLDER - REQUER RESEARCH
from dspy.finetuning import export_for_finetuning

# Coletar traces
traces = []
for example in trainset:
    trace = pipeline(example.query, trace=True)
    traces.append(trace)

# Exportar para formato de fine-tuning
finetuning_dataset = export_for_finetuning(traces)

# Fine-tune (OpenAI, HuggingFace, etc)
# ... DETAILS TO BE RESEARCHED ...
```

## Estratégias Multi-Agent
1. **Fine-tune cada agente:** Separadamente
2. **Fine-tune modelo único:** Para todos agentes
3. **Fine-tune só críticos:** Bottleneck agents

## Workflow Prático
```
1. Otimização de prompts (BootstrapFewShot/MIPRO)
2. Deploy em produção
3. Coletar traces (Langfuse)
4. Criar dataset de fine-tuning
5. Fine-tune modelo(s)
6. Re-deploy
7. Monitorar
8. Iterar
```

## Tools & Platforms (RESEARCH)
- OpenAI fine-tuning API
- Hugging Face Transformers
- DSPy integrations? (TO BE RESEARCHED)
- Custom training loops

## Key Takeaways
- Fine-tuning é o próximo nível após otimização
- Requer investimento (data, compute, expertise)
- ROI pode ser alto em produção
- Integração com DSPy ainda sendo explorada

**Status:** Estrutura completa, research pending ✅⚠️
