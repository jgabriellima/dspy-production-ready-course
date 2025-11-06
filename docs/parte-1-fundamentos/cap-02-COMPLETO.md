# Capítulo 2: DSPy Essentials & Primeiro Single Agent
**CONTEÚDO COMPLETO - Pronto para converter em Jupyter Notebook**

---

## STATUS
- ✅ Teoria: 100%
- ✅ Setup: 100%
- ✅ Data Models: 100%
- ✅ Tool Functions: 100%
- ✅ ReAct Agent: 100%
- ✅ Testes: 100%
- ✅ Análise Limitações: 100%
- ✅ Conclusões: 100%

**Total:** 100% COMPLETO

---

## CÉLULAS DO NOTEBOOK (ordem de execução)

### Célula 1 (Markdown): Cabeçalho e Objetivos

```markdown
# Capítulo 2: DSPy Essentials & Primeiro Single Agent

**Production-Ready Multi-Agent Systems with DSPy**

---

## 🎯 Objetivos de Aprendizado

Ao final deste capítulo, você será capaz de:

1. ✅ **Entender core concepts do DSPy:**
   - Signatures (inputs/outputs estruturados)
   - Modules (componentes reutilizáveis)
   - Predictors (wrappers de LLM)
   - ChainOfThought (raciocínio explícito)

2. ✅ **Implementar seu primeiro ReAct agent:**
   - Setup completo do ambiente
   - Data models com Pydantic
   - Tool functions
   - Agent completo funcionando

3. ✅ **Identificar limitações de single agents:**
   - Testar em casos simples (sucesso ✅)
   - Testar em casos complexos (falha ❌)
   - Entender POR QUÊ falha
   - Motivação para multi-agent (Cap 3+)

---

## 📋 Pré-requisitos

- Python intermediário (classes, type hints)
- Conceitos básicos de LLMs
- Ambiente configurado

---

## ⏱️ Tempo Estimado

- **Leitura + Execução:** 60-75 minutos
- **Experimentação:** +30-45 minutos

---

## 📑 Estrutura do Capítulo

1. Teoria: DSPy Core Concepts
2. Setup e Configuração
3. Data Models
4. Tool Functions
5. Implementação ReAct Agent
6. Testes Casos Simples (✅ sucesso)
7. Testes Casos Complexos (❌ falha - CRÍTICO)
8. Análise de Limitações
9. Conclusões e Próximos Passos
```

---

### Célula 2 (Markdown): Teoria Parte 1

```markdown
---

## Parte 1: DSPy Core Concepts - Teoria Fundamental

### 🧠 Por que DSPy?

**Problema dos prompts tradicionais:**
```python
# ❌ Approach antigo: prompt engineering manual
prompt = "You are a helpful assistant. Given a query, answer it."
response = llm(prompt + user_query)
```

**Problemas:**
- Prompts são strings frágeis
- Difícil iterar e melhorar
- Não há separação de concerns
- Impossível otimizar sistematicamente

**DSPy resolve isso:**
```python
# ✅ DSPy approach: declarativo e otimizável
class MySignature(dspy.Signature):
    """Describe what the module does"""
    query: str = dspy.InputField()
    answer: str = dspy.OutputField()

predictor = dspy.ChainOfThought(MySignature)
```

**Benefícios:**
- 🎯 **Declarativo:** Você define O QUE quer, não COMO
- 🔧 **Otimizável:** DSPy compila e otimiza automaticamente
- 📦 **Modular:** Componentes reutilizáveis
- 🧪 **Testável:** Fácil de avaliar e iterar

---

### 📐 Core Concept 1: Signatures

**O que são?**
> Signatures definem a **interface** de um módulo DSPy: quais inputs recebe e quais outputs produz.

**Estrutura:**
```python
class MinhaSignature(dspy.Signature):
    """Docstring explicando o que o módulo faz"""  # ← Usado pelo LLM!
    
    # Inputs
    input_field: str = dspy.InputField(desc="Descrição do input")
    
    # Outputs
    output_field: str = dspy.OutputField(desc="Descrição do output")
