# Cap 2 - Conteúdo Restante para Adicionar ao Notebook

## Instruções

Copie o conteúdo abaixo e adicione como células no notebook `cap-02-dspy-essentials-single-agent.ipynb`.

Alternar entre células **Markdown** e **Python** conforme indicado.

---

## 📝 CÉLULA MARKDOWN

```markdown
## Parte 4: Tool Functions

Agents precisam de **ferramentas** para interagir com o mundo. Vamos criar ferramentas para:

1. **fetch_flight_info**: Buscar voos disponíveis
2. **pick_flight**: Selecionar melhor voo
3. **get_user_info**: Obter informações do usuário
4. **book_flight**: Reservar um voo

**Importante:** Tool functions retornam **strings JSON** (LLMs entendem bem texto).
```

---

## 💻 CÉLULA PYTHON

```python
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
    })


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
    })


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
        return json.dumps({"error": f"Usuário {name} não encontrado"})
    
    return json.dumps({"user": user.model_dump()})


def book_flight(user_name: str, flight_id: str, date: str) -> str:
    """
    Reserva um voo para um usuário.
    
    Args:
        user_name: Nome do usuário
        flight_id: ID do voo a reservar
        date: Data da viagem
    
    Returns:
        String JSON com confirmação da reserva
    """
    user = users_db.get(user_name)
    if not user:
        return json.dumps({"error": f"Usuário {user_name} não encontrado"})
    
    # Encontrar o voo
    flight = None
    for route_flights in flights_db.values():
        for f in route_flights:
            if f.flight_id == flight_id:
                flight = f
                break
        if flight:
            break
    
    if not flight:
        return json.dumps({"error": f"Voo {flight_id} não encontrado"})
    
    if flight.available_seats <= 0:
        return json.dumps({"error": "Sem assentos disponíveis"})
    
    # Criar itinerário
    itinerary_id = str(uuid.uuid4())
    confirmation_number = f"CONF{uuid.uuid4().hex[:8].upper()}"
    
    itinerary = Itinerary(
        itinerary_id=itinerary_id,
        user_id=user.user_id,
        flights=[flight],
        total_price=flight.price,
        booking_date=datetime.now().strftime("%Y-%m-%d"),
        status="confirmed"
    )
    
    itineraries_db[itinerary_id] = itinerary
    
    # Atualizar assentos disponíveis
    flight.available_seats -= 1
    
    return json.dumps({
        "success": True,
        "confirmation_number": confirmation_number,
        "itinerary_id": itinerary_id,
        "flight": flight.model_dump(),
        "total_price": flight.price,
        "message": f"Voo {flight.flight_number} reservado com sucesso para {user_name}"
    })


print("✅ Tool functions criadas!")
print("\nFunções disponíveis:")
print("  - fetch_flight_info()")
print("  - pick_flight()")
print("  - get_user_info()")
print("  - book_flight()")
```

---

## 📝 CÉLULA MARKDOWN

```markdown
## Parte 5: Primeiro ReAct Agent

Agora vamos criar nosso primeiro agent usando o padrão **ReAct** (Reasoning + Acting).

### Signature do Agent

Primeiro definimos a Signature - o que o agent faz:
```

---

## 💻 CÉLULA PYTHON

```python
class AirlineAssistant(dspy.Signature):
    """
    Você é um assistente de reservas de voos que ajuda usuários a encontrar e reservar voos.
    
    Ferramentas disponíveis:
    - fetch_flight_info: Buscar voos disponíveis para uma rota
    - pick_flight: Selecionar o melhor voo (por preço ou duração)
    - get_user_info: Obter informações do usuário
    - book_flight: Reservar um voo para o usuário
    
    Seja sempre prestativo, profissional e forneça informações claras sobre voos e reservas.
    """
    
    user_request: str = dspy.InputField(
        desc="Requisição ou pergunta do usuário"
    )
    response: str = dspy.OutputField(
        desc="Sua resposta ao usuário"
    )

print("✅ Signature definida!")
```

---

## 📝 CÉLULA MARKDOWN

```markdown
### Criar o ReAct Agent

Agora criamos o agent com as tools:
```

---

