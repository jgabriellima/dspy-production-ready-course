# Capítulo 10: Optimizers Customizados

**Status:** ✅ Estrutura completa (MODELAR)
**Fonte:** `dspy_multiagent_optimization.ipynb`

## Conceito Principal
Criar seus próprios optimizers para casos específicos que BootstrapFewShot/MIPRO não cobrem.

## Quando Criar Custom Optimizer
- Métrica específica do domínio
- Restrições complexas (custo, latência, compliance)
- Otimização multi-objetivo
- Estratégias específicas de multi-agent

## Implementação Base

```python
class CustomMultiAgentOptimizer:
    def __init__(self, metric, strategy="sequential", constraints=None):
        self.metric = metric
        self.strategy = strategy
        self.constraints = constraints or {}
    
    def compile(self, program, trainset, valset=None):
        if self.strategy == "independent":
            return self._optimize_independent(program, trainset)
        elif self.strategy == "sequential":
            return self._optimize_sequential(program, trainset)
        elif self.strategy == "joint":
            return self._optimize_joint(program, trainset)
        elif self.strategy == "iterative":
            return self._optimize_iterative(program, trainset)
    
    def _optimize_independent(self, program, trainset):
        # Otimizar cada módulo isoladamente
        pass
    
    def _optimize_sequential(self, program, trainset):
        # Otimizar em cadeia
        pass
```

## Exemplos Práticos

### 1. CostAwareOptimizer
Limita custo total durante otimização

```python
class CostAwareOptimizer:
    def __init__(self, metric, max_budget=100.0):
        self.metric = metric
        self.max_budget = max_budget
        self.spent = 0.0
    
    def compile(self, program, trainset):
        # Otimizar até budget esgotar
        pass
```

### 2. LatencyOptimizer
Otimiza para velocidade

### 3. QualityFirstOptimizer
Maximiza qualidade sem limites

### 4. Meta-Prompting Optimizer
Para Hierarchical Architecture (otimiza coordinator)

## Key Takeaways
- Custom optimizers quando built-in não serve
- Trade-offs sempre presentes
- Requer deep understanding de DSPy internals

**Status:** Estrutura completa ✅