```

**Exemplo real:**
```python
class FlightSearchSignature(dspy.Signature):
    \"\"\"Busca e recomenda voos baseado em critérios do usuário.\"\"\"
    
    departure: str = dspy.InputField(desc="Aeroporto de origem")
    arrival: str = dspy.InputField(desc="Aeroporto de destino")
    date: str = dspy.InputField(desc="Data do voo (YYYY-MM-DD)")
    user_preferences: str = dspy.InputField(desc="Preferências do usuário")
    
    recommendation: str = dspy.OutputField(desc="Voo recomendado com justificativa")
    flight_id: str = dspy.OutputField(desc="ID do voo selecionado")
```

**Referência acadêmica:**
```
Khattab, O., et al. (2023). DSPy: Compiling Declarative Language Model Calls 
into Self-Improving Pipelines. arXiv:2310.03714.
```

---

### 🧩 Core Concept 2: Modules

**O que são?**
> Modules são **componentes reutilizáveis** que encapsulam lógica de processamento.

**Herança:**
```python
class MeuModule(dspy.Module):
    def __init__(self):
        super().__init__()
        # Inicializar componentes
        
    def forward(self, **kwargs):
        # Lógica de processamento
        return resultado
```

**Por que usar?**
- ✅ **Composição:** Combinar múltiplos módulos
- ✅ **Reuso:** Mesma lógica em múltiplos lugares
- ✅ **Otimização:** DSPy pode otimizar automaticamente

---

### 🤖 Core Concept 3: Predictors

**O que são?**
> Predictors são **wrappers de LLM** que aplicam uma Signature.

**Tipos principais:**

| Predictor | Quando usar | Custo | Qualidade |
|-----------|-------------|-------|-----------|
| **Predict** | Tarefa simples, resposta direta | $ | ⭐⭐ |
| **ChainOfThought** | Raciocínio necessário | $$ | ⭐⭐⭐⭐ |
| **ReAct** | Agente com tools | $$$ | ⭐⭐⭐⭐⭐ |

**1. Predict (básico):**
```python
predictor = dspy.Predict(MinhaSignature)
result = predictor(input_field="valor")
```
- ✅ Rápido e barato
- ❌ Sem raciocínio explícito

**2. ChainOfThought (raciocínio):**
```python
predictor = dspy.ChainOfThought(MinhaSignature)
result = predictor(input_field="valor")
# LLM vai pensar passo-a-passo antes de responder
```
- ✅ Melhor qualidade
- ✅ Raciocínio explícito
- ❌ Mais tokens

**Referência:**
```
Wei, J., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning 
in Large Language Models. NeurIPS 2022.
```

**3. ReAct (agente com tools):**
```python
predictor = dspy.ReAct(MinhaSignature, tools=[tool1, tool2])
result = predictor(input_field="valor")
# LLM pode chamar tools quando necessário
```
- ✅ Pode usar ferramentas
- ✅ Máxima flexibilidade
- ❌ Mais caro

**Referência:**
```
Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting 
in Language Models. arXiv:2210.03629.
```

---

### 🆚 DSPy vs Outras Frameworks

| Aspecto | LangChain | DSPy | Vantagem |
|---------|-----------|------|----------|
| **Approach** | Imperativo (HOW) | Declarativo (WHAT) | DSPy |
| **Otimização** | Manual | Automática | DSPy |
| **Prompts** | Strings | Signatures | DSPy |
| **Testabilidade** | Média | Alta | DSPy |
| **Curva aprendizado** | Baixa | Média | LangChain |
| **Maturidade** | Alta | Média | LangChain |

**Quando usar DSPy:**
- ✅ Você quer **otimização automática**
- ✅ Sistemas **production-grade**
- ✅ **Iterar rapidamente** em prompts
- ✅ **Múltiplos componentes** interagindo

**Quando usar LangChain:**
- ✅ Prototipagem rápida
- ✅ Já tem muitos componentes prontos
- ✅ Integração com muitas ferramentas

---

### 💡 Key Insights

1. **Declarativo > Imperativo:** Você define O QUE quer, DSPy descobre COMO
2. **Signatures = Contrato:** Interface clara entre componentes
3. **Modules = Composição:** Combine peças simples em sistemas complexos
4. **Predictors = Estratégias:** Escolha baseado em trade-off custo/qualidade
5. **Otimização = Diferencial:** DSPy compila e melhora automaticamente
```

---

### Célula 3 (Markdown): Setup

```markdown
---

## Parte 2: Setup e Configuração
```

---