## 💻 CÉLULA PYTHON

```python
# Lista de tools
tools = [
    fetch_flight_info,
    pick_flight,
    get_user_info,
    book_flight
]

# Criar o agent ReAct
agent = dspy.ReAct(
    signature=AirlineAssistant,
    tools=tools,
    max_iters=10  # Máximo de iterações thinking-acting
)

print("✅ ReAct Agent criado!")
print(f"   Tools: {len(tools)}")
print(f"   Max iterations: 10")
```

---

## 📝 CÉLULA MARKDOWN

```markdown
## Parte 6: Testes - Casos Simples (✅ Sucesso)

Vamos testar o agent com um caso **simples** - uma única tarefa bem definida.

### Teste 1: Buscar voos disponíveis
```

---

## 💻 CÉLULA PYTHON

```python
print("=" * 60)
print("TESTE 1: Buscar voos GRU → SDU")
print("=" * 60)

request = "Quais voos estão disponíveis de GRU para SDU amanhã?"

result = agent(user_request=request)

print(f"\n👤 Usuário: {request}")
print(f"\n🤖 Agent: {result.response}")
print("\n✅ Sucesso! Agent conseguiu buscar voos corretamente.")
```

---

## 📝 CÉLULA MARKDOWN

```markdown
### Teste 2: Reservar um voo simples
```

---

## 💻 CÉLULA PYTHON

```python
print("=" * 60)
print("TESTE 2: Reservar voo para Maria")
print("=" * 60)

request = "Reserve o voo mais barato de GRU para SDU para Maria amanhã"

result = agent(user_request=request)

print(f"\n👤 Usuário: {request}")
print(f"\n🤖 Agent: {result.response}")
print("\n✅ Sucesso! Agent conseguiu reservar o voo.")
```

---

## 📝 CÉLULA MARKDOWN

```markdown
## Parte 7: Testes - Casos Complexos (❌ Falha)

Agora vem a parte **CRÍTICA**: vamos testar o agent com tarefas **complexas multi-domínio**.

**Objetivo:** Demonstrar as **limitações** de um single agent.

### Teste 3: Tarefa Multi-Domínio

Vamos pedir ao agent para fazer algo que requer:
- ✅ Buscar voos (domínio: travel)
- ✅ Analisar preferências (domínio: preferences)
- ✅ Comparar opções (domínio: analysis)
- ✅ Fazer recomendação (domínio: recommendation)

**Problema esperado:** Single agent generalista não consegue fazer análise profunda em cada domínio.
```

---

## 💻 CÉLULA PYTHON

```python
print("=" * 60)
print("TESTE 3: Tarefa Multi-Domínio Complexa")
print("=" * 60)

complex_request = """
Preciso viajar de São Paulo (GRU) para Rio de Janeiro (SDU) amanhã.

Minhas preferências são:
1. Preciso chegar antes das 11h (reunião importante)
2. Prefiro conforto a preço
3. Sou frequent flyer (FF12345)
4. Quero saber qual voo tem melhor custo-benefício considerando:
   - Horário de chegada
   - Preço vs conforto
   - Benefícios para frequent flyer
   
Por favor, analise todas as opções e me dê uma recomendação detalhada com justificativa.
"""

print(f"\n👤 Usuário (requisição complexa):\n{complex_request}")

result = agent(user_request=complex_request)

print(f"\n🤖 Agent:\n{result.response}")

print("\n" + "=" * 60)
print("ANÁLISE DA RESPOSTA:")
print("=" * 60)
```

---

## 📝 CÉLULA MARKDOWN

