# 🎓 DSPy ReAct Agents - Série de Notebooks Zero to Hero

Esta série de notebooks oferece um caminho completo de aprendizado para **agentes ReAct com DSPy**, desde os fundamentos até otimização avançada.

## 📚 Estrutura da Série

A série está organizada em **4 notebooks complementares**, oferecendo duas abordagens de aprendizado (Linear e Hands-On) em dois níveis (Básico e Avançado):

### 🎯 Nível Básico - Fundamentos

#### 1. **Fundamentos (Linear)** - `dspy_agents_basic_linear_final.ipynb`
- **Abordagem:** Conceitos → Construção → Execução
- **Tempo:** 20-25 minutos
- **Nível:** Iniciante
- **Ideal para:** Quem prefere entender a teoria antes de codificar

**Conteúdo:**
- ✅ O que são agentes ReAct e por que usar DSPy
- ✅ Modelagem de dados com Pydantic
- ✅ Criação de ferramentas (tools)
- ✅ Configuração e criação do agente
- ✅ Testes básicos

#### 2. **Fundamentos (Hands-On)** - `dspy_agents_basic_handson_final.ipynb`
- **Abordagem:** Fazer → Testar → Entender
- **Tempo:** 15-20 minutos
- **Nível:** Iniciante
- **Ideal para:** Quem prefere aprender fazendo

**Conteúdo:**
- ⚡ Código funcionando rapidamente
- 🧪 Testes práticos imediatos
- 📖 Explicações posteriores
- 🔍 Experimentação guiada

---

### 🚀 Nível Avançado - Otimização

#### 3. **Otimização Avançada (Linear)** - `dspy_agents_advanced_linear_final.ipynb`
- **Abordagem:** Por que otimizar → Como otimizar → Produção
- **Tempo:** 45-60 minutos
- **Nível:** Intermediário/Avançado
- **Ideal para:** Quem quer entender profundamente cada técnica

**Conteúdo:**
- 🎯 Por que agentes precisam de otimização
- 📊 Métricas multi-objetivo para agentes
- 🔧 BootstrapFewShot - Otimização automática
- 🚀 MIPRO e RandomSearch - Técnicas avançadas
- 💾 Serialização e deployment
- 📈 Avaliação e comparação de resultados

#### 4. **Otimização Avançada (Hands-On)** - `dspy_agents_advanced_handson_final.ipynb`
- **Abordagem:** Otimizar agora → Ver resultados → Entender técnica
- **Tempo:** 30-45 minutos
- **Nível:** Intermediário/Avançado
- **Ideal para:** Quem quer resultados rápidos e depois entender

**Conteúdo:**
- ⚡ Otimização express
- 📊 Melhorias dramáticas imediatas
- 🔍 Análise posterior dos resultados
- 🧪 Experimentação com técnicas
- 🚀 Deploy rápido em produção

---

## 🗺️ Guia de Navegação

### Como Escolher Seu Caminho?

```
┌─────────────────────────────────────────────────────┐
│  Você é...                                          │
├─────────────────────────────────────────────────────┤
│  💭 Gosta de teoria antes?   → Notebooks LINEAR     │
│  🛠️  Prefere praticar logo?  → Notebooks HANDS-ON   │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│  Seu objetivo...                                    │
├─────────────────────────────────────────────────────┤
│  📚 Aprender do zero         → Notebooks BÁSICOS    │
│  🚀 Melhorar agentes         → Notebooks AVANÇADOS  │
└─────────────────────────────────────────────────────┘
```

### Caminhos Sugeridos

**Caminho 1: Aprendizado Completo Estruturado**
```
1. Básico Linear → 2. Avançado Linear
```
Melhor para: Entendimento profundo e sistemático

**Caminho 2: Prática Intensiva**
```
1. Básico Hands-On → 2. Avançado Hands-On
```
Melhor para: Aprender fazendo, iteração rápida

