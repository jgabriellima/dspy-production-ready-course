# Referências Acadêmicas - Bibliografia Completa

## Objetivo

Centralizar todas as referências acadêmicas citadas no livro, organizadas por tópico.

**Status:** Em construção — adicionar referências conforme capítulos são escritos.

---

## DSPy Framework

### Paper Principal

**DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines**

```bibtex
@article{khattab2023dspy,
  title={DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
  author={Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and Vardhamanan, Sri and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas T and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher},
  journal={arXiv preprint arXiv:2310.03714},
  year={2023},
  url={https://arxiv.org/abs/2310.03714}
}
```

**Abstract:**  
_"The ML community is rapidly exploring techniques for prompting language models (LMs) and for stacking them into pipelines that solve complex tasks. Unfortunately, existing LM pipelines are typically implemented using hard-coded "prompt templates", i.e. lengthy strings discovered via trial and error. Toward a more systematic approach for developing and optimizing LM pipelines, we introduce DSPy, a programming model that abstracts LM pipelines as text transformation graphs, i.e. imperative computational graphs where LMs are invoked through declarative modules. DSPy modules are parameterized, meaning they can learn (by creating and collecting demonstrations) how to apply compositions of prompting, finetuning, augmentation, and reasoning techniques."_

**Citado em:** Caps 1, 2, 8, 9

---

## Agent Patterns e Architectures

### ReAct (Reasoning + Acting)

**ReAct: Synergizing Reasoning and Acting in Language Models**

```bibtex
@article{yao2022react,
  title={ReAct: Synergizing Reasoning and Acting in Language Models},
  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  journal={arXiv preprint arXiv:2210.03629},
  year={2022},
  url={https://arxiv.org/abs/2210.03629}
}
```

**Abstract:**  
_"While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information."_

**Citado em:** Caps 2, 3

---

### Reflexion (Self-Critique)

**Reflexion: Language Agents with Verbal Reinforcement Learning**

```bibtex
@article{shinn2023reflexion,
  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
  author={Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  journal={arXiv preprint arXiv:2303.11366},
  year={2023},
  url={https://arxiv.org/abs/2303.11366}
}
```

**Abstract:**  
_"Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require. To address this, we propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials."_

**Citado em:** Cap 7

---

### Chain-of-Thought Prompting

**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**

```bibtex
@article{wei2022chain,
  title={Chain-of-Thought Prompting Elicits Reasoning in Large Language Models},
  author={Wei, Jason and Wang, Xuezhi and Schuurmans, Dale and Bosma, Maarten and Xia, Fei and Chi, Ed and Le, Quoc V and Zhou, Denny},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  pages={24824--24837},
  year={2022},
  url={https://arxiv.org/abs/2201.11903}
}
```

**Abstract:**  
_"We explore how generating a chain of thought—a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning."_

**Citado em:** Caps 2, 8

---

## Optimization

### MIPRO (Multi-prompt Instruction Proposal Optimizer)

**Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs**

```bibtex
@article{opsahl2024mipro,
  title={Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs},
  author={Opsahl-Ong, Bryce and Dulberg, Josh and Reddy, Avinash and Khattab, Omar},
  journal={arXiv preprint arXiv:2406.11695},
  year={2024},
  url={https://arxiv.org/abs/2406.11695}
}
```

**Abstract:**  
_"Large Language Model (LLM) programs are sequences of LM calls where the output of one step influences subsequent steps. These programs have shown remarkable performance but require careful tuning of prompts, which include instructions and few-shot demonstrations. We introduce MIPRO, a novel technique that optimizes both instructions and demonstrations for multi-stage LM programs."_

**Citado em:** Caps 9, 10, 12

---

### BootstrapFewShot

**[Referência interna DSPy - documentar]**

**Citado em:** Caps 9, 10

---

## Fine-Tuning e Transfer Learning

### Parameter-Efficient Fine-Tuning

**LoRA: Low-Rank Adaptation of Large Language Models**

```bibtex
@article{hu2021lora,
  title={LoRA: Low-Rank Adaptation of Large Language Models},
  author={Hu, Edward J and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
  journal={arXiv preprint arXiv:2106.09685},
  year={2021},
  url={https://arxiv.org/abs/2106.09685}
}
```

