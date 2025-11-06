# 📊 Resumo Executivo: Otimização de Arquiteturas Multi-Agent

## Conteúdo Completo do Notebook de Otimização

Este documento complementa o notebook `dspy_multiagent_optimization.ipynb` com conteúdo adicional sobre otimização de cada arquitetura.

---

## 🔄 Parte 3: Otimização Sequential/Pipeline

### Estratégias

#### 1. **Backward Optimization** (Recomendada)
```python
# Otimizar de trás para frente
for i in reversed(range(len(agents))):
    agents[i] = optimize(agents[i], data_considering_future_agents)
```

**Vantagens:**
- Cada agente sabe o que o próximo espera
- Reduz propagação de erros
- Credit assignment mais claro

#### 2. **End-to-End Optimization**
```python
# Tratar como módulo único
pipeline = Pipeline(agents)
optimized = MIPRO.compile(pipeline, trainset)
```

**Uso de MIPRO:**
- MIPROv2 funciona bem para pipelines
- `num_candidates=10`: testar múltiplas configurações
- `num_trials=20`: mais iterações para convergir

---

## 💬 Parte 4: Otimização Collaborative/Debate

### Desafios Únicos

1. **Diversidade vs Consenso**: Queremos perspectivas diferentes MAS consenso útil
2. **Multi-objective**: Otimizar múltiplos objetivos simultaneamente
3. **Debate Quality**: Não apenas resultado, mas qualidade do debate

### Estratégias

#### 1. **Independent + Consensus Optimization**
```python
# Passo 1: Otimizar cada agente para sua perspectiva
price_agent = optimize(price_agent, price_focused_data)
comfort_agent = optimize(comfort_agent, comfort_focused_data)
time_agent = optimize(time_agent, time_focused_data)

# Passo 2: Otimizar consenso
consensus_agent = optimize(
    consensus_agent,
    data_with_multiple_perspectives,
    fixed_agents=[price, comfort, time]
)
```

#### 2. **Reward Shaping**
```python
def collaborative_metric(pred, gold):
    # Componentes da métrica
    final_quality = accuracy(pred.final_decision, gold)
    diversity_score = measure_diversity(pred.agent_opinions)
    consensus_quality = measure_consensus_process(pred.debate_history)
    
    # Métrica composta
    return (
        0.5 * final_quality +
        0.2 * diversity_score +
        0.3 * consensus_quality
    )
```

**Métricas Customizadas:**
- **Diversity Score**: Medir quão diferentes são as perspectivas
- **Consensus Quality**: Avaliar processo de chegada ao consenso
- **Final Accuracy**: Qualidade da decisão final

#### 3. **Multi-Objective Optimization**
```python
# Pareto optimization para trade-offs
objectives = {
    'accuracy': lambda p, g: accuracy(p, g),
    'diversity': lambda p, g: diversity_score(p.opinions),
    'speed': lambda p, g: 1.0 / p.num_rounds
}

# Encontrar soluções Pareto-optimal
pareto_solutions = multi_objective_optimize(system, objectives, trainset)
```

### Técnica Específica: Debate Rounds Optimization

```python
class DebateOptimizer:
    def optimize_rounds(self, system, trainset):
        """Encontrar número ótimo de rodadas de debate"""
        results = []
        
        for num_rounds in [1, 2, 3, 4]:
            system.num_rounds = num_rounds
            score = evaluate(system, trainset)
            cost = estimate_cost(num_rounds)
            
            results.append({
                'rounds': num_rounds,
                'score': score,
                'cost': cost,
                'efficiency': score / cost
            })
        
        # Escolher melhor trade-off
        best = max(results, key=lambda x: x['efficiency'])
        return best['rounds']
```

---

## 🔍 Parte 5: Otimização Reflexive/Self-Critique

### Desafios Únicos

1. **Loop Convergence**: Garantir que loop de refinamento converge
2. **Quality Threshold**: Definir quando parar de refinar
3. **Overfitting do Crítico**: Crítico pode ser muito severo ou leniente

### Estratégias

#### 1. **Actor-Critic Co-Optimization**
```python
for iteration in range(max_iterations):
    # Otimizar Actor para gerar boas respostas
    actor = optimize(actor, trainset, metric=output_quality)
    
    # Otimizar Critic para avaliar corretamente
    critic = optimize(
        critic,
        critique_data,  # dados com críticas humanas
        metric=critique_accuracy
    )
    
    # Refiner aprende com ambos
    refiner = optimize(
        refiner,
        refinement_data,
        fixed_actor=actor,
        fixed_critic=critic
    )
```