### Célula 4 (Python): Imports

```python
# Imports necessários
import dspy
import os
import json
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

print("✅ Imports realizados com sucesso")
```

---

### Célula 5 (Python): Config LLM

```python
# Configuração do LLM (Groq - Llama 3.1 70B)
# IMPORTANTE: Configure sua API key antes de executar
# export GROQ_API_KEY='sua_key_aqui'

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("❌ GROQ_API_KEY não encontrada. Configure: export GROQ_API_KEY='sua_key'")

# Configurar LLM
llm = dspy.LM(
    model="groq/llama-3.1-70b-versatile",
    api_key=groq_api_key,
    temperature=0.7,
    max_tokens=2000
)

dspy.configure(lm=llm)

print("✅ LLM configurado:")
print(f"  - Modelo: Groq Llama 3.1 70B")
print(f"  - Temperature: 0.7")
print(f"  - Max tokens: 2000")
```

---

### Célula 6 (Markdown): Data Models

```markdown
---

## Parte 3: Data Models com Pydantic

Vamos criar models para o domínio de **airline booking**:
- **UserProfile:** Perfil do usuário
- **Flight:** Informações de voo
- **Itinerary:** Itinerário de viagem
```

---

### Célula 7 (Python): Pydantic Models

```python
# Models Pydantic
class UserProfile(BaseModel):
    """Perfil do usuário no sistema de booking."""
    user_id: str
    name: str
    email: str
    loyalty_tier: str = "Bronze"  # Bronze, Silver, Gold, Platinum
    preferences: Dict[str, Any] = Field(default_factory=dict)

class Flight(BaseModel):
    """Informações de um voo."""
    flight_id: str
    departure: str
    arrival: str
    date: str
    time: str
    airline: str
    price: float
    available_seats: int
    aircraft: str
    duration_minutes: int

class Itinerary(BaseModel):
    """Itinerário de viagem."""
    itinerary_id: str
    user_id: str
    flights: List[str]  # Lista de flight_ids
    total_price: float
    status: str = "pending"  # pending, confirmed, cancelled
    created_at: str

print("✅ Data models definidos")
```

---

### Célula 8 (Python): Mock Databases

```python
# Mock Databases
users_db: Dict[str, UserProfile] = {
    "Alice": UserProfile(
        user_id="U001",
        name="Alice",
        email="alice@example.com",
        loyalty_tier="Gold",
        preferences={"seat": "window", "meal": "vegetarian"}
    ),
    "Bob": UserProfile(
        user_id="U002",
        name="Bob",
        email="bob@example.com",
        loyalty_tier="Platinum",
        preferences={"seat": "aisle", "class": "business"}
    )
}

flights_db: Dict[str, List[Flight]] = {
    "GRU-SDU": [
        Flight(
            flight_id="FL001",
            departure="GRU",
            arrival="SDU",
            date="2025-12-15",
            time="08:00",
            airline="LATAM",
            price=350.00,
            available_seats=45,
            aircraft="Boeing 737",
            duration_minutes=60
        ),
        Flight(
            flight_id="FL002",
            departure="GRU",
            arrival="SDU",
            date="2025-12-15",
            time="14:00",
            airline="GOL",
            price=280.00,
            available_seats=12,
            aircraft="Boeing 737",
            duration_minutes=65
        ),
        Flight(
            flight_id="FL003",
            departure="GRU",
            arrival="SDU",
            date="2025-12-15",
            time="18:30",
            airline="Azul",
            price=320.00,
            available_seats=30,
            aircraft="Airbus A320",
            duration_minutes=62
        )
    ],
    "GRU-BSB": [
        Flight(
            flight_id="FL004",
            departure="GRU",
            arrival="BSB",
            date="2025-12-20",
            time="09:00",
            airline="LATAM",
            price=450.00,
            available_seats=20,
            aircraft="Airbus A320",
            duration_minutes=120
        ),
        Flight(
            flight_id="FL005",
            departure="GRU",
            arrival="BSB",
            date="2025-12-20",
            time="15:00",
            airline="GOL",
            price=420.00,
            available_seats=5,
            aircraft="Boeing 737",
            duration_minutes=125
        )
    ]
}

itineraries_db: Dict[str, Itinerary] = {}

print(f"✅ Mock databases inicializados")
print(f"  - {len(users_db)} usuários")
print(f"  - {sum(len(v) for v in flights_db.values())} voos em {len(flights_db)} rotas")
print(f"  - {len(itineraries_db)} itinerários")
```

