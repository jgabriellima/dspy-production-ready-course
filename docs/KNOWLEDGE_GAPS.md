# Knowledge Gaps - Conceitos a Explicar

## Objetivo

Identificar e documentar todos os conceitos que precisam ser explicados no livro, categorizados por prioridade e localização.

---

## PARTE 1: FUNDAMENTOS

### Cap 1: Enterprise aos Agentes

**Crítico (deve ser explicado):**
- [ ] O que são Large Language Models (LLMs)
- [ ] Diferença entre prompting e programming LLMs
- [ ] O que são agentes de IA (definição formal)
- [ ] Autonomia em agentes
- [ ] Raciocínio vs Ação em agentes
- [ ] Por que agents são necessários vs prompting simples

**Importante:**
- [ ] História de AI agents (breve)
- [ ] Cognitive Architectures (conceito geral)
- [ ] SOAR, ACT-R (menção histórica)
- [ ] Comparação com RPA (Robotic Process Automation)

**Comparações de Frameworks:**
- [ ] LangChain vs DSPy
- [ ] AutoGen vs DSPy
- [ ] CrewAI vs DSPy
- [ ] Quando usar cada um

---

### Cap 2: DSPy Essentials

**Crítico (DSPy Core):**
- [ ] O que é DSPy (definição)
- [ ] Language Model Programs (conceito)
- [ ] Signatures (inputs/outputs estruturados)
- [ ] InputField vs OutputField
- [ ] Modules (componentes reutilizáveis)
- [ ] Predictors (wrappers de LLM)
- [ ] dspy.Module base class
- [ ] forward method
- [ ] ChainOfThought (o que é, quando usar)
- [ ] ReAct pattern (Reasoning + Acting)

**Importante:**
- [ ] Few-shot learning
- [ ] Zero-shot learning
- [ ] In-context learning
- [ ] Prompt engineering vs DSPy
- [ ] Teleprompters (conceito geral)

**Referências Necessárias:**
- [ ] DSPy paper (Khattab et al., 2023)
- [ ] ReAct paper (Yao et al., 2022)
- [ ] Chain-of-Thought paper (Wei et al., 2022)

---

### Cap 3: Primeiro Multi-Agent

**Crítico:**
- [ ] O que é sistema multi-agent
- [ ] Coordenação entre agentes
- [ ] Estado compartilhado (shared state)
- [ ] Comunicação inter-agent
- [ ] Trade-offs: single vs multi

**Importante:**
- [ ] Patterns de comunicação
- [ ] Synchronous vs asynchronous
- [ ] Message passing

---

## PARTE 2: ARQUITETURAS

### Conceitos Gerais (Aplicam a todos caps 4-7)

**Crítico:**
- [ ] O que são cognitive architectures
- [ ] Pattern vs Architecture
- [ ] Design patterns para agents
- [ ] Especialização vs Generalização
- [ ] Modularidade em sistemas multi-agent

**Trade-offs Analysis:**
- [ ] Latência
- [ ] Custo (tokens, chamadas)
- [ ] Complexidade de implementação
- [ ] Complexidade de debugging
- [ ] Manutenibilidade

---

### Cap 4: Sequential/Pipeline

**Crítico:**
- [ ] Pipeline pattern (conceito geral CS)
- [ ] Stages e boundaries
- [ ] Data flow
- [ ] Error propagation em pipelines
- [ ] Intermediate outputs

**Importante:**
- [ ] Unix pipes (analogia)
- [ ] MapReduce (menção)
- [ ] ETL pipelines (comparação)

---

### Cap 5: Hierarchical

**Crítico:**
- [ ] Coordinator-Specialist pattern
- [ ] Delegation
- [ ] Roteamento dinâmico
- [ ] Single point of failure
- [ ] Load balancing

**Importante:**
- [ ] Hierarchical systems em CS
- [ ] Manager-Worker pattern
- [ ] Master-Slave (menção histórica, terminologia antiga)

---

### Cap 6: Collaborative/Debate

**Crítico:**
- [ ] Debate pattern
- [ ] Consensus mechanisms
- [ ] Voting strategies
- [ ] Multiple perspectives
- [ ] Deliberation

**Importante:**
- [ ] Byzantine Generals Problem (menção)
- [ ] Consensus algorithms (breve)
- [ ] Multi-agent RL (menção)