#### 2. **Quality-Aware Metrics**
```python
def reflexive_metric(pred, gold):
    # Qualidade do output final
    final_quality = accuracy(pred.final_output, gold)
    
    # Qualidade do processo reflexivo
    improvement = pred.final_quality - pred.initial_quality
    iterations_needed = pred.iterations_used
    
    # Penalizar se usa muitas iterações
    efficiency = improvement / iterations_needed
    
    return 0.7 * final_quality + 0.3 * efficiency
```

#### 3. **Convergence Optimization**
```python
def optimize_convergence(system, trainset):
    """Otimizar sistema para convergir rapidamente"""
    
    # Métrica que favorece convergência rápida
    def convergence_metric(pred, gold):
        if pred.converged:
            quality = accuracy(pred.output, gold)
            speed_bonus = 1.0 / pred.iterations_used
            return quality + 0.2 * speed_bonus
        else:
            return 0.0  # Penalizar não convergência
    
    return optimize(system, trainset, metric=convergence_metric)
```

### Técnica Específica: Quality Threshold Tuning

```python
class ReflexiveOptimizer:
    def tune_quality_threshold(self, system, trainset, devset):
        """Encontrar threshold ótimo para parar refinamento"""
        
        thresholds = [7.0, 7.5, 8.0, 8.5, 9.0]
        results = {}
        
        for threshold in thresholds:
            system.quality_threshold = threshold
            
            # Avaliar no dev set
            avg_quality = []
            avg_iterations = []
            
            for example in devset:
                result = system(example)
                avg_quality.append(evaluate(result, example.gold))
                avg_iterations.append(result.iterations_used)
            
            results[threshold] = {
                'quality': np.mean(avg_quality),
                'iterations': np.mean(avg_iterations),
                'efficiency': np.mean(avg_quality) / np.mean(avg_iterations)
            }
        
        # Escolher threshold com melhor efficiency
        best_threshold = max(results.items(), 
                            key=lambda x: x[1]['efficiency'])[0]
        
        return best_threshold, results
```

---

## 🚀 Parte 6: MIPRO Adaptado para Multi-Agent

### Por que MIPRO é Ideal para Multi-Agent?

MIPRO (Multi-prompt Instruction PRoposal Optimizer) é perfeito para multi-agent porque:

1. **Multi-prompt**: Otimiza múltiplas signatures simultaneamente
2. **Instrução + Exemplos**: Aprende tanto instruções quanto few-shot examples
3. **Bayesian Optimization**: Explora espaço de busca eficientemente

### MIPRO para Cada Arquitetura

#### 1. **Hierarchical**
```python
# Aplicar MIPRO no sistema completo
optimizer = dspy.MIPROv2(
    metric=hierarchical_metric,
    num_candidates=10,
    init_temperature=1.0,
    verbose=True
)

# Otimiza coordenador E especialistas juntos
optimized_system = optimizer.compile(
    hierarchical_system,
    trainset=trainset,
    num_trials=30,
    max_bootstrapped_demos=4,
    max_labeled_demos=4
)
```

**Configuração Específica:**
- `num_candidates=10`: Testar 10 variações de prompts
- `num_trials=30`: Mais trials para coordenação complexa
- `init_temperature=1.0`: Exploração inicial alta

#### 2. **Sequential/Pipeline**
```python
# MIPRO end-to-end para pipeline
optimizer = dspy.MIPROv2(
    metric=pipeline_end_to_end_metric,
    num_candidates=8,
    prompt_model=lm,  # Usar LLM para gerar prompts
)

optimized_pipeline = optimizer.compile(
    pipeline_system,
    trainset=trainset,
    requires_permission_to_run=False
)
```

**Dica:** Use `task_description` detalhada:
```python
task_description = """
This is a sequential pipeline for flight booking:
1. Search: Find available flights
2. Analyze: Evaluate options
3. Recommend: Pick best flight
4. Confirm: Finalize booking

Each stage must pass high-quality information to the next.
"""
```