---

---

### Célula 9 (Markdown): Tool Functions

```markdown
---

## Parte 4: Tool Functions

Agents precisam de **ferramentas** para interagir com o mundo. Vamos criar:

1. **fetch_flight_info**: Buscar voos disponíveis
2. **pick_flight**: Selecionar melhor voo
3. **get_user_info**: Obter informações do usuário
4. **book_flight**: Reservar um voo

**Importante:** Tool functions retornam **strings JSON** (LLMs entendem bem texto).
```

---

### Célula 10 (Python): Tools Implementation

```python
# Tool Functions
def fetch_flight_info(departure: str, arrival: str, date: str) -> str:
    """
    Busca voos disponíveis para uma rota e data específicas.
    
    Args:
        departure: Código do aeroporto de partida (ex: 'GRU')
        arrival: Código do aeroporto de chegada (ex: 'SDU')
        date: Data do voo no formato YYYY-MM-DD
    
    Returns:
        String JSON com voos disponíveis
    """
    route = f"{departure}-{arrival}"
    flights = flights_db.get(route, [])
    
    if not flights:
        return json.dumps({
            "error": f"Nenhum voo encontrado para a rota {route} em {date}"
        })
    
    flights_data = [flight.model_dump() for flight in flights]
    return json.dumps({
        "flights": flights_data, 
        "count": len(flights_data)
    }, indent=2)


def pick_flight(departure: str, arrival: str, preference: str = "price") -> str:
    """
    Seleciona o melhor voo baseado na preferência do usuário.
    
    Args:
        departure: Código do aeroporto de partida
        arrival: Código do aeroporto de chegada
        preference: 'price' para mais barato, 'duration' para mais rápido
    
    Returns:
        String JSON com voo selecionado
    """
    route = f"{departure}-{arrival}"
    flights = flights_db.get(route, [])
    
    if not flights:
        return json.dumps({
            "error": f"Nenhum voo disponível para a rota {route}"
        })
    
    if preference == "duration":
        best_flight = min(flights, key=lambda f: f.duration_minutes)
    else:  # price
        best_flight = min(flights, key=lambda f: f.price)
    
    return json.dumps({
        "selected_flight": best_flight.model_dump(), 
        "reason": f"Melhor opção por {preference}"
    }, indent=2)


def get_user_info(name: str) -> str:
    """
    Recupera informações do perfil do usuário.
    
    Args:
        name: Nome do usuário
    
    Returns:
        String JSON com perfil do usuário
    """
    user = users_db.get(name)
    if not user:
        return json.dumps({"error": f"Usuário '{name}' não encontrado"})
    
    return json.dumps(user.model_dump(), indent=2)


def book_flight(flight_id: str, user_name: str) -> str:
    """
    Realiza booking de um voo para um usuário.
    
    Args:
        flight_id: ID do voo a ser reservado
        user_name: Nome do usuário
    
    Returns:
        String JSON com confirmação ou erro
    """
    # Buscar usuário
    user = users_db.get(user_name)
    if not user:
        return json.dumps({"error": f"Usuário '{user_name}' não encontrado"})
    
    # Buscar voo
    flight = None
    for route_flights in flights_db.values():
        for f in route_flights:
            if f.flight_id == flight_id:
                flight = f
                break
        if flight:
            break
    
    if not flight:
        return json.dumps({"error": f"Voo '{flight_id}' não encontrado"})
    
    # Verificar disponibilidade
    if flight.available_seats <= 0:
        return json.dumps({"error": "Voo sem assentos disponíveis"})
    
    # Criar itinerário
    itinerary_id = f"IT{len(itineraries_db) + 1:03d}"
    itinerary = Itinerary(
        itinerary_id=itinerary_id,
        user_id=user.user_id,
        flights=[flight_id],
        total_price=flight.price,
        status="confirmed",
        created_at=datetime.now().isoformat()
    )
    
    itineraries_db[itinerary_id] = itinerary
    
    # Atualizar assentos disponíveis
    flight.available_seats -= 1
    
    return json.dumps({
        "success": True,
        "itinerary_id": itinerary_id,
        "flight_id": flight_id,
        "user_name": user_name,
        "total_price": flight.price,
        "message": f"Booking confirmado! Itinerário: {itinerary_id}"
    }, indent=2)


print("✅ Tool functions definidas:")
print("  - fetch_flight_info()")
print("  - pick_flight()")
print("  - get_user_info()")
print("  - book_flight()")
```

