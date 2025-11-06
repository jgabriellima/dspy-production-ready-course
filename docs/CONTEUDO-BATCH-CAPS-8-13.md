# CONTEÚDO COMPLETO: Capítulos 8-13
**Otimização e Fine-Tuning Multi-Agent**

---

# Capítulo 8: Fundamentos de Otimização Multi-Agent

## STATUS: 100% ESTRUTURA

### Conceito Principal
**Por que otimizar? Como otimizar multi-agent é diferente de single agent?**

### Estrutura do Capítulo

1. **O Desafio** (MD)
   - Single agent: otimizar 1 prompt
   - Multi-agent: otimizar N prompts + coordenação
   - **Explosion combinatorial:** N agents × M iterações = N^M possibilidades

2. **Estratégias de Otimização** (MD)
   - **Independent:** Otimiza cada agente isoladamente
   - **Sequential:** Otimiza agente por agente em ordem
   - **Joint:** Otimiza todos juntos (caro mas melhor)
   - **Iterative/Alternating:** Alterna entre agentes

3. **Fundamentação Teórica** (MD)
   - Multi-objective optimization
   - Nash Equilibrium em multi-agent
   - Credit assignment problem
   - Papers: MARL, Multi-agent coordination

4. **Exemplo Prático** (PY)
```python
# Comparar 4 estratégias no Sequential Pipeline (Cap 4)

# Baseline (sem otimização)
pipeline_baseline = SequentialPipelineMultiAgent()

# Estratégia 1: Independent
# Otimizar cada agente isoladamente
search_optimized = dspy.BootstrapFewShot(metric=search_metric)(search_agent)
analysis_optimized = dspy.BootstrapFewShot(metric=analysis_metric)(analysis_agent)
# ... etc

# Estratégia 2: Sequential
# Otimizar em ordem (search → analysis → recommendation → confirmation)

# Estratégia 3: Joint
# Otimizar todo pipeline como uma unidade

# Estratégia 4: Iterative
# Otimizar search, depois analysis com search otimizado, etc
```

---

# Capítulo 9: BootstrapFewShot & MIPRO

## STATUS: 100% ESTRUTURA (MODELAR de notebooks)

### Fonte
`dspy_multiagent_optimization.ipynb` + `dspy_optimization_mastery.ipynb`

### Conceito Principal
**Otimização automática de prompts com DSPy**

### Estrutura do Capítulo

1. **BootstrapFewShot** (MD + PY)
   - O que é? Gera exemplos automaticamente
   - Como funciona? Teacher model gera, student aprende
   - Quando usar? Quando você tem dataset mas poucos exemplos anotados

```python
# Exemplo: Otimizar SearchAgent do Cap 4
from dspy.teleprompt import BootstrapFewShot

# Definir métrica
def search_metric(example, prediction, trace=None):
    # Avaliar qualidade da busca
    return score

# Criar optimizer
optimizer = BootstrapFewShot(metric=search_metric, max_bootstrapped_demos=8)

# Otimizar
search_agent_optimized = optimizer.compile(search_agent, trainset=trainset)
```

2. **MIPRO (MIPROv2)** (MD + PY)
   - O que é? Multi-prompt Instruction Proposal Optimizer
   - Paper ref: Opsahl-Ong et al., 2024
   - Otimiza instruções E demonstrações simultaneamente
   - **Best for multi-stage programs**

```python
from dspy.teleprompt import MIPROv2

optimizer = MIPROv2(
    metric=pipeline_metric,
    num_candidates=10,
    init_temperature=1.0
)

pipeline_optimized = optimizer.compile(
    pipeline,
    trainset=trainset,
    num_trials=100
)
```

3. **Comparação** (MD)
   - BootstrapFewShot: Rápido, bons exemplos
   - MIPRO: Mais completo, otimiza tudo
   - Trade-off: Tempo vs qualidade

4. **Hands-On** (PY)
   - Aplicar ambos no Sequential Pipeline
   - Comparar resultados
   - Métricas antes/depois

---

# Capítulo 10: Optimizers Customizados

## STATUS: 100% ESTRUTURA (MODELAR de notebooks)

### Fonte
`dspy_multiagent_optimization.ipynb`

### Conceito Principal
**Criar seu próprio optimizer para casos específicos**

### Estrutura do Capítulo

1. **Quando Criar Custom Optimizer** (MD)
   - Métrica específica do domínio
   - Restrições complexas
   - Otimização multi-objetivo
   - Budget constraints (custo, latência)

2. **Anatomy of an Optimizer** (PY)
```python
class CustomMultiAgentOptimizer:
    def __init__(self, metric, strategy="sequential"):
        self.metric = metric
        self.strategy = strategy
    
    def compile(self, program, trainset, valset=None):
        if self.strategy == "independent":
            return self._optimize_independent(program, trainset)
        elif self.strategy == "joint":
            return self._optimize_joint(program, trainset)
        # ...
    
    def _optimize_independent(self, program, trainset):
        # Otimizar cada módulo isoladamente
        pass
    
    def _optimize_joint(self, program, trainset):
        # Otimizar todos juntos
        pass
```

3. **Exemplos Práticos** (PY)
   - **CostAwareOptimizer:** Limita custo total
   - **LatencyOptimizer:** Otimiza para velocidade
   - **QualityFirstOptimizer:** Maximiza qualidade sem limites

4. **Meta-Prompting para Coordenação** (MD + PY)
   - Otimizar o Coordinator (Hierarchical)
   - Reward shaping para Sequential
   - Quality metrics composition

---

# Capítulo 11: Métricas, Datasets e Evaluation

## STATUS: 100% ESTRUTURA (CRIAR)

### Conceito Principal
**Como avaliar multi-agent systems**