---

### Cap 7: Reflexive/Self-Critique

**Crítico:**
- [ ] Actor-Critic pattern
- [ ] Self-improvement
- [ ] Feedback loops
- [ ] Convergence criteria
- [ ] Iterative refinement

**Importante:**
- [ ] Reinforcement Learning (contexto)
- [ ] Meta-learning (menção)
- [ ] Self-play (comparação)

**Referências Necessárias:**
- [ ] Reflexion paper (Shinn et al., 2023)
- [ ] Self-Refine paper

---

## PARTE 3: OTIMIZAÇÃO

### Cap 8: Fundamentos Otimização

**Crítico:**
- [ ] Optimization landscape
- [ ] Loss functions
- [ ] Gradient-based vs gradient-free
- [ ] Overfitting em LLM systems
- [ ] Train/val/test splits
- [ ] Cross-validation

**Métricas:**
- [ ] Accuracy
- [ ] Precision
- [ ] Recall
- [ ] F1 score
- [ ] Custom metrics
- [ ] Statistical significance

**Desafios Multi-Agent:**
- [ ] Combinatorial explosion
- [ ] Credit assignment problem
- [ ] Coordinated overfitting
- [ ] Joint optimization

**Importante:**
- [ ] Hyperparameter optimization
- [ ] Grid search, random search
- [ ] Bayesian optimization (menção)

---

### Cap 9: BootstrapFewShot & MIPRO

**Crítico:**
- [ ] Bootstrapping (conceito)
- [ ] Few-shot prompting
- [ ] Demonstrations
- [ ] MIPRO algorithm
- [ ] Candidate generation
- [ ] Proposal functions
- [ ] Trial evaluation

**Importante:**
- [ ] Prompt optimization landscape
- [ ] Automatic prompt engineering
- [ ] Meta-prompting

**Referências Necessárias:**
- [ ] MIPRO paper (Opsahl-Ong et al., 2024)
- [ ] DSPy optimization docs

---

### Cap 10: Custom Optimizers

**Crítico:**
- [ ] Alternating optimization
- [ ] Backward optimization
- [ ] Multi-objective optimization
- [ ] Reward shaping
- [ ] Meta-prompting para coordenação

**Importante:**
- [ ] Pareto optimality
- [ ] Scalarization de objetivos
- [ ] Curriculum learning (menção)

---

### Cap 11: Métricas e Evaluation

**Crítico:**
- [ ] Composed metrics
- [ ] Metric aggregation strategies
- [ ] Dataset construction
- [ ] Data augmentation
- [ ] Intermediate supervision
- [ ] Langfuse para evaluation

**Importante:**
- [ ] Metric design principles
- [ ] Proxy metrics
- [ ] Leading vs lagging indicators

---

### Cap 12: Optimization Mastery

**Crítico:**
- [ ] Production optimization
- [ ] A/B testing de otimizações
- [ ] Statistical power
- [ ] Sample size calculation

**Importante:**
- [ ] Online learning (menção)
- [ ] Contextual bandits (menção)

---

### Cap 13: Fine-Tuning

**Crítico:**
- [ ] Fine-tuning vs optimization (diferença fundamental)
- [ ] Transfer learning
- [ ] Domain adaptation
- [ ] Catastrophic forgetting
- [ ] Parameter-efficient fine-tuning (PEFT)
- [ ] LoRA, QLoRA

**Dataset:**
- [ ] Dataset preparation
- [ ] Data formatting
- [ ] Quality assurance
- [ ] Data privacy

**Training:**
- [ ] Training loop
- [ ] Learning rate scheduling
- [ ] Early stopping
- [ ] Checkpoint management

**Multi-Agent Specific:**
- [ ] Per-agent fine-tuning
- [ ] Global model fine-tuning
- [ ] Specialist vs generalist trade-off

**Importante:**
- [ ] Full fine-tuning vs PEFT
- [ ] Instruction tuning
- [ ] RLHF (menção)
- [ ] DPO (menção)

---

## PARTE 4: PRODUCTION

### Cap 14: Arquiteturas de Referência

**Crítico:**
- [ ] Enterprise tool architecture
- [ ] Tool registry pattern
- [ ] State management strategies
- [ ] Shared state vs isolated state
- [ ] Consistency models (eventual, strong)
- [ ] CQRS pattern
- [ ] Event Sourcing