#### 3. **Collaborative/Debate**
```python
# MIPRO com métrica multi-objetivo
def collaborative_mipro_metric(pred, gold):
    final_acc = accuracy(pred.consensus, gold)
    debate_quality = evaluate_debate_quality(pred.debate_history)
    return 0.7 * final_acc + 0.3 * debate_quality

optimizer = dspy.MIPROv2(
    metric=collaborative_mipro_metric,
    num_candidates=12,  # Mais variações para capturar diversidade
    prompt_model=lm,
)

optimized = optimizer.compile(
    collaborative_system,
    trainset=trainset,
    num_trials=40  # Mais trials para convergir
)
```

#### 4. **Reflexive**
```python
# MIPRO focado em qualidade iterativa
def reflexive_mipro_metric(pred, gold):
    if not pred.converged:
        return 0.0
    
    quality = accuracy(pred.final_output, gold)
    efficiency = 1.0 / pred.iterations_used
    return quality + 0.15 * efficiency

optimizer = dspy.MIPROv2(
    metric=reflexive_mipro_metric,
    num_candidates=8,
    init_temperature=0.8,  # Menos exploração, mais exploitation
)

optimized = optimizer.compile(
    reflexive_system,
    trainset=trainset,
    max_bootstrapped_demos=6  # Mais exemplos para crítica
)
```

### MIPRO Avançado: Custom Proposal

```python
# Propor prompts customizados para multi-agent
class MultiAgentProposer:
    def propose_instructions(self, system, trainset):
        """Propor instruções específicas para cada agente"""
        proposals = {
            'coordinator': [
                "Route user request to the most appropriate specialist",
                "Analyze request and delegate to expert agent",
                "Determine which specialist handles this query"
            ],
            'search_specialist': [
                "Find all relevant flights matching criteria",
                "Search comprehensively for flight options",
                "Retrieve available flights for route and date"
            ],
            # ... mais propostas
        }
        return proposals

# Usar com MIPRO
optimizer = dspy.MIPROv2(
    metric=metric,
    num_candidates=10,
    proposal_model=MultiAgentProposer()
)
```

---

## 📊 Parte 7: Datasets e Métricas para Multi-Agent

### Criando Datasets Específicos

#### Dataset para Hierarchical
```python
@dataclass
class HierarchicalExample:
    user_request: str
    correct_specialist: str  # "search", "recommendation", "booking"
    specialist_input: Dict[str, Any]
    expected_output: str
    gold_routing: str

trainset_hierarchical = [
    HierarchicalExample(
        user_request="Find flights from SFO to JFK on Dec 1st",
        correct_specialist="search",
        specialist_input={"departure": "SFO", "arrival": "JFK"},
        expected_output=json.dumps({"flights": [...]}),
        gold_routing="search"
    ),
    # ... mais exemplos
]
```

#### Dataset para Sequential
```python
@dataclass
class SequentialExample:
    initial_input: Dict[str, Any]
    intermediate_outputs: List[str]  # Output de cada etapa
    final_output: str
    stage_labels: List[str]  # Qual etapa está correta/incorreta

trainset_sequential = [
    SequentialExample(
        initial_input={"query": "cheap flight to NYC"},
        intermediate_outputs=[
            json.dumps({"flights": [...]}),  # Etapa 1
            "Analysis: 3 options available...",  # Etapa 2
            json.dumps({"recommendation": "f002"}),  # Etapa 3
        ],
        final_output=json.dumps({"booking": "confirmed"}),
        stage_labels=["correct", "correct", "correct", "correct"]
    ),
]
```

#### Dataset para Collaborative
```python
@dataclass
class CollaborativeExample:
    scenario: str
    agent_perspectives: Dict[str, str]  # Opinião esperada de cada agente
    consensus: str
    trade_offs: List[str]  # Trade-offs identificados

trainset_collaborative = [
    CollaborativeExample(
        scenario="User wants flight: cheap BUT comfortable",
        agent_perspectives={
            "price": "Choose f002 ($380)",
            "comfort": "Choose f003 (A350, more space)",
            "time": "Choose f003 (fastest)"
        },
        consensus="f003 - balances comfort and time, small price increase acceptable",
        trade_offs=["$140 more expensive but better experience"]
    ),
]
```

#### Dataset para Reflexive
```python
@dataclass
class ReflexiveExample:
    initial_input: str
    initial_output: str  # Output da primeira tentativa
    critique: str  # Crítica esperada
    refined_output: str  # Output melhorado
    quality_progression: List[float]  # [5.0, 7.5, 9.0] scores por iteração

trainset_reflexive = [
    ReflexiveExample(
        initial_input="Recommend flight for business traveler",
        initial_output="Choose f001 - cheapest option",
        critique="Missing: business travelers value time and comfort over price",
        refined_output="Choose f003 - fastest flight with premium aircraft",
        quality_progression=[6.0, 8.5, 9.2]
    ),
]
```