```markdown
### Análise Crítica do Teste 3

**O que observamos:**

❌ **Limitação 1: Análise Superficial**
- Agent consegue buscar voos
- Mas análise de custo-benefício é **superficial**
- Não considera profundamente todos os critérios
- Falta expertise em análise de preferências

❌ **Limitação 2: Sem Especialização**
- Agent é **generalista**
- Não tem conhecimento profundo de:
  - Programas de frequent flyer
  - Análise de conforto vs preço
  - Trade-offs de horários

❌ **Limitação 3: Raciocínio Limitado**
- Consegue fazer reasoning básico
- Mas reasoning **multi-critério complexo** é fraco
- Falta capacidade de pesar múltiplos fatores simultaneamente

❌ **Limitação 4: Sem Contexto de Domínio**
- Não sabe que reunião importante → voo mais cedo é crítico
- Não entende implicações de ser frequent flyer
- Análise genérica, não personalizada

---

### Por Que Isso Acontece?

**Single Agent = Generalista**

```
┌─────────────────────────────────────┐
│     SINGLE AGENT (Generalista)      │
│                                     │
│  • Faz tudo "OK"                    │
│  • Nada "Excelente"                 │
│  • Sem especialização profunda      │
│  • Contexto limitado                │
│                                     │
│  Resultado: ❌ Análise superficial  │
└─────────────────────────────────────┘
```

**O que precisamos:**

```
┌─────────────────────────────────────────────────────┐
│          MULTI-AGENT SYSTEM                         │
│                                                     │
│  ┌──────────────┐  ┌──────────────┐               │
│  │Search Agent  │  │Analyze Agent │               │
│  │(Busca voos)  │  │(Analisa opts)│               │
│  └──────────────┘  └──────────────┘               │
│         │                  │                        │
│         └────────┬─────────┘                        │
│                  ↓                                  │
│          ┌──────────────┐                          │
│          │Recommend Agt │                          │
│          │(Recomenda)   │                          │
│          └──────────────┘                          │
│                                                     │
│  Resultado: ✅ Análise profunda e especializada    │
└─────────────────────────────────────────────────────┘
```
```

---

## 📝 CÉLULA MARKDOWN

```markdown
## Parte 8: Análise de Limitações

### Limitações Identificadas de Single Agents

Baseado nos testes, identificamos **4 limitações principais**:

#### 1. 🎯 Falta de Especialização

**Problema:** Single agent é generalista, não especialista.

**Impacto:**
- Análise superficial
- Sem conhecimento profundo de domínio
- Decisões "OK", não "excelentes"

**Exemplo:** 
- Agent sabe buscar voos ✅
- Mas não sabe analisar custo-benefício profundamente ❌

---

#### 2. 🧠 Raciocínio Multi-Critério Limitado

**Problema:** Difícil raciocinar sobre múltiplos critérios simultaneamente.

**Impacto:**
- Não consegue balancear múltiplos trade-offs
- Falta análise comparativa profunda
- Recomendações simplistas

**Exemplo:**
- Analisar: horário + preço + conforto + frequent flyer
- Agent escolhe um critério, ignora outros ❌

---

#### 3. 📊 Sem Contexto de Domínio

**Problema:** Não entende nuances e contexto específico.

**Impacto:**
- Recomendações genéricas
- Não personaliza por perfil
- Ignora contexto importante

**Exemplo:**
- "Reunião importante" → deveria priorizar chegada cedo
- "Frequent flyer" → deveria considerar benefícios
- Agent trata tudo genericamente ❌

---

#### 4. 🔄 Falta de Modularidade

**Problema:** Tudo em um único agent = difícil melhorar.

**Impacto:**
- Não pode especializar partes
- Difícil otimizar separadamente
- Coupling alto

**Solução:** Multi-agent permite especialização e otimização por partes ✅

---

### Quando Single Agent Funciona

✅ **Tarefas simples e bem definidas:**
- "Busque voos de A para B"
- "Reserve voo X para usuário Y"
- "Cancele reserva Z"

✅ **Domínio único:**
- Apenas busca de voos
- Apenas reservas
- Apenas cancelamentos

✅ **Sem análise complexa:**
- Não precisa comparar opções
- Não precisa raciocínio multi-critério
- Sem trade-offs complexos

---

### Quando Single Agent Falha

❌ **Tarefas multi-domínio:**
- Busca + análise + recomendação
- Múltiplos sistemas/APIs
- Contextos diferentes

❌ **Análise complexa:**
- Multi-critério
- Trade-offs
- Personalização profunda

❌ **Especialização necessária:**
- Conhecimento profundo de domínio
- Nuances e contexto
- Decisões críticas

---

## A Solução: Multi-Agent Systems

**No próximo capítulo (Cap 3)**, vamos ver como **Multi-Agent Systems** resolvem essas limitações através de:

1. **Especialização:** Cada agent é expert em seu domínio
2. **Modularidade:** Agents independentes, otimizáveis separadamente
3. **Coordenação:** Agents trabalham juntos
4. **Qualidade:** Especialização leva a melhores resultados

```
┌─────────────────────────────────────────────────────┐
│          PROGRESSION                                 │
│                                                      │
│  Single Agent      →    Multi-Agent System          │
│  (Generalista)          (Especialistas)             │
│                                                      │
│  ✅ Simples            ✅ Qualidade superior        │
│  ✅ Rápido            ✅ Especialização             │
│  ❌ Superficial       ✅ Análise profunda           │
│  ❌ Limitado          ✅ Modular                    │
│                                                      │
│  Use quando:           Use quando:                  │
│  • Tarefas simples     • Tarefas complexas         │
│  • 1 domínio           • Multi-domínio             │
│  • Sem análise         • Análise crítica           │
└─────────────────────────────────────────────────────┘
```
```

