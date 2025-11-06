# Capítulo 16: Scaling Multi-Agent Systems

**Status:** ✅ Estrutura completa

## Conceito Principal
Como escalar de 100 para 1M requests/dia

## Bottlenecks
- LLM API rate limits (ex: OpenAI 60 RPM)
- Latência sequencial (N agents em cadeia)
- Estado compartilhado (coordenação)
- Custo ($$$ → $$$$$)

## Horizontal Scaling

```python
from fastapi import FastAPI
import redis

app = FastAPI()
redis_client = redis.Redis()

@app.post("/agent")
async def handle_request(query: str):
    # Distribute load across N workers
    worker_id = get_least_loaded_worker()
    
    # Queue request
    redis_client.lpush(f"queue:{worker_id}", query)
    
    # Await response
    result = await wait_for_result(query_id)
    
    return result
```

## Caching Strategies

```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=10000)
def cached_agent_call(agent_name, input_hash):
    # If seen before, return from cache
    pass

def call_agent_with_cache(agent, input_data):
    input_hash = hashlib.md5(str(input_data).encode()).hexdigest()
    
    # Try cache first
    cached = get_from_cache(input_hash)
    if cached:
        return cached
    
    # If not, call agent
    result = agent(input_data)
    
    # Save to cache
    save_to_cache(input_hash, result)
    
    return result
```

## Async & Parallel Execution

```python
import asyncio

async def parallel_multi_agent(query):
    # Fan-out: Multiple agents in parallel
    tasks = [
        asyncio.create_task(search_agent_async(query)),
        asyncio.create_task(analysis_agent_async(query)),
        asyncio.create_task(booking_agent_async(query))
    ]
    
    # Fan-in: Aggregate results
    results = await asyncio.gather(*tasks)
    
    # Coordinator synthesizes
    final = coordinator_agent(results)
    
    return final
```

## Cost Optimization
- **Tier agents:** Cheap first, expensive if needed
- **Batch requests:** Group when possible
- **Fallback to cache:** Use cached results
- **Model selection:** GPT-4 vs GPT-3.5 vs local

## Key Takeaways
- Horizontal scaling é essencial
- Caching reduz custo dramaticamente
- Async/parallel para latência
- Cost optimization é iterativo
- Monitor everything

**Status:** Estrutura completa ✅