**Communication:**
- [ ] Synchronous vs asynchronous
- [ ] Message queues
- [ ] Event buses
- [ ] Pub/Sub pattern

**Integration:**
- [ ] Facade pattern
- [ ] Adapter pattern
- [ ] Gateway pattern
- [ ] Legacy system integration

---

### Cap 15: LLMOps

**Crítico:**
- [ ] MLOps vs LLMOps
- [ ] Continuous learning
- [ ] Feedback loops
- [ ] Data flywheel
- [ ] Drift detection
- [ ] Degradation detection

**Pipelines:**
- [ ] CI/CD para ML
- [ ] Automated retraining
- [ ] Automated deployment
- [ ] Model versioning
- [ ] Experiment tracking

**Observability:**
- [ ] Traces, metrics, logs
- [ ] OpenTelemetry
- [ ] Distributed tracing

---

### Cap 16: Scaling

**Crítico:**
- [ ] Horizontal vs vertical scaling
- [ ] Stateless vs stateful services
- [ ] Load balancing
- [ ] Service mesh
- [ ] Caching strategies
- [ ] Cache invalidation
- [ ] TTL policies

**Performance:**
- [ ] Latency vs throughput
- [ ] P50, P95, P99
- [ ] Amdahl's Law (menção)
- [ ] Bottleneck analysis

**Cost:**
- [ ] Cost models
- [ ] Token economics
- [ ] Cost attribution
- [ ] ROI calculation

---

### Cap 17: Case Studies

**Framework de Análise:**
- [ ] Problem framing
- [ ] Requirements gathering
- [ ] Architecture selection criteria
- [ ] Trade-off analysis
- [ ] Success metrics definition
- [ ] Post-mortem analysis

**Decision Framework:**
- [ ] Decision matrices
- [ ] Scoring models
- [ ] Risk assessment
- [ ] Cost-benefit analysis

---

## APÊNDICES

### Apêndice B: Deployment

**Conceitos:**
- [ ] Containerization (Docker)
- [ ] Orchestration (Kubernetes)
- [ ] Serverless
- [ ] API design (REST, GraphQL)
- [ ] Rate limiting
- [ ] Authentication & Authorization

---

### Apêndice C: Observability

**Tools:**
- [ ] Langfuse setup
- [ ] Arize Phoenix setup
- [ ] Prometheus
- [ ] Grafana
- [ ] ELK stack (menção)

---

### Apêndice D: Security

**Conceitos:**
- [ ] OWASP Top 10
- [ ] Input validation
- [ ] Output sanitization
- [ ] SQL injection (analogia)
- [ ] Prompt injection
- [ ] GDPR
- [ ] SOC2
- [ ] HIPAA

---

## Fundamentos de Computação/Matemática

**A explicar quando necessário:**
- [ ] Big O notation
- [ ] Distributed systems basics
- [ ] CAP theorem (menção)
- [ ] Eventual consistency
- [ ] Idempotency
- [ ] Exponential backoff
- [ ] Circuit breaker pattern
- [ ] Rate limiting algorithms

**Matemática/Estatística:**
- [ ] Probability basics
- [ ] Expected value
- [ ] Variance
- [ ] Normal distribution
- [ ] Statistical tests (t-test, chi-square)
- [ ] Confidence intervals
- [ ] P-values

---

## Priorização

### CRÍTICO (deve estar no livro):
- Todos marcados como "Crítico" acima

### IMPORTANTE (contexto necessário):
- Todos marcados como "Importante" acima

### NICE-TO-HAVE (menções breves):
- Conceitos avançados
- Comparações
- História

---

## Estratégia de Explicação

**Para cada conceito:**
1. Definição clara
2. Por que é importante
3. Exemplo prático
4. Quando usar/não usar
5. Referências (se acadêmico)

**Formato:**
```markdown
### Conceito: Nome

**Definição:** ...

**Por que importa:** ...

**Exemplo:**
```python
# Código ilustrativo
```

**Quando usar:** ...

**Referências:** [Author, Year]
```

---

## Status

- [ ] Lista completa
- [ ] Priorização feita
- [ ] Distribuição por capítulos
- [ ] Referências mapeadas
- [ ] Começar explicações