---

## 📝 CÉLULA MARKDOWN

```markdown
## Parte 9: Conclusões e Próximos Passos

### O Que Aprendemos

Neste capítulo, você:

1. ✅ **Dominou DSPy Core Concepts:**
   - Signatures, Modules, Predictors
   - ChainOfThought, ReAct
   - Diferença vs prompt engineering

2. ✅ **Implementou um ReAct Agent:**
   - Data models com Pydantic
   - Tool functions funcionais
   - Agent completo testado

3. ✅ **Identificou Limitações Críticas:**
   - Single agent = generalista
   - Falha em tarefas multi-domínio
   - Análise superficial vs especializada
   - **Motivação clara para multi-agent**

---

### Key Takeaways

🎯 **Single agents funcionam para tarefas simples**
- Um domínio, bem definido
- Sem análise complexa
- Rápido de implementar

⚠️ **Single agents falham em complexidade**
- Multi-domínio
- Análise multi-critério
- Especialização necessária

✨ **Multi-agent é a solução**
- Especialização por domínio
- Análise profunda
- Modularidade e qualidade

---

### Próximo Capítulo: Multi-Agent Systems

No **Capítulo 3**, vamos:

1. 🔧 **Retomar o problema que falhou** (Teste 3)
2. 🏗️ **Implementar solução multi-agent**
3. 📊 **Comparar resultados:** single vs multi
4. 🎯 **Entender quando usar cada abordagem**
5. 👀 **Preview das 4 arquiteturas** (Parte 2 do livro)

---

### Exercícios Sugeridos

**🟢 Básico:**
1. Adicione uma nova tool: `check_flight_status()`
2. Teste o agent com diferentes requisições
3. Modifique a temperature do LLM e observe diferenças

**🟡 Intermediário:**
1. Adicione validação nas tool functions
2. Implemente error handling robusto
3. Crie métricas para avaliar respostas do agent

**🔴 Avançado:**
1. Implemente um sistema de logging/tracing
2. Crie testes automatizados para o agent
3. Compare performance com diferentes LLMs

---

### Referências Complementares

📚 **Papers:**
- [DSPy Paper](https://arxiv.org/abs/2310.03714)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903)

📖 **Recursos:**
- [DSPy Docs](https://dspy.ai)
- [Pydantic Docs](https://docs.pydantic.dev)
- [Groq API](https://console.groq.com)

🎓 **Próximos Capítulos:**
- Cap 3: Primeiro Sistema Multi-Agent
- Cap 4-7: Arquiteturas Cognitivas
- Cap 8-13: Otimização & Fine-Tuning

---

**Parabéns! 🎉**

Você completou o Capítulo 2 e agora tem uma base sólida em DSPy e single agents.

**Continue para:** [Capítulo 3: Primeiro Sistema Multi-Agent](cap-03-primeiro-multiagent.ipynb)

---

*"The only way to learn is by doing."* — Programming Wisdom

**Happy Coding!** 🚀
```

---

## ✅ FIM DO CONTEÚDO

Total de células a adicionar: **~18 células** (9 markdown + 9 python)

Copie na ordem para o notebook!