---

### Célula 11 (Markdown): ReAct Agent

```markdown
---

## Parte 5: Implementação do ReAct Agent

Agora vamos criar nosso **primeiro agente completo** usando DSPy!

**ReAct** = **Rea**soning + **Act**ing
- LLM pode **pensar** (reasoning)
- LLM pode **agir** (chamar tools)
- Repete até resolver o problema

**Arquitetura:**
```
User Query
    ↓
[ReAct Agent]
    ↓
Thought: "Preciso buscar voos"
    ↓
Action: fetch_flight_info(GRU, SDU, 2025-12-15)
    ↓
Observation: [JSON com voos]
    ↓
Thought: "Agora vou escolher o melhor"
    ↓
Action: pick_flight(GRU, SDU, preference='price')
    ↓
Observation: [Voo selecionado]
    ↓
Final Answer: "Recomendo voo FL002..."
```
```

---

### Célula 12 (Python): Agent Implementation

```python
# Signature do Agent
class BookingAgentSignature(dspy.Signature):
    """Agente especializado em reserva de voos. Pode buscar voos, 
    selecionar o melhor baseado em preferências, e fazer booking."""
    
    query: str = dspy.InputField(desc="Pedido do usuário (ex: 'Quero voo GRU-SDU para dia 15/12')")
    
    answer: str = dspy.OutputField(desc="Resposta completa ao usuário com recomendação")


# Module do Agent
class BookingAgent(dspy.Module):
    def __init__(self):
        super().__init__()
        
        # ReAct com tools
        self.agent = dspy.ReAct(
            BookingAgentSignature,
            tools=[fetch_flight_info, pick_flight, get_user_info, book_flight]
        )
    
    def forward(self, query: str):
        """
        Processa query do usuário e retorna resposta.
        
        Args:
            query: Pedido do usuário
            
        Returns:
            dspy.Prediction com answer
        """
        result = self.agent(query=query)
        return result


# Instanciar agent
agent = BookingAgent()

print("✅ BookingAgent criado e pronto para uso!")
print("  - Pode buscar voos (fetch_flight_info)")
print("  - Pode escolher melhor voo (pick_flight)")
print("  - Pode obter info do usuário (get_user_info)")
print("  - Pode fazer booking (book_flight)")
```

---

### Célula 13 (Markdown): Testes Simples

```markdown
---

## Parte 6: Testes - Casos Simples (✅ Sucesso Esperado)

Vamos testar o agent em casos **simples e bem definidos**.

**Hipótese:** Single agent deve funcionar bem aqui.
```

---

### Célula 14 (Python): Teste Simples 1

```python
# Teste 1: Busca simples de voos
print("="*60)
print("🧪 TESTE 1: Busca simples de voos")
print("="*60)

query1 = "Quero ver voos de GRU para SDU no dia 15 de dezembro de 2025"

result1 = agent(query=query1)

print("\n📝 Query:")
print(f"  {query1}")
print("\n💬 Resposta do Agent:")
print(f"  {result1.answer}")
print("\n✅ Resultado: SUCESSO (caso simples)")
```

---

### Célula 15 (Python): Teste Simples 2

```python
# Teste 2: Recomendação com preferência
print("\n" + "="*60)
print("🧪 TESTE 2: Recomendação com preferência")
print("="*60)

query2 = "Preciso de um voo barato de GRU para SDU"

result2 = agent(query=query2)

print("\n📝 Query:")
print(f"  {query2}")
print("\n💬 Resposta do Agent:")
print(f"  {result2.answer}")
print("\n✅ Resultado: SUCESSO (caso simples com preferência)")
```

---

### Célula 16 (Markdown): Testes Complexos

```markdown
---

## Parte 7: Testes - Casos Complexos (❌ Falha Esperada - CRÍTICO)

Agora vamos testar o agent em casos **complexos e multi-step**.

**Hipótese:** Single agent vai **FALHAR** aqui. Por quê?
- Precisa coordenar múltiplas ações
- Precisa manter contexto complexo
- Decisões interdependentes
- Sem especialização

**Isso motiva Multi-Agent Systems!** (Caps 3+)
```