### Métricas Customizadas

#### Métrica Composta para Hierarchical
```python
def hierarchical_metric(example, pred, trace=None):
    # 1. Routing accuracy (coordenador)
    routing_correct = (pred.specialist == example.correct_specialist)
    routing_score = 1.0 if routing_correct else 0.0
    
    # 2. Specialist quality
    specialist_score = evaluate_specialist_output(
        pred.specialist_output,
        example.expected_output
    )
    
    # 3. End-to-end quality
    e2e_score = evaluate_final_output(pred, example.gold)
    
    # Compor com pesos
    return (
        0.3 * routing_score +
        0.3 * specialist_score +
        0.4 * e2e_score
    )
```

#### Métrica para Sequential (com intermediate supervision)
```python
def sequential_metric(example, pred, trace=None):
    scores = []
    
    # Avaliar cada etapa
    for i, (stage_output, gold_stage) in enumerate(zip(
        pred.stage_outputs, 
        example.intermediate_outputs
    )):
        stage_score = evaluate_stage(stage_output, gold_stage)
        weight = 1.0 / (len(pred.stage_outputs) - i)  # Etapas finais têm mais peso
        scores.append(weight * stage_score)
    
    # Final output tem peso maior
    final_score = evaluate_final(pred.final_output, example.final_output)
    scores.append(2.0 * final_score)
    
    return np.mean(scores)
```

#### Métrica para Collaborative (multi-objective)
```python
def collaborative_metric(example, pred, trace=None):
    # 1. Consensus accuracy
    consensus_acc = (pred.consensus_decision == example.consensus)
    
    # 2. Perspective diversity
    opinions = [pred.price_opinion, pred.comfort_opinion, pred.time_opinion]
    diversity = measure_diversity(opinions)  # Baixa similaridade entre opiniões
    
    # 3. Trade-off awareness
    tradeoff_score = evaluate_tradeoff_discussion(
        pred.debate_history,
        example.trade_offs
    )
    
    # 4. Debate quality
    debate_rounds = len(pred.debate_history)
    efficiency = 1.0 / debate_rounds if debate_rounds > 0 else 0.0
    
    return (
        0.4 * consensus_acc +
        0.2 * diversity +
        0.2 * tradeoff_score +
        0.2 * efficiency
    )

def measure_diversity(opinions):
    """Medir quão diferentes são as opiniões"""
    # Exemplo simplificado: usar similarity
    similarities = []
    for i in range(len(opinions)):
        for j in range(i+1, len(opinions)):
            sim = similarity(opinions[i], opinions[j])
            similarities.append(sim)
    
    # Diversidade = 1 - média de similaridade
    return 1.0 - np.mean(similarities)
```

#### Métrica para Reflexive (quality progression)
```python
def reflexive_metric(example, pred, trace=None):
    # 1. Final quality
    final_quality = evaluate(pred.final_output, example.gold)
    
    # 2. Improvement trajectory
    if len(pred.quality_history) > 1:
        improvements = [
            pred.quality_history[i+1] - pred.quality_history[i]
            for i in range(len(pred.quality_history)-1)
        ]
        avg_improvement = np.mean(improvements)
    else:
        avg_improvement = 0.0
    
    # 3. Convergence speed
    iterations = pred.iterations_used
    speed_score = 1.0 / iterations if iterations > 0 else 0.0
    
    # 4. Critique quality (se temos gold critique)
    if hasattr(example, 'gold_critique'):
        critique_score = evaluate_critique(
            pred.critique,
            example.gold_critique
        )
    else:
        critique_score = 0.5  # Neutro
    
    return (
        0.5 * final_quality +
        0.2 * min(avg_improvement * 10, 1.0) +  # Normalizar
        0.15 * speed_score +
        0.15 * critique_score
    )
```

---

## 🧪 Parte 8: Experimentos Comparativos

### Protocolo de Avaliação

