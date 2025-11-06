#!/usr/bin/env python3
"""
Script para processar e adaptar os notebooks DSPy ReAct Agents
de acordo com o plano pedagógico.
"""

import json
import sys

def load_notebook(path):
    """Carrega um notebook Jupyter"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notebook(notebook, path):
    """Salva um notebook Jupyter"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)

def find_cell_index(notebook, keyword):
    """Encontra o índice da primeira célula que contém uma palavra-chave"""
    for idx, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            if keyword in source:
                return idx
    return -1

def create_basic_linear(source_nb):
    """Cria o notebook básico linear"""
    nb = json.loads(json.dumps(source_nb))  # Deep copy
    
    # Encontrar onde começa a otimização
    opt_start = find_cell_index(nb, "🚀 Otimização Avançada do Agente")
    
    if opt_start > 0:
        # Manter células até o início da otimização
        # Manter também a seção de exemplos básicos de uso
        example_usage_start = find_cell_index(nb, "Example Usage")
        
        # Criar nova lista de células
        new_cells = []
        
        # Adicionar células básicas (antes da otimização)
        new_cells.extend(nb['cells'][:opt_start])
        
        # Adicionar célula de conclusão
        conclusion_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "---\n\n",
                "# 🎯 Próximos Passos\n\n",
                "## O que aprendemos\n\n",
                "Neste notebook, você aprendeu:\n\n",
                "✅ O que são agentes ReAct e como funcionam\n",
                "✅ Como modelar dados com Pydantic\n",
                "✅ Como criar ferramentas (tools) para agentes\n",
                "✅ Como configurar e criar um agente ReAct com DSPy\n",
                "✅ Como testar o agente com diferentes casos de uso\n\n",
                "## Para onde ir agora?\n\n",
                "### Opção 1: Abordagem Hands-On\n",
                "Se você prefere aprender fazendo, veja o notebook [Fundamentos (Hands-On)](dspy_agents_basic_handson_full.ipynb).\n\n",
                "### Opção 2: Otimização Avançada\n",
                "Pronto para melhorar seu agente? Veja:\n",
                "- [Otimização Avançada (Linear)](dspy_agents_advanced_linear_full.ipynb) - Para entender a teoria\n",
                "- [Otimização Avançada (Hands-On)](dspy_agents_advanced_handson_full.ipynb) - Para praticar direto\n\n",
                "### Recursos Adicionais\n",
                "- [Documentação oficial do DSPy](https://dspy.ai)\n",
                "- [Tutorial original](https://dspy.ai/tutorials/customer_service_agent/)\n",
                "- [Paper ReAct](https://arxiv.org/abs/2210.03629)\n"
            ]
        }
        new_cells.append(conclusion_cell)
        
        nb['cells'] = new_cells
    
    return nb

def create_basic_handson(source_nb):
    """Cria o notebook básico hands-on"""
    nb = create_basic_linear(source_nb)  # Começa igual ao linear
    
    # Adicionar célula de introdução hands-on no início
    intro_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## ⚡ Quick Start: Agente em 5 Minutos\n\n",
            "**Filosofia:** Código primeiro, explicação depois!\n\n",
            "Vamos criar um agente funcionando AGORA. Execute as células abaixo em sequência.\n",
            "Depois voltamos para entender cada parte.\n"
        ]
    }
    
    # Inserir após o header (célula 0)
    nb['cells'].insert(1, intro_cell)
    
    return nb

def create_advanced_linear(source_nb):
    """Cria o notebook avançado linear"""
    nb = json.loads(json.dumps(source_nb))  # Deep copy
    
    # Encontrar início da otimização
    opt_start = find_cell_index(nb, "🚀 Otimização Avançada do Agente")
    
    if opt_start > 0:
        # Manter apenas: header + seções de otimização
        # Remover células básicas (mantém apenas setup mínimo e otimização)
        
        # Encontrar células essenciais (imports, modelos, tools)
        setup_end = find_cell_index(nb, "Create the ReAct Agent")
        
        if setup_end > 0:
            # Manter: header + setup mínimo + otimização
            new_cells = []
            new_cells.extend(nb['cells'][:setup_end+2])  # Setup básico
            new_cells.extend(nb['cells'][opt_start:])     # Otimização completa
            nb['cells'] = new_cells
    
    return nb

def create_advanced_handson(source_nb):
    """Cria o notebook avançado hands-on"""
    nb = create_advanced_linear(source_nb)  # Começa com advanced linear
    
    # Adicionar nota hands-on
    intro_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## ⚡ Vamos Otimizar AGORA!\n\n",
            "**Filosofia:** Ver resultados impressionantes primeiro, entender depois!\n\n",
            "Execute as células abaixo e prepare-se para ver seu agente melhorar significativamente.\n"
        ]
    }
    
    nb['cells'].insert(1, intro_cell)
    
    return nb

def main():
    source_path = '/Users/joaogabriellima/Documents/Work/MyProjects/ai_materials/notebooks/dspy_customer_service_agent.ipynb'
    
    print("📚 Processando notebooks...")
    
    # Carregar notebook original
    source_nb = load_notebook(source_path)
    print(f"✅ Notebook original carregado: {len(source_nb['cells'])} células")
    
    # Criar versões adaptadas
    print("\n🔧 Criando versões adaptadas...")
    
    # 1. Básico Linear
    basic_linear_nb = create_basic_linear(source_nb)
    save_notebook(
        basic_linear_nb,
        '/Users/joaogabriellima/Documents/Work/MyProjects/ai_materials/notebooks/dspy_agents_basic_linear_final.ipynb'
    )
    print(f"  ✅ Básico Linear: {len(basic_linear_nb['cells'])} células")
    
    # 2. Básico Hands-On
    basic_handson_nb = create_basic_handson(source_nb)
    save_notebook(
        basic_handson_nb,
        '/Users/joaogabriellima/Documents/Work/MyProjects/ai_materials/notebooks/dspy_agents_basic_handson_final.ipynb'
    )
    print(f"  ✅ Básico Hands-On: {len(basic_handson_nb['cells'])} células")
    
    # 3. Avançado Linear
    advanced_linear_nb = create_advanced_linear(source_nb)
    save_notebook(
        advanced_linear_nb,
        '/Users/joaogabriellima/Documents/Work/MyProjects/ai_materials/notebooks/dspy_agents_advanced_linear_final.ipynb'
    )
    print(f"  ✅ Avançado Linear: {len(advanced_linear_nb['cells'])} células")
    
    # 4. Avançado Hands-On
    advanced_handson_nb = create_advanced_handson(source_nb)
    save_notebook(
        advanced_handson_nb,
        '/Users/joaogabriellima/Documents/Work/MyProjects/ai_materials/notebooks/dspy_agents_advanced_handson_final.ipynb'
    )
    print(f"  ✅ Avançado Hands-On: {len(advanced_handson_nb['cells'])} células")
    
    print("\n✨ Todos os notebooks criados com sucesso!")
    print("\n📁 Arquivos criados:")
    print("  • dspy_agents_basic_linear_final.ipynb")
    print("  • dspy_agents_basic_handson_final.ipynb")
    print("  • dspy_agents_advanced_linear_final.ipynb")
    print("  • dspy_agents_advanced_handson_final.ipynb")

if __name__ == "__main__":
    main()