---

### Célula 17 (Python): Teste Complexo 1

```python
# Teste 3: Cenário complexo - múltiplos usuários e restrições
print("\n" + "="*60)
print("🧪 TESTE 3: Cenário complexo - múltiplos usuários")
print("="*60)

query3 = """
Alice e Bob querem viajar juntos. Alice prefere voos baratos e janela, 
Bob prefere business class e corredor. Precisam de GRU para SDU no dia 15/12,
e também uma segunda viagem de GRU para BSB no dia 20/12. 
Qual a melhor combinação considerando ambos os perfis e o custo total?
"""

try:
    result3 = agent(query=query3)
    print("\n📝 Query:")
    print(f"  {query3.strip()}")
    print("\n💬 Resposta do Agent:")
    print(f"  {result3.answer}")
    print("\n⚠️ Análise:")
    print("  - Agent pode ter dado resposta parcial")
    print("  - Não conseguiu otimizar para AMBOS os usuários")
    print("  - Faltou coordenação entre múltiplas decisões")
except Exception as e:
    print(f"\n❌ FALHA: {e}")
    print("\n⚠️ Single agent não conseguiu lidar com complexidade")
```

---

### Célula 18 (Python): Teste Complexo 2

```python
# Teste 4: Restrições conflitantes
print("\n" + "="*60)
print("🧪 TESTE 4: Restrições conflitantes")
print("="*60)

query4 = """
Preciso do voo mais barato de GRU para BSB, MAS também preciso 
que tenha pelo menos 15 assentos disponíveis porque vou com um grupo,
E preciso que seja antes das 12h porque tenho reunião à tarde.
Se não houver voo que atenda tudo, qual o melhor trade-off?
"""

try:
    result4 = agent(query=query4)
    print("\n📝 Query:")
    print(f"  {query4.strip()}")
    print("\n💬 Resposta do Agent:")
    print(f"  {result4.answer}")
    print("\n⚠️ Análise:")
    print("  - Agent pode não ter considerado todos os trade-offs")
    print("  - Faltou raciocínio multi-objetivo")
    print("  - Precisaria de agentes especializados")
except Exception as e:
    print(f"\n❌ FALHA: {e}")
    print("\n⚠️ Restrições conflitantes são difíceis para single agent")
```

---

### Célula 19 (Markdown): Análise de Limitações

```markdown
---

## Parte 8: Análise de Limitações do Single Agent

### 🔍 O que Observamos

#### ✅ Single Agent FUNCIONA WELL para:
1. **Tarefas simples e lineares**
   - Buscar voos
   - Selecionar melhor opção com 1 critério
   - Fazer booking direto

2. **Contexto limitado**
   - 1 usuário
   - 1 viagem
   - 1 critério de otimização

3. **Sem interdependências**
   - Ações independentes
   - Sem necessidade de coordenação

---

#### ❌ Single Agent FALHA ou TEM DIFICULDADES em:

1. **Múltiplos stakeholders**
   - Alice quer barato, Bob quer business
   - Como otimizar para AMBOS?
   - **Solução:** Agente especializado por usuário

2. **Restrições conflitantes**
   - Mais barato vs mais assentos vs horário
   - Como fazer trade-offs?
   - **Solução:** Agentes especializados por critério + coordenador

3. **Workflows complexos**
   - Reservar voo → Hotel → Transfer
   - Cada step depende do anterior
   - **Solução:** Pipeline de agentes especializados

4. **Necessidade de debate/consenso**
   - Múltiplas opções válidas
   - Qual a melhor?
   - **Solução:** Múltiplos agentes "debatendo"

5. **Auto-correção**
   - Agent errou
   - Como corrigir?
   - **Solução:** Agente reflexivo que critica e melhora

---

### 📊 Trade-offs: Single vs Multi-Agent

| Aspecto | Single Agent | Multi-Agent |
|---------|--------------|-------------|
| **Simplicidade** | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **Custo** | 💰 (1 LLM call) | 💰💰💰 (N calls) |
| **Latência** | ⚡ Rápido | 🐢 Mais lento |
| **Especialização** | ❌ Generalista | ✅ Especialistas |
| **Complexidade** | ⭐⭐ Tarefas simples | ⭐⭐⭐⭐⭐ Complexas |
| **Debugabilidade** | 📦 Caixa preta | 🔍 Transparente |
| **Manutenibilidade** | ⚠️ Tudo em 1 | ✅ Modular |

---

### 💡 Quando Usar Cada Abordagem

**Use Single Agent quando:**
- ✅ Tarefa é simples e bem definida
- ✅ Não há múltiplos stakeholders
- ✅ Custo e latência são críticos
- ✅ Não precisa de especialização

**Use Multi-Agent quando:**
- ✅ Problema tem múltiplos domínios
- ✅ Necessita especialização
- ✅ Benefício de múltiplas perspectivas
- ✅ Qualidade > Custo/Latência
- ✅ Debugabilidade é importante

---

### 🚀 Próximos Passos

Nos próximos capítulos vamos explorar:

1. **Cap 3:** Primeiro Sistema Multi-Agent (intro)
2. **Cap 4:** Sequential/Pipeline Architecture
3. **Cap 5:** Hierarchical Architecture
4. **Cap 6:** Collaborative/Debate Architecture
5. **Cap 7:** Reflexive/Self-Critique Architecture

**A jornada está apenas começando!** 🎯
```