```python
class MultiAgentEvaluator:
    def __init__(self, trainset, devset, testset):
        self.trainset = trainset
        self.devset = devset
        self.testset = testset
        
    def compare_architectures(self, systems, metrics):
        """Comparar diferentes arquiteturas"""
        results = {}
        
        for name, system in systems.items():
            print(f"\n{'='*60}")
            print(f"Evaluating: {name}")
            print('='*60)
            
            # Treinar
            start_time = time.time()
            optimized = self.train(system, self.trainset)
            train_time = time.time() - start_time
            
            # Avaliar
            test_score = self.evaluate(optimized, self.testset, metrics)
            
            # Custo (estimado)
            cost = self.estimate_cost(optimized, self.testset)
            
            results[name] = {
                'test_score': test_score,
                'train_time': train_time,
                'inference_cost': cost,
                'efficiency': test_score / cost
            }
            
        return results
    
    def train(self, system, trainset):
        """Treinar sistema com técnica apropriada"""
        # Escolher otimizador baseado em tipo de sistema
        if isinstance(system, HierarchicalMultiAgent):
            optimizer = HierarchicalOptimizer(...)
            return optimizer.alternating_optimize(trainset)
        elif isinstance(system, SequentialPipelineMultiAgent):
            optimizer = SequentialPipelineOptimizer(...)
            return optimizer.backward_optimize(trainset)
        # ... outros casos
        
    def evaluate(self, system, testset, metrics):
        """Avaliar sistema otimizado"""
        scores = []
        for example in testset:
            try:
                pred = system(**example.inputs)
                score = metrics(example, pred)
                scores.append(score)
            except Exception as e:
                print(f"Error: {e}")
                scores.append(0.0)
        
        return np.mean(scores)
```

### Resultados Esperados

```python
# Exemplo de resultados comparativos
comparative_results = {
    'Hierarchical': {
        'test_score': 0.85,
        'train_time': 120,  # segundos
        'inference_cost': 0.005,  # $ por query
        'efficiency': 170.0  # score/cost
    },
    'Sequential': {
        'test_score': 0.88,
        'train_time': 180,
        'inference_cost': 0.008,
        'efficiency': 110.0
    },
    'Collaborative': {
        'test_score': 0.92,
        'train_time': 300,
        'inference_cost': 0.015,
        'efficiency': 61.3
    },
    'Reflexive': {
        'test_score': 0.94,
        'train_time': 240,
        'inference_cost': 0.012,
        'efficiency': 78.3
    }
}

# Visualizar
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Quality vs Cost
axes[0, 0].scatter(
    [r['inference_cost'] for r in comparative_results.values()],
    [r['test_score'] for r in comparative_results.values()]
)
axes[0, 0].set_xlabel('Inference Cost ($)')
axes[0, 0].set_ylabel('Test Score')
axes[0, 0].set_title('Quality vs Cost Trade-off')

# ... mais plots
```

---

## 🎓 Conclusões e Recomendações

### Quando usar cada técnica?

| Arquitetura | Técnica de Otimização | Quando Usar |
|-------------|----------------------|-------------|
| **Hierarchical** | Alternating Optimization | Domínios bem separados, precisa de roteamento |
| **Sequential** | Backward + End-to-End | Workflow linear, cada etapa crítica |
| **Collaborative** | Reward Shaping + Multi-Objective | Decisões complexas, trade-offs |
| **Reflexive** | Actor-Critic Co-Optimization | Qualidade > Tudo, tempo disponível |

### Best Practices

1. **Start Simple**
   - Comece com BootstrapFewShot para agentes individuais
   - Depois use técnicas avançadas

2. **Measure Everything**
   - Track métricas por agente E sistema completo
   - Monitore custo e latência

3. **Iterate**
   - Não otimize tudo de uma vez
   - Itere: baseline → individual agents → joint optimization

4. **Use MIPRO quando possível**
   - MIPROv2 é state-of-the-art para multi-prompt optimization
   - Funciona bem para todas as arquiteturas

5. **Custom Metrics são Críticas**
   - Métricas genéricas não capturam nuances de multi-agent
   - Invista tempo em métricas customizadas boas

### Recursos Adicionais

- [DSPy Documentation](https://dspy.ai)
- [MIPRO Paper](https://arxiv.org/abs/2406.11695)
- [Multi-Agent RL Survey](https://arxiv.org/abs/1911.10635)

---

**Fim do Resumo Executivo**

Este conteúdo complementa o notebook `dspy_multiagent_optimization.ipynb` e pode ser incorporado como células markdown/code conforme necessário.

