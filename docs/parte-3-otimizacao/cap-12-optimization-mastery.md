# Capítulo 12: Optimization Mastery

**Status:** ✅ Estrutura completa (MODELAR)
**Fonte:** `dspy_optimization_mastery.ipynb`

## Conceito Principal
Técnicas avançadas de otimização para squeezar até a última gota de performance.

## Técnicas

### 1. Ensemble Methods
Múltiplos modelos otimizados votam

```python
# Treinar N versões
models = []
for i in range(5):
    opt = MIPROv2(metric=my_metric, seed=i)
    model = opt.compile(pipeline, trainset)
    models.append(model)

# Ensemble: Voting
def ensemble_predict(query):
    predictions = [m(query) for m in models]
    # Votar ou agregar
    return aggregate(predictions)
```

### 2. Curriculum Learning
Treinar com exemplos fáceis → difíceis

### 3. Active Learning
Selecionar exemplos mais informativos

### 4. Hyperparameter Tuning
Grid search para multi-agent configs

### 5. Meta-Learning
Learn to optimize (transfer learning)

## Key Takeaways
- Ensemble: Robustez vs custo
- Curriculum: Acelera convergência
- Active: Reduz dataset necessário
- Hyper: Crítico para production
- Meta: Futuro da otimização

**Status:** Estrutura completa ✅
