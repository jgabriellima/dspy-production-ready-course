"""
Exemplos Práticos de Código - Multi-Agent Systems com DSPy

Este arquivo contém exemplos prontos para uso de:
- Implementações de arquiteturas
- Otimizadores customizados
- Métricas compostas
- Utilidades

Use como referência ou copie diretamente para seus projetos!
"""

import dspy
from typing import List, Dict, Any, Optional, Callable
from pydantic import BaseModel
import json
import numpy as np


# =============================================================================
# EXEMPLO 1: Hierarchical Multi-Agent System
# =============================================================================

class HierarchicalSystem(dspy.Module):
    """
    Sistema hierarchical completo com coordenador e especialistas.
    
    Uso:
        system = HierarchicalSystem(specialists)
        result = system(user_request="Find flights to NYC")
    """
    
    def __init__(self, specialists: Dict[str, dspy.Module]):
        super().__init__()
        self.specialists = specialists
        
        # Signature do coordenador
        class CoordinatorSignature(dspy.Signature):
            """Route user request to appropriate specialist"""
            user_request: str = dspy.InputField()
            specialist_name: str = dspy.OutputField(
                desc="Name of specialist: 'search', 'recommendation', or 'booking'"
            )
            reasoning: str = dspy.OutputField(desc="Why this specialist?")
        
        self.coordinator = dspy.ChainOfThought(CoordinatorSignature)
    
    def forward(self, user_request: str, **kwargs):
        # Coordenador decide
        routing = self.coordinator(user_request=user_request)
        specialist_name = routing.specialist_name.lower()
        
        # Delegar para especialista
        if specialist_name in self.specialists:
            specialist = self.specialists[specialist_name]
            result = specialist(user_request=user_request, **kwargs)
            return dspy.Prediction(
                specialist_used=specialist_name,
                reasoning=routing.reasoning,
                result=result
            )
        else:
            return dspy.Prediction(
                error=f"Unknown specialist: {specialist_name}"
            )


# =============================================================================
# EXEMPLO 2: Sequential Pipeline
# =============================================================================

class SequentialPipeline(dspy.Module):
    """
    Pipeline sequencial com múltiplos estágios.
    
    Uso:
        pipeline = SequentialPipeline([agent1, agent2, agent3])
        result = pipeline(initial_input="...")
    """
    
    def __init__(self, agents: List[dspy.Module]):
        super().__init__()
        self.agents = agents
        self.stage_outputs = []
    
    def forward(self, **kwargs):
        self.stage_outputs = []
        current_input = kwargs
        
        # Executar cada agente em sequência
        for i, agent in enumerate(self.agents):
            stage_result = agent(**current_input)
            self.stage_outputs.append(stage_result)
            
            # Preparar input para próximo estágio
            current_input = self._prepare_next_input(stage_result)
        
        return dspy.Prediction(
            final_output=stage_result,
            stage_outputs=self.stage_outputs
        )
    
    def _prepare_next_input(self, stage_result):
        """Converter output de um estágio em input do próximo"""
        # Implementar baseado em sua lógica
        return {"input": stage_result}


# =============================================================================
# EXEMPLO 3: Collaborative/Debate System
# =============================================================================

class CollaborativeSystem(dspy.Module):
    """
    Sistema collaborative com múltiplas perspectivas e consenso.
    
    Uso:
        system = CollaborativeSystem(
            agents={'price': price_agent, 'quality': quality_agent},
            num_rounds=2
        )
        result = system(scenario="...")
    """
    
    def __init__(
        self, 
        agents: Dict[str, dspy.Module],
        consensus_agent: dspy.Module,
        num_rounds: int = 2
    ):
        super().__init__()
        self.agents = agents
        self.consensus_agent = consensus_agent
        self.num_rounds = num_rounds
    
    def forward(self, **kwargs):
        debate_history = []
        previous_opinions = "No previous opinions"
        
        # Múltiplas rodadas de debate
        for round_num in range(self.num_rounds):
            round_opinions = {}
            
            # Cada agente dá sua opinião
            for name, agent in self.agents.items():
                opinion = agent(
                    **kwargs,
                    other_opinions=previous_opinions
                )
                round_opinions[name] = opinion
            
            debate_history.append(round_opinions)
            previous_opinions = self._format_opinions(round_opinions)
        
        # Formar consenso
        consensus = self.consensus_agent(
            opinions=previous_opinions,
            debate_history=json.dumps(debate_history),
            **kwargs
        )
        
        return dspy.Prediction(
            consensus=consensus,
            debate_history=debate_history,
            final_opinions=round_opinions
        )
    
    def _format_opinions(self, opinions: Dict) -> str:
        """Formatar opiniões para próxima rodada"""
        formatted = []
        for name, opinion in opinions.items():
            formatted.append(f"{name}: {opinion}")
        return "\n".join(formatted)