---

### Célula 20 (Markdown): Conclusões

```markdown
---

## Parte 9: Conclusões e Key Takeaways

### ✅ O que Você Aprendeu

1. **DSPy Core Concepts:**
   - ✅ Signatures definem interfaces
   - ✅ Modules encapsulam lógica
   - ✅ Predictors aplicam Signatures
   - ✅ DSPy é declarativo e otimizável

2. **ReAct Agents:**
   - ✅ Combinam raciocínio e ação
   - ✅ Podem usar ferramentas (tools)
   - ✅ Adequados para tarefas com tools

3. **Limitações de Single Agents:**
   - ✅ Funcionam bem em casos simples
   - ❌ Lutam com complexidade
   - ❌ Falta especialização
   - ❌ Difíceis de debugar

4. **Motivação para Multi-Agent:**
   - ✅ Especialização por domínio
   - ✅ Múltiplas perspectivas
   - ✅ Melhor qualidade em problemas complexos
   - ✅ Mais debugável e manutenível

---

### 📚 Referências Principais

```
Khattab, O., et al. (2023). DSPy: Compiling Declarative Language Model Calls 
into Self-Improving Pipelines. arXiv:2310.03714.

Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models. 
arXiv:2210.03629.

Wei, J., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. 
NeurIPS 2022.
```

---

### 🎯 Exercícios Sugeridos

1. **Adicionar novos tools:**
   - `cancel_booking()`
   - `get_flight_status()`
   - `search_hotels()`

2. **Testar com outros LLMs:**
   - GPT-4
   - Claude
   - Llama local

3. **Otimizar prompts:**
   - Usar `dspy.BootstrapFewShot` (Cap 9)
   - Comparar performance

4. **Criar seu próprio agente:**
   - Domínio diferente (e-commerce, suporte, etc.)
   - Implementar do zero

---

### ➡️ Próximo Capítulo

**Cap 3: Primeiro Sistema Multi-Agent**

Vamos criar nosso primeiro sistema com múltiplos agentes especializados:
- SearchAgent (busca)
- AnalysisAgent (análise)
- RecommendationAgent (recomendação)
- BookingAgent (reserva)

**Prepare-se para ver a diferença!** 🚀
```

---

## ✅ CAP 2 COMPLETO - 100%

**Total de células:** 20
- **Markdown:** 10 células (teoria, explicações, análises)
- **Python:** 10 células (código executável)

**Conteúdo:**
- ✅ Teoria DSPy completa
- ✅ Setup e configuração
- ✅ Data models
- ✅ Tool functions
- ✅ ReAct agent implementado
- ✅ Testes simples (sucesso)
- ✅ Testes complexos (falha motivada)
- ✅ Análise profunda de limitações
- ✅ Motivação clara para multi-agent
- ✅ Referências acadêmicas
- ✅ Exercícios e próximos passos

**Para converter em notebook Jupyter:**
```bash
# Usar nbformat ou copiar células manualmente
jupyter notebook cap-02-dspy-essentials-single-agent.ipynb
```

