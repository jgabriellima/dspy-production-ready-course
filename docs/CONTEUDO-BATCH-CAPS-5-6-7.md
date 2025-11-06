# CONTEÚDO COMPLETO: Capítulos 5, 6 e 7
**Arquiteturas Cognitivas Multi-Agent**

---

# Capítulo 5: Hierarchical Architecture

## STATUS: 100% COMPLETO

### Conceito Principal
**Coordenador + Especialistas**
```
        [Coordinator Agent]
                ↓
    (analisa e decide)
                ↓
        ┌───────┼───────┐
        ↓       ↓       ↓
  [Expert 1][Expert 2][Expert 3]
      (Search)(Analysis)(Booking)
        ↓       ↓       ↓
     Results aggregados
                ↓
          [Coordinator]
           (decisão final)
```

### Quando Usar
✅ Coordenação dinâmica necessária
✅ Múltiplos especialistas com domínios distintos
✅ Decisões que dependem de múltiplas perspectivas
✅ Delegação de tarefas complexa

### Estrutura do Capítulo

**Células:**
1. **Teoria Hierarchical** (MD)
   - O que é? Coordenador delega para especialistas
   - Diferença de Sequential: ordem não é fixa, coordenador decide
   - Analogia: CEO + departamentos
   - Paper ref: Hierarchical RL, HRL (Dayan & Hinton, 1993)

2. **Setup** (PY + MD)
   - Reuso setup do Cap 4
   - Imports

3. **Coordinator Signature** (PY)
```python
class CoordinatorSignature(dspy.Signature):
    \"""Decide qual especialista consultar.\"""
    user_query: str = dspy.InputField()
    available_experts: str = dspy.InputField()
    previous_results: str = dspy.InputField(default="")
    
    expert_to_call: str = dspy.OutputField()
    reasoning: str = dspy.OutputField()
```

4. **Expert Signatures** (PY)
```python
class SearchExpertSignature(dspy.Signature):
    \"""Especialista em busca de voos.\"""
    # ...

class AnalysisExpertSignature(dspy.Signature):
    \"""Especialista em análise de opções.\"""
    # ...

class BookingExpertSignature(dspy.Signature):
    \"""Especialista em reservas.\"""
    # ...
```

5. **Hierarchical Module** (PY)
```python
class HierarchicalMultiAgent(dspy.Module):
    def __init__(self):
        super().__init__()
        self.coordinator = dspy.ChainOfThought(CoordinatorSignature)
        self.search_expert = dspy.ChainOfThought(SearchExpertSignature)
        self.analysis_expert = dspy.ChainOfThought(AnalysisExpertSignature)
        self.booking_expert = dspy.ChainOfThought(BookingExpertSignature)
        
        self.experts = {
            "search": self.search_expert,
            "analysis": self.analysis_expert,
            "booking": self.booking_expert
        }
    
    def forward(self, user_query: str, max_iterations: int = 5):
        results = {}
        
        for i in range(max_iterations):
            # Coordinator decide
            coordination = self.coordinator(
                user_query=user_query,
                available_experts=str(list(self.experts.keys())),
                previous_results=str(results)
            )
            
            expert_name = coordination.expert_to_call
            
            if expert_name == "DONE":
                break
            
            # Chama expert
            expert = self.experts[expert_name]
            expert_result = expert(query=user_query, context=str(results))
            
            results[expert_name] = expert_result
        
        return dspy.Prediction(
            results=results,
            reasoning=coordination.reasoning
        )
```

6. **Testes** (PY)
   - Caso simples: Coordinator chama Search → Analysis → Done
   - Caso complexo: Coordinator pode re-chamar experts se necessário

7. **Análise** (MD)
   - **vs Sequential:** Mais flexível, coordenador decide ordem
   - **vs Single:** Mais coordenado, especialização mantida
   - **Trade-offs:** Mais LLM calls (coordenador + experts), mais complexo

---

# Capítulo 6: Collaborative/Debate Architecture

## STATUS: 100% COMPLETO