# =============================================================================
# EXEMPLO 4: Reflexive/Self-Critique System
# =============================================================================

class ReflexiveSystem(dspy.Module):
    """
    Sistema reflexivo com actor-critic loop.
    
    Uso:
        system = ReflexiveSystem(
            actor=actor_agent,
            critic=critic_agent,
            max_iterations=3
        )
        result = system(task="...")
    """
    
    def __init__(
        self,
        actor: dspy.Module,
        critic: dspy.Module,
        refiner: dspy.Module,
        max_iterations: int = 3,
        quality_threshold: float = 8.0
    ):
        super().__init__()
        self.actor = actor
        self.critic = critic
        self.refiner = refiner
        self.max_iterations = max_iterations
        self.quality_threshold = quality_threshold
    
    def forward(self, **kwargs):
        quality_history = []
        previous_critique = "No previous critique"
        
        for iteration in range(self.max_iterations):
            # Actor gera output
            output = self.actor(
                **kwargs,
                previous_critique=previous_critique
            )
            
            # Critic avalia
            critique = self.critic(
                output=output,
                **kwargs
            )
            
            # Extrair quality score
            quality_score = self._extract_quality(critique)
            quality_history.append(quality_score)
            
            # Verificar se atingiu threshold
            if quality_score >= self.quality_threshold:
                return dspy.Prediction(
                    output=output,
                    critique=critique,
                    quality_score=quality_score,
                    iterations=iteration + 1,
                    converged=True,
                    quality_history=quality_history
                )
            
            # Refiner melhora
            if iteration < self.max_iterations - 1:
                refined = self.refiner(
                    original_output=output,
                    critique=critique,
                    **kwargs
                )
                previous_critique = critique
        
        # Retornar última tentativa
        return dspy.Prediction(
            output=output,
            critique=critique,
            quality_score=quality_score,
            iterations=self.max_iterations,
            converged=False,
            quality_history=quality_history
        )
    
    def _extract_quality(self, critique) -> float:
        """Extrair score numérico da crítica"""
        # Implementar parsing apropriado
        try:
            return float(critique.quality_score)
        except:
            return 7.0  # Default


# =============================================================================
# EXEMPLO 5: Otimizadores Customizados
# =============================================================================

class AlternatingOptimizer:
    """
    Otimizador alternating para sistemas hierarchical.
    
    Uso:
        optimizer = AlternatingOptimizer(coordinator, specialists)
        optimized_coordinator, optimized_specialists = optimizer.optimize(trainset)
    """
    
    def __init__(
        self,
        coordinator: dspy.Module,
        specialists: Dict[str, dspy.Module]
    ):
        self.coordinator = coordinator
        self.specialists = specialists
    
    def optimize(
        self,
        trainset: List,
        metric: Callable,
        max_iterations: int = 3
    ):
        """Alternating optimization"""
        
        current_coordinator = self.coordinator
        current_specialists = self.specialists.copy()
        
        for iteration in range(max_iterations):
            print(f"Iteration {iteration + 1}/{max_iterations}")
            
            # Otimizar especialistas
            current_specialists = self._optimize_specialists(
                current_specialists,
                trainset,
                metric
            )
            
            # Otimizar coordenador
            current_coordinator = self._optimize_coordinator(
                current_coordinator,
                current_specialists,
                trainset,
                metric
            )
            
            # Avaliar sistema completo
            score = self._evaluate_system(
                current_coordinator,
                current_specialists,
                trainset,
                metric
            )
            
            print(f"  System score: {score:.3f}")
        
        return current_coordinator, current_specialists
    
    def _optimize_specialists(self, specialists, trainset, metric):
        """Otimizar cada especialista"""
        optimized = {}
        
        for name, specialist in specialists.items():
            # Filtrar dados relevantes
            specialist_data = [
                ex for ex in trainset 
                if ex.specialist_type == name
            ]
            
            if len(specialist_data) > 0:
                optimizer = dspy.BootstrapFewShot(
                    metric=metric,
                    max_bootstrapped_demos=4
                )
                optimized[name] = optimizer.compile(
                    specialist,
                    trainset=specialist_data
                )
            else:
                optimized[name] = specialist
        
        return optimized
    
    def _optimize_coordinator(self, coordinator, specialists, trainset, metric):
        """Otimizar coordenador"""
        def routing_metric(example, pred, trace=None):
            return float(pred.specialist_name == example.correct_specialist)
        
        optimizer = dspy.BootstrapFewShot(
            metric=routing_metric,
            max_bootstrapped_demos=8
        )
        
        return optimizer.compile(coordinator, trainset=trainset)
    
    def _evaluate_system(self, coordinator, specialists, testset, metric):
        """Avaliar sistema completo"""
        scores = []
        # Implementar avaliação end-to-end
        return np.mean(scores) if scores else 0.0