**Caminho 3: Híbrido Balanceado**
```
1. Básico Linear → 2. Avançado Hands-On
```
Melhor para: Teoria nos fundamentos, prática na otimização

**Caminho 4: Quick Start**
```
1. Básico Hands-On → 2. Básico Linear (revisão) → 3. Avançado Hands-On
```
Melhor para: Resultados rápidos com consolidação posterior

---

## 📊 Comparação Rápida

| Notebook | Células | Tempo | Abordagem | Quando Usar |
|----------|---------|-------|-----------|-------------|
| **Básico Linear** | 19 | 20-25min | Teoria→Prática | Primeira vez com DSPy/ReAct |
| **Básico Hands-On** | 20 | 15-20min | Prática→Teoria | Quer ver funcionando logo |
| **Avançado Linear** | 40 | 45-60min | Progressivo | Entender otimização a fundo |
| **Avançado Hands-On** | 41 | 30-45min | Resultados primeiro | Otimizar agente rapidamente |

---

## 🎯 Pré-requisitos

### Para Notebooks Básicos:
- ✅ Python básico (funções, classes, tipos)
- ✅ Conceitos básicos de LLMs
- ✅ Familiaridade com Jupyter Notebooks

### Para Notebooks Avançados:
- ✅ Ter completado um notebook básico
- ✅ Python intermediário
- ✅ Noções de métricas de ML (recomendado)

---

## 🚀 Quick Start

1. **Instale as dependências:**
```bash
pip install dspy-ai python-dotenv pydantic
```

2. **Configure suas API keys:**
```bash
# Crie um arquivo .env
GROQ_API_KEY=your_key_here
# ou
OPENAI_API_KEY=your_key_here
```

3. **Escolha seu notebook:**
- Primeiro contato? → `dspy_agents_basic_linear_final.ipynb`
- Quer praticar? → `dspy_agents_basic_handson_final.ipynb`
- Já sabe o básico? → `dspy_agents_advanced_linear_final.ipynb`

---

## 📚 O Que Você Vai Construir

Em todos os notebooks, você vai criar um **agente de atendimento ao cliente para uma companhia aérea** que pode:

- 🔍 Buscar voos disponíveis
- ✈️ Reservar passagens aéreas
- 👤 Consultar perfis de usuários
- 🎫 Gerenciar itinerários
- 📝 Abrir tickets de suporte

**Notebooks Básicos:** Agente funcionando com capacidades completas  
**Notebooks Avançados:** Agente otimizado com 15-30% mais performance

---

## 🎓 Conceitos Abordados

### Notebooks Básicos
- Arquitetura ReAct (Reasoning + Acting)
- Modelagem de dados com Pydantic
- Criação de tools/ferramentas
- Configuração de LLMs
- DSPy Signatures
- Módulo dspy.ReAct
- Testing básico

### Notebooks Avançados
- Métricas multi-objetivo
- Few-shot learning
- BootstrapFewShot optimization
- MIPRO (Multi-objective Instruction Prompt Optimization)
- RandomSearch
- Serialização de modelos
- Deployment em produção
- Avaliação e comparação

---

## 📖 Recursos Adicionais

- [Documentação oficial do DSPy](https://dspy.ai)
- [Tutorial original](https://dspy.ai/tutorials/customer_service_agent/)
- [Paper ReAct](https://arxiv.org/abs/2210.03629)
- [DSPy GitHub](https://github.com/stanfordnlp/dspy)

---

## 🤝 Contribuições

Esta série de notebooks foi criada para facilitar o aprendizado de agentes ReAct com DSPy. 

**Feedback e melhorias são bem-vindos!**

---

## 📝 Notas

- Todos os notebooks usam os mesmos dados mock (companhia aérea)
- Os notebooks são independentes mas complementares
- Exemplos são executáveis sem modificações (com API keys configuradas)
- Outputs de exemplo estão salvos nos notebooks para referência

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Baseado em:** https://dspy.ai/tutorials/customer_service_agent/