**Abstract:**  
_"An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks."_

**Citado em:** Cap 13

---

**QLoRA: Efficient Finetuning of Quantized LLMs**

```bibtex
@article{dettmers2023qlora,
  title={QLoRA: Efficient Finetuning of Quantized LLMs},
  author={Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke},
  journal={arXiv preprint arXiv:2305.14314},
  year={2023},
  url={https://arxiv.org/abs/2305.14314}
}
```

**Citado em:** Cap 13

---

## Multi-Agent Systems (Foundational)

### SOAR Cognitive Architecture

```bibtex
@article{laird2012soar,
  title={The Soar cognitive architecture},
  author={Laird, John E},
  journal={MIT press},
  year={2012}
}
```

**Citado em:** Cap 1

---

### ACT-R

```bibtex
@article{anderson2004integrated,
  title={An integrated theory of the mind},
  author={Anderson, John R and Bothell, Daniel and Byrne, Michael D and Douglass, Scott and Lebiere, Christian and Qin, Yulin},
  journal={Psychological review},
  volume={111},
  number={4},
  pages={1036},
  year={2004}
}
```

**Citado em:** Cap 1

---

## Evaluation e Metrics

### BLEU, ROUGE (NLP Metrics)

**BLEU: a Method for Automatic Evaluation of Machine Translation**

```bibtex
@inproceedings{papineni2002bleu,
  title={BLEU: a method for automatic evaluation of machine translation},
  author={Papineni, Kishore and Roukos, Salim and Ward, Todd and Zhu, Wei-Jing},
  booktitle={Proceedings of the 40th annual meeting of the Association for Computational Linguistics},
  pages={311--318},
  year={2002}
}
```

**Citado em:** Cap 11

---

## LLMOps e Production

### MLOps Principles

**[A adicionar - papers sobre MLOps]**

**Citado em:** Cap 15

---

### Observability

**[A adicionar - papers sobre observability em ML systems]**

**Citado em:** Caps 15, 16

---

## Scaling e Distributed Systems

### Distributed Systems Fundamentals

**[A adicionar - papers relevantes]**

**Citado em:** Cap 16

---

## Benchmarks e Datasets

### HotPotQA

**HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering**

```bibtex
@inproceedings{yang2018hotpotqa,
  title={HotpotQA: A dataset for diverse, explainable multi-hop question answering},
  author={Yang, Zhilin and Qi, Peng and Zhang, Saizheng and Bengio, Yoshua and Cohen, William W and Salakhutdinov, Ruslan and Manning, Christopher D},
  booktitle={Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
  pages={2369--2380},
  year={2018}
}
```

**Citado em:** Caps 8, 11

---

### MMLU (Massive Multitask Language Understanding)

```bibtex
@article{hendrycks2020measuring,
  title={Measuring massive multitask language understanding},
  author={Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
  journal={arXiv preprint arXiv:2009.03300},
  year={2020},
  url={https://arxiv.org/abs/2009.03300}
}
```

**Citado em:** Cap 11

---

## A Adicionar

### Capítulos Pendentes de Referências

- [ ] Cap 1: Papers sobre enterprise AI
- [ ] Cap 3: Papers sobre multi-agent coordination
- [ ] Cap 4-7: Papers sobre cognitive architectures
- [ ] Cap 10: Papers sobre optimization
- [ ] Cap 11: Papers sobre evaluation metrics
- [ ] Cap 13: Papers sobre fine-tuning LLMs
- [ ] Cap 14: Papers sobre enterprise architectures
- [ ] Cap 15: Papers sobre LLMOps
- [ ] Cap 16: Papers sobre scaling
- [ ] Cap 17: Case studies e white papers

---

## Formato para Apêndice F

Converter este documento para o formato final do Apêndice F:
- Organizar por categoria
- Adicionar abstracts em português (traduzidos)
- Links para papers
- Notas sobre relevância

---

## Ferramentas de Gestão

**BibTeX:** Para citações
**Zotero:** Para gerenciar papers
**Google Scholar:** Para buscar papers
**arXiv:** Para preprints

---

**Status:** 10/100+ referências adicionadas  
**Última atualização:** [Data atual]