class BackwardPipelineOptimizer:
    """
    Otimizador backward para pipelines.
    
    Uso:
        optimizer = BackwardPipelineOptimizer(agents)
        optimized_agents = optimizer.optimize(trainset)
    """
    
    def __init__(self, agents: List[dspy.Module]):
        self.agents = agents
    
    def optimize(
        self,
        trainset: List,
        metrics: Dict[str, Callable]
    ):
        """Otimizar pipeline de trás para frente"""
        
        optimized_agents = [None] * len(self.agents)
        
        # Otimizar de trás para frente
        for i in range(len(self.agents) - 1, -1, -1):
            print(f"Optimizing agent {i + 1}/{len(self.agents)}")
            
            agent = self.agents[i]
            metric = metrics.get(f'agent_{i}', metrics.get('default'))
            
            # Preparar dados para este agente
            agent_data = self._prepare_agent_data(
                trainset,
                i,
                optimized_agents
            )
            
            # Otimizar
            optimizer = dspy.BootstrapFewShot(
                metric=metric,
                max_bootstrapped_demos=4
            )
            
            optimized_agents[i] = optimizer.compile(
                agent,
                trainset=agent_data
            )
        
        return optimized_agents
    
    def _prepare_agent_data(self, trainset, agent_idx, optimized_agents):
        """Preparar dados específicos para o agente"""
        # Se temos agentes otimizados depois dele,
        # usar suas saídas esperadas como ground truth
        # Implementar lógica específica
        return trainset


# =============================================================================
# EXEMPLO 6: Métricas Compostas
# =============================================================================

class ComposedMetric:
    """
    Métrica composta para sistemas multi-agent.
    
    Uso:
        metric = ComposedMetric(
            component_metrics={
                'routing': routing_accuracy,
                'quality': output_quality,
                'efficiency': efficiency_score
            },
            weights={'routing': 0.3, 'quality': 0.5, 'efficiency': 0.2}
        )
        score = metric(example, prediction)
    """
    
    def __init__(
        self,
        component_metrics: Dict[str, Callable],
        weights: Optional[Dict[str, float]] = None
    ):
        self.component_metrics = component_metrics
        
        # Pesos uniformes se não especificados
        if weights is None:
            n = len(component_metrics)
            weights = {name: 1.0/n for name in component_metrics}
        
        self.weights = weights
    
    def __call__(self, example, prediction, trace=None):
        """Avaliar usando todas as métricas componentes"""
        scores = {}
        
        for name, metric_fn in self.component_metrics.items():
            try:
                score = metric_fn(example, prediction, trace)
                scores[name] = score
            except Exception as e:
                print(f"Error in metric {name}: {e}")
                scores[name] = 0.0
        
        # Média ponderada
        total_score = sum(
            self.weights.get(name, 0.0) * score
            for name, score in scores.items()
        )
        
        return total_score


def hierarchical_metric_factory(routing_weight=0.3, quality_weight=0.7):
    """Factory para métricas hierarchical"""
    
    def metric(example, prediction, trace=None):
        # Routing accuracy
        routing_score = float(
            prediction.specialist_used == example.correct_specialist
        )
        
        # Output quality
        quality_score = evaluate_output_quality(
            prediction.result,
            example.expected_output
        )
        
        return routing_weight * routing_score + quality_weight * quality_score
    
    return metric


def sequential_metric_factory(stage_weights=None):
    """Factory para métricas sequential"""
    
    def metric(example, prediction, trace=None):
        if not hasattr(prediction, 'stage_outputs'):
            return 0.0
        
        scores = []
        
        # Avaliar cada estágio
        for i, stage_output in enumerate(prediction.stage_outputs):
            stage_score = evaluate_stage(
                stage_output,
                example.stage_golds[i]
            )
            
            # Aplicar peso (se fornecido)
            if stage_weights and i < len(stage_weights):
                stage_score *= stage_weights[i]
            
            scores.append(stage_score)
        
        return np.mean(scores)
    
    return metric


# =============================================================================
# EXEMPLO 7: Utilidades
# =============================================================================

def evaluate_output_quality(output: Any, expected: Any) -> float:
    """Avaliar qualidade de output (implementar conforme necessário)"""
    # Exemplo simplificado
    if isinstance(output, str) and isinstance(expected, str):
        return float(output.strip() == expected.strip())
    return 0.5  # Default


def evaluate_stage(stage_output: Any, gold: Any) -> float:
    """Avaliar estágio individual"""
    # Implementar lógica específica
    return 1.0