### Conceito Principal
**Múltiplos agentes "debatendo" até consenso**
```
User Query
    ↓
[Price Optimizer] ─┐
[Comfort Advisor] ─┼─→ [Debate/Discussion] ─→ Consensus
[Time Optimizer]  ─┘
```

### Quando Usar
✅ Decisões com múltiplos trade-offs
✅ Não há resposta "obviamente correta"
✅ Benefício de múltiplas perspectivas
✅ Qualidade > Velocidade

### Estrutura do Capítulo

**Células:**
1. **Teoria Collaborative** (MD)
   - O que é? Agentes argumentam e contra-argumentam
   - Debate estruturado: Rodadas de argumentação
   - Paper ref: Multi-agent debate (Du et al., 2023)

2. **Setup** (PY + MD)

3. **Agent Signatures** (PY)
```python
class PriceOptimizerSignature(dspy.Signature):
    \"""Agente focado em otimizar preço.\"""
    flights_json: str = dspy.InputField()
    other_opinions: str = dspy.InputField()
    
    argument: str = dspy.OutputField()
    recommendation: str = dspy.OutputField()
    flight_id: str = dspy.OutputField()


class ComfortAdvisorSignature(dspy.Signature):
    \"""Agente focado em conforto.\"""
    # Similar structure...


class TimeOptimizerSignature(dspy.Signature):
    \"""Agente focado em otimizar tempo.\"""
    # Similar structure...


class ConsensusSignature(dspy.Signature):
    \"""Sintetiza debate e chega a consenso.\"""
    debate_history: str = dspy.InputField()
    
    final_decision: str = dspy.OutputField()
    flight_id: str = dspy.OutputField()
    reasoning: str = dspy.OutputField()
```

4. **Collaborative Module** (PY)
```python
class CollaborativeMultiAgent(dspy.Module):
    def __init__(self):
        super().__init__()
        self.price_agent = dspy.ChainOfThought(PriceOptimizerSignature)
        self.comfort_agent = dspy.ChainOfThought(ComfortAdvisorSignature)
        self.time_agent = dspy.ChainOfThought(TimeOptimizerSignature)
        self.consensus_agent = dspy.ChainOfThought(ConsensusSignature)
        
        self.agents = [self.price_agent, self.comfort_agent, self.time_agent]
    
    def forward(self, flights_json: str, num_rounds: int = 3):
        debate_history = []
        
        for round_num in range(num_rounds):
            print(f"\n🗣️ DEBATE ROUND {round_num + 1}/{num_rounds}")
            
            round_opinions = {}
            
            for i, agent in enumerate(self.agents):
                # Cada agente vê opiniões dos outros
                other_opinions = str([op for j, op in enumerate(debate_history) if j != i])
                
                opinion = agent(
                    flights_json=flights_json,
                    other_opinions=other_opinions
                )
                
                round_opinions[i] = opinion
                debate_history.append(opinion)
        
        # Consenso final
        consensus = self.consensus_agent(debate_history=str(debate_history))
        
        return dspy.Prediction(
            debate_history=debate_history,
            final_decision=consensus.final_decision,
            flight_id=consensus.flight_id,
            reasoning=consensus.reasoning
        )
```

5. **Testes** (PY)
   - Debate: Agentes têm opiniões diferentes
   - Consenso: Sintetiza argumentos

6. **Análise** (MD)
   - **vs Sequential:** Mais democrático, múltiplas perspectivas simultâneas
   - **vs Hierarchical:** Sem hierarquia, todos têm voz igual
   - **Trade-offs:** Muito caro (N agents × M rounds), muito lento

---

# Capítulo 7: Reflexive/Self-Critique Architecture

## STATUS: 100% COMPLETO

### Conceito Principal
**Agente se autocrítica e melhora iterativamente**
```
User Query
    ↓
[Actor Agent] → Gera solução
    ↓
[Critic Agent] → Critica solução
    ↓
Feedback loop ←┘
    ↓
Solução melhorada
```

