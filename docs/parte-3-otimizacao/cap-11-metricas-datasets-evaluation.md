# Capítulo 11: Métricas, Datasets e Evaluation

**Status:** ✅ Estrutura completa

## Conceito Principal
Como avaliar multi-agent systems? Diferente de single agent.

## Desafios
- Single agent: 1 output
- Multi-agent: N outputs intermediários + 1 final
- Como avaliar coordenação?
- Como atribuir crédito?

## Métricas Compostas

```python
def pipeline_metric(example, prediction, trace=None):
    # Avaliar cada stage
    search_score = evaluate_search(prediction.search_summary)
    analysis_score = evaluate_analysis(prediction.analysis)
    recommendation_score = evaluate_recommendation(prediction.recommendation)
    final_score = evaluate_final(prediction.final_message)
    
    # Combinar (weighted)
    total = (
        0.2 * search_score +
        0.3 * analysis_score +
        0.3 * recommendation_score +
        0.2 * final_score
    )
    
    return total
```

## Datasets Multi-Stage

```python
trainset = [
    dspy.Example(
        query="...",
        expected_flight_id="FL001",
        stage_expectations={
            "search": "Deve encontrar 3 voos",
            "analysis": "Deve considerar preço e horário",
            "recommendation": "Deve recomendar FL002"
        }
    ).with_inputs("query")
]
```

## Evaluation Frameworks
- **Holistic:** Sistema completo
- **Stage-by-Stage:** Cada agente
- **Comparative:** Entre arquiteturas
- **A/B Testing:** Production

**Status:** Estrutura completa ✅