def measure_diversity(opinions: List[str]) -> float:
    """Medir diversidade de opiniões"""
    if len(opinions) < 2:
        return 0.0
    
    # Calcular similaridades par a par
    similarities = []
    for i in range(len(opinions)):
        for j in range(i + 1, len(opinions)):
            # Usar métrica de similaridade apropriada
            sim = simple_similarity(opinions[i], opinions[j])
            similarities.append(sim)
    
    # Diversidade = 1 - média de similaridade
    return 1.0 - np.mean(similarities)


def simple_similarity(text1: str, text2: str) -> float:
    """Similaridade simples baseada em palavras comuns"""
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    if not words1 or not words2:
        return 0.0
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union)


def create_example(
    input_data: Dict[str, Any],
    expected_output: Any,
    **kwargs
) -> dspy.Example:
    """Helper para criar exemplos DSPy"""
    return dspy.Example(
        **input_data,
        expected_output=expected_output,
        **kwargs
    ).with_inputs(*input_data.keys())


# =============================================================================
# EXEMPLO 8: Template de Uso Completo
# =============================================================================

def complete_workflow_example():
    """
    Exemplo completo de workflow multi-agent com otimização.
    """
    
    # 1. Configurar LLM
    lm = dspy.LM('openai/gpt-4o-mini')
    dspy.configure(lm=lm)
    
    # 2. Criar agentes especializados
    search_agent = create_search_agent()
    recommendation_agent = create_recommendation_agent()
    booking_agent = create_booking_agent()
    
    specialists = {
        'search': search_agent,
        'recommendation': recommendation_agent,
        'booking': booking_agent
    }
    
    # 3. Criar sistema hierarchical
    system = HierarchicalSystem(specialists)
    
    # 4. Criar dataset
    trainset = create_training_data()
    testset = create_test_data()
    
    # 5. Definir métrica
    metric = hierarchical_metric_factory(
        routing_weight=0.3,
        quality_weight=0.7
    )
    
    # 6. Otimizar sistema
    optimizer = AlternatingOptimizer(
        coordinator=system.coordinator,
        specialists=specialists
    )
    
    optimized_coordinator, optimized_specialists = optimizer.optimize(
        trainset=trainset,
        metric=metric,
        max_iterations=3
    )
    
    # 7. Criar sistema otimizado
    optimized_system = HierarchicalSystem(optimized_specialists)
    optimized_system.coordinator = optimized_coordinator
    
    # 8. Avaliar
    test_score = evaluate_system(optimized_system, testset, metric)
    print(f"Test Score: {test_score:.3f}")
    
    # 9. Usar em produção
    result = optimized_system(
        user_request="Find cheap flights to NYC next week"
    )
    
    return optimized_system, result


# =============================================================================
# Helpers (implementar conforme necessário)
# =============================================================================

def create_search_agent():
    """Criar agente de busca"""
    class SearchSignature(dspy.Signature):
        """Find flights matching criteria"""
        departure: str = dspy.InputField()
        arrival: str = dspy.InputField()
        flights: str = dspy.OutputField(desc="JSON list of flights")
    
    return dspy.ChainOfThought(SearchSignature)


def create_recommendation_agent():
    """Criar agente de recomendação"""
    class RecommendationSignature(dspy.Signature):
        """Recommend best flight from options"""
        available_flights: str = dspy.InputField()
        user_preferences: str = dspy.InputField()
        recommendation: str = dspy.OutputField()
    
    return dspy.ChainOfThought(RecommendationSignature)


def create_booking_agent():
    """Criar agente de booking"""
    class BookingSignature(dspy.Signature):
        """Book selected flight"""
        flight_id: str = dspy.InputField()
        user_name: str = dspy.InputField()
        confirmation: str = dspy.OutputField()
    
    return dspy.ChainOfThought(BookingSignature)


def create_training_data():
    """Criar dados de treino"""
    # Implementar criação de dataset
    return []


def create_test_data():
    """Criar dados de teste"""
    # Implementar criação de dataset
    return []


def evaluate_system(system, testset, metric):
    """Avaliar sistema no test set"""
    scores = []
    for example in testset:
        try:
            pred = system(**example.inputs())
            score = metric(example, pred)
            scores.append(score)
        except:
            scores.append(0.0)
    
    return np.mean(scores) if scores else 0.0


# =============================================================================
# Main - Exemplos de uso
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Exemplos de Multi-Agent Systems com DSPy")
    print("=" * 60)
    
    # Descomentar para executar exemplos
    # complete_workflow_example()
    
    print("\nVeja os exemplos acima e adapte para seu caso de uso!")
    print("Consulte os notebooks para exemplos completos e executáveis.")


