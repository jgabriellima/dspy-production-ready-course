# Capítulo 15: LLMOps & Continuous Learning

**Status:** ✅ Estrutura completa + ⚠️ RESEARCH NEEDED
**Research:** Ver `docs/_planejamento/07-RESEARCH-LLMOPS.md`

## Conceito Principal
Production feedback loop: Traces → Datasets → Re-optimization → Fine-tuning

## LLMOps ≠ MLOps
- MLOps: Modelos tradicionais (features fixas)
- LLMOps: LLMs + Agents + Prompts (muda constantemente)
- **Diferenças:**
  - Prompts são dinâmicos
  - Outputs são texto (difícil avaliar)
  - Custos são por token
  - Behavior pode mudar com updates

## Production Feedback Loop

```
User Interactions
    ↓
[Trace Collection] (Langfuse, Arize)
    ↓
[Automatic Dataset Creation]
    ↓
[Continuous Evaluation]
    ↓
[Performance Drops?] ─YES→ [Re-optimization] → Deploy
    ↓ NO
    ↓
[Optimization Plateau?] ─YES→ [Fine-tuning] → Deploy
    ↓ NO
    ↓
Continue monitoring
```

## Trace Collection

```python
# Integration com Langfuse (PLACEHOLDER - RESEARCH)
import langfuse

tracer = langfuse.Langfuse()

@tracer.trace
def production_pipeline(query):
    result = pipeline(query)
    # Trace automatically sent to Langfuse
    return result
```

## Automated Dataset Creation

```python
def traces_to_dataset(traces, quality_threshold=0.8):
    dataset = []
    
    for trace in traces:
        if trace.user_feedback >= quality_threshold:
            example = dspy.Example(
                query=trace.input,
                expected_output=trace.output
            ).with_inputs("query")
            
            dataset.append(example)
    
    return dataset
```

## Continuous Evaluation

```python
from apscheduler.schedulers.background import BackgroundScheduler

def evaluate_production():
    # Get traces last 24h
    traces = get_recent_traces(hours=24)
    
    # Convert to dataset
    dataset = traces_to_dataset(traces)
    
    # Evaluate current performance
    current_score = evaluate(current_pipeline, dataset)
    
    # If performance drops, trigger re-optimization
    if current_score < threshold:
        trigger_reoptimization(dataset)

# Run every 6 hours
scheduler = BackgroundScheduler()
scheduler.add_job(evaluate_production, 'interval', hours=6)
scheduler.start()
```

## Triggers Automáticos
1. **Performance drop** → Re-optimize
2. **New data accumulated** → Re-train
3. **Negative feedback** → Review
4. **Optimization plateau** → Consider fine-tuning

## Model Versioning
- Git: Código
- DVC: Datasets
- MLflow/W&B: Modelos
- DSPy prompts? (TO BE DEFINED)

## Key Takeaways
- LLMOps é essencial para produção
- Feedback loop contínuo
- Automação de evaluation
- Triggers inteligentes
- Versioning de tudo

**Status:** Estrutura completa, research pending ✅⚠️