### Estrutura do Capítulo

1. **Desafios de Evaluation** (MD)
   - Single agent: 1 output para avaliar
   - Multi-agent: N outputs intermediários + 1 final
   - Como avaliar coordenação?
   - Como avaliar contribuição de cada agente?

2. **Métricas Compostas** (PY)
```python
# Métrica composta para Sequential Pipeline
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

3. **Datasets para Multi-Agent** (PY)
```python
# Criar dataset com múltiplos níveis
trainset = [
    dspy.Example(
        query="...",
        expected_flight_id="FL001",
        expected_reasoning="...",
        stage_expectations={
            "search": "...",
            "analysis": "...",
            "recommendation": "..."
        }
    ).with_inputs("query")
]
```

4. **Evaluation Frameworks** (PY)
   - **Holistic:** Avalia sistema completo
   - **Stage-by-Stage:** Avalia cada agente
   - **Comparative:** Compara arquiteturas
   - **A/B Testing:** Multi-agent vs single agent

---

# Capítulo 12: Optimization Mastery

## STATUS: 100% ESTRUTURA (MODELAR de notebooks)

### Fonte
`dspy_optimization_mastery.ipynb`

### Conceito Principal
**Técnicas avançadas de otimização**

### Estrutura do Capítulo

1. **Ensemble Methods** (MD + PY)
   - Múltiplos modelos otimizados
   - Voting, averaging, stacking
   - Trade-off: custo vs robustez

2. **Curriculum Learning** (MD + PY)
   - Treinar com exemplos fáceis primeiro
   - Gradualmente aumentar dificuldade
   - Aplicado a multi-agent: otimizar arquitetura simples → complexa

3. **Active Learning** (MD + PY)
   - Selecionar exemplos mais informativos
   - Reduzir dataset necessário
   - **Query by committee:** Agents discordam = exemplo valioso

4. **Hyperparameter Tuning** (PY)
```python
# Grid search para multi-agent
best_config = None
best_score = 0

for num_agents in [2, 4, 8]:
    for temperature in [0.3, 0.7, 1.0]:
        for max_tokens in [500, 1000, 2000]:
            pipeline = create_pipeline(num_agents, temperature, max_tokens)
            score = evaluate(pipeline, valset)
            
            if score > best_score:
                best_score = score
                best_config = (num_agents, temperature, max_tokens)
```

5. **Meta-Learning** (MD)
   - Learn to optimize
   - Transfer learning entre domínios
   - Few-shot adaptation

---

# Capítulo 13: Fine-Tuning Multi-Agent Systems

## STATUS: 100% ESTRUTURA (REQUER RESEARCH)

### ⚠️ RESEARCH NEEDED
Ver: `docs/_planejamento/06-RESEARCH-FINETUNING.md`

### Conceito Principal
**Quando otimização de prompts não é suficiente: fine-tune o LLM base**

### Estrutura do Capítulo

1. **Por que Fine-Tune?** (MD)
   - Otimização de prompts: melhora até certo ponto
   - Fine-tuning: melhora weights do modelo
   - **Quando?** Quando você tem:
     - Dataset grande e específico
     - Budget para treinar
     - Performance crítica

2. **DSPy + Fine-Tuning** (MD + PY)
   - **RESEARCH:** Como DSPy integra fine-tuning?
   - Exportar traces para dataset de fine-tuning
   - Tools disponíveis no ecossistema DSPy

```python
# PLACEHOLDER - REQUER RESEARCH
# Como seria?
from dspy.finetuning import export_for_finetuning

# Coletar traces de execução
traces = []
for example in trainset:
    trace = pipeline(example.query, trace=True)
    traces.append(trace)

# Exportar para formato de fine-tuning
finetuning_dataset = export_for_finetuning(traces)

# Fine-tune (usando OpenAI API, Hugging Face, etc)
# ... DETAILS TO BE RESEARCHED ...
```

3. **Multi-Agent Fine-Tuning Strategies** (MD)
   - **Strategy 1:** Fine-tune cada agente separadamente
   - **Strategy 2:** Fine-tune modelo único para todos agentes
   - **Strategy 3:** Fine-tune só os agentes críticos
   - **Trade-offs:** Custo, complexidade, performance

4. **Practical Workflow** (MD + PY)
```
1. Desenvolver com otimização de prompts
2. Coletar traces de produção
3. Criar dataset de fine-tuning
4. Fine-tune modelo(s)
5. Re-deploy com modelos fine-tunados
6. Monitorar performance
7. Iterar
```

5. **Tools & Platforms** (MD)
   - **RESEARCH NEEDED:**
     - OpenAI fine-tuning API
     - Hugging Face Transformers
     - DSPy integrations?
     - Custom training loops
   - Ver: `06-RESEARCH-FINETUNING.md` para detalhes

---

## REFERÊNCIAS PRINCIPAIS

```
Khattab, O., et al. (2023). DSPy: Compiling Declarative Language Model Calls 
into Self-Improving Pipelines. arXiv:2310.03714.

Opsahl-Ong, B., et al. (2024). Optimizing Instructions and Demonstrations for 
Multi-Stage Language Model Programs (MIPRO). arXiv:2406.11695.

Shinn, N., et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. 
arXiv:2303.11366.

[RESEARCH NEEDED: Fine-tuning papers específicos para DSPy]
```

---

## PRÓXIMOS PASSOS

1. ✅ Estruturas prontas para Caps 8-13
2. ⏳ RESEARCH necessário para Cap 13 (fine-tuning)
3. ⏳ Expandir cada cap para 15-20 células
4. ⏳ Adicionar código executável
5. ⏳ Adicionar testes e análises

**Status Caps 8-13:** Estrutura 100%, conteúdo completo pending (mas blueprint pronto)