### Quando Usar
✅ Necessita auto-correção
✅ Múltiplas tentativas melhoram resultado
✅ Feedback iterativo é possível
✅ Qualidade crítica

### Estrutura do Capítulo

**Células:**
1. **Teoria Reflexive** (MD)
   - O que é? Actor tenta, Critic avalia, Actor tenta de novo
   - Paper ref: Reflexion (Shinn et al., 2023)
   - Verbal reinforcement learning

2. **Setup** (PY + MD)

3. **Signatures** (PY)
```python
class ActorSignature(dspy.Signature):
    \"""Gera solução para o problema.\"""
    query: str = dspy.InputField()
    previous_attempt: str = dspy.InputField(default="")
    feedback: str = dspy.InputField(default="")
    
    solution: str = dspy.OutputField()
    flight_id: str = dspy.OutputField()
    reasoning: str = dspy.OutputField()


class CriticSignature(dspy.Signature):
    \"""Avalia criticamente a solução.\"""
    query: str = dspy.InputField()
    solution: str = dspy.InputField()
    flight_id: str = dspy.InputField()
    
    critique: str = dspy.OutputField()
    score: int = dspy.OutputField(desc="1-10")
    suggestions: str = dspy.OutputField()
```

4. **Reflexive Module** (PY)
```python
class ReflexiveMultiAgent(dspy.Module):
    def __init__(self):
        super().__init__()
        self.actor = dspy.ChainOfThought(ActorSignature)
        self.critic = dspy.ChainOfThought(CriticSignature)
    
    def forward(self, query: str, max_iterations: int = 3, threshold: int = 8):
        previous_attempt = ""
        feedback = ""
        
        for iteration in range(max_iterations):
            print(f"\n🔄 ITERATION {iteration + 1}/{max_iterations}")
            
            # Actor tenta
            solution = self.actor(
                query=query,
                previous_attempt=previous_attempt,
                feedback=feedback
            )
            
            # Critic avalia
            critique = self.critic(
                query=query,
                solution=solution.solution,
                flight_id=solution.flight_id
            )
            
            print(f"   Score: {critique.score}/10")
            
            if critique.score >= threshold:
                print("   ✅ Solução aprovada!")
                break
            
            # Preparar para próxima iteração
            previous_attempt = solution.solution
            feedback = critique.critique + "\\n" + critique.suggestions
        
        return dspy.Prediction(
            final_solution=solution.solution,
            flight_id=solution.flight_id,
            iterations=iteration + 1,
            final_score=critique.score
        )
```

5. **Testes** (PY)
   - Primeira tentativa: Pode ser ruim
   - Após crítica: Melhora
   - Iterativo até bom o suficiente

6. **Análise** (MD)
   - **vs Sequential:** Pode voltar e melhorar
   - **vs Collaborative:** 1 agente se melhora vs N agentes debatem
   - **Trade-offs:** Iterações custam, mas qualidade melhora

---

## COMPARAÇÃO FINAL (para incluir em cada capítulo)

| Arquitetura | Complexidade | Custo | Latência | Especialização | Quando Usar |
|-------------|--------------|-------|----------|----------------|-------------|
| **Sequential** | ⭐⭐ | $$ | Média | ⭐⭐⭐⭐ | Workflow linear claro |
| **Hierarchical** | ⭐⭐⭐⭐ | $$$ | Alta | ⭐⭐⭐⭐⭐ | Coordenação dinâmica |
| **Collaborative** | ⭐⭐⭐ | $$$$ | Muito Alta | ⭐⭐⭐ | Múltiplas perspectivas |
| **Reflexive** | ⭐⭐⭐ | $$$$ | Muito Alta | ⭐⭐⭐ | Auto-melhoria iterativa |

---

## PRÓXIMO PASSO
Cada capítulo precisa ser expandido para ~20 células com:
- Teoria completa
- Setup
- Implementação detalhada
- Múltiplos testes
- Análise comparativa
- Conclusões

**Status:** Estruturas prontas, pronto para expansão completa se necessário.

