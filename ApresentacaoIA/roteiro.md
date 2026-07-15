# Roteiro da Apresentação: Desenvolvimento de Software Integrado com IA

Este documento estrutura a apresentação com um foco de **20% em Contexto/Teoria e 80% em Demonstração Prática**, visando mostrar o impacto real da IA no dia a dia do engenheiro.

---

## PARTE 1: CONTEXTO E MUDANÇA DE PARADIGMA (20%)
*Objetivo: Nivelar o conhecimento do público rapidamente e apresentar o novo modelo mental de trabalho.*

### 1. O Novo Normal no Desenvolvimento
* **O "Santo Graal" do Momento:** A IA deixou de ser ficção e virou a principal alavanca de produtividade.
* **O Foco do Engenheiro:** Enquanto o mundo fala de imagens e vídeos, nosso foco são as **LLMs**. Código-fonte é texto, e LLMs são especialistas absolutas na manipulação de texto estruturado.

### 2. O que é IA?
* **Conteúdo:** Hoje chamamos de "IA" um conjunto de algoritmos de software que simulam a inteligencia humana, como:
  1. LLM (destaque e coloca do lado direito da imagem, e redistribui os demais)
  2. Visão Computacional
  3. IA Preditiva Machine Learning
  4. Melhor Caminho A*
  5. E outros...
* **Visual:** **[img: .assets/ai_types.svg | x: 0, y: 0]**

### 3. LLM
* **Transição:** De: "2. O que é IA?" | Imagem de conexão: [img: .assets/seta.svg | x: 250, y: 0 | w: 100 | autoNext: true] (Clique 1) | Efeito: Aparecer
* **Conteúdo:** Vamos focar nosso bate-papo nas LLMs, que nada mais são que redes neurais. Como a LLM funciona, ela recebe um Contexto, Processa, e gera um Resultado. Então se você muda o contexto, o resultado será diferente. Esta LLM é uma API, um serviço que as aplicaçoes chamam para usar a IA dentro delas. Sugestão imagem: @brain2.svg.
* **Visual:** **[img: .assets/llm_process.svg | x: 504, y: -1]** (Clique 2)

### 4. Provedores de IA
* **Transição:** De: "3. LLM" | Imagem de conexão: [img: .assets/seta.svg | x: 750, y: 0 | w: 100 | autoNext: true] (Clique 1) | Efeito: Aparecer
* **Conteúdo:** Estes serviços de LLMs são mantidos por empresas como OpenAI, Google, Anthropic e outras. Alternativa: Criar seu próprio servidor de LLM (ex: Ollama).
* **Visual:** **[img: (a definir) | x: 1000, y: 0]** (Clique 2)

### 5. Tokens
* **Transição:** De: "3. LLM" | Imagem de conexão: [img: .assets/seta.svg | x: 504, y: 250 | w: 100 | autoNext: true] (Clique 1) | Efeito: Aparecer
* **Conteúdo:** Tokens são pedaços de palavras. Eles representam o "pedágio" ou o limite de banda. Injetar o contexto correto sem estourar o limite de tokens é a chave para a engenharia de IA.
* **Visual:** **[img: (a definir) | x: 504, y: 500]** (Clique 2)

### 4. O Novo Processo de Trabalho: Da Escrita para a Revisão
* *Slide principal de impacto da introdução.*
* **O Modelo Antigo:** O desenvolvedor gasta horas *escrevendo* documentação e *digitando* código do zero.
* **O Novo Fluxo com IA:** 
  1. **Definição de Diretrizes:** Nosso papel passa a ser definir *o que* precisa ser feito e as regras de negócio.
  2. **Geração:** Pedimos para a IA elaborar o documento ou código.
  3. **Revisão:** Avaliamos o resultado com olhar crítico de engenharia.
  4. **Ajuste de Diretrizes:** Se o resultado não foi bom, não editamos o texto/código manualmente na hora; nós *ajustamos a diretriz original* e pedimos uma nova geração.

### 4. Ferramentas e o Ecossistema: O Funil de Produtividade
* **O Novo Básico (Ferramentas Diversas):** A IA já é *commodity* em tarefas gerais. Chats (ChatGPT/Gemini) para brainstorm inicial, NotebookLM para consolidar PDFs e grandes regras de negócio, e Teams para transcrição e resumos de reuniões.
* **O Nosso Diferencial (Ferramentas para o Desenvolvedor):** Para escrever código, precisamos de contexto completo do repositório. Usamos IDEs Agênticas (ex: Cursor, Windsurf).
* **Nossa Aposta Estratégica: Antigravity:** O investimento massivo do Google em IA voltada para código nos dá uma ferramenta nativa de estado da arte para aplicar o novo processo de trabalho.
Baixo impacto se houver necessidade de troca de IDE agentico.

### 5. Vibe Coding 🌊 (Exploração/Design):
  * Abordagem intuitiva e rápida. Prompt -> Gera -> Testa -> Ajusta. Focado no resultado visual e "sentimento".
  * **Vantagem:** Prototipagem relâmpago, criatividade extrema.
  * **Desvantagem:** Código difícil de manter e escalar ("caixa preta").

- [x] **[img: .assets/vibe_coding.svg | x: 1000, y: 0]**

### 6. Spec-Driven Development 📐 (Engenharia/Produção):
  * Especificações e regras restritas (testes, docs, arquitetura) definidas *antes* do código. A IA segue a regra estritamente.
  * **Vantagem:** Previsibilidade, segurança, escala bem em equipe.
  * **Desvantagem:** Mais lento no início.
* **A Recomendação:** Vibe Coding para PoCs e validação de ideias. SDD para sistemas críticos que vão para produção.

---

## PARTE 2: A PRÁTICA NO DIA A DIA - "O LIVRO DE RECEITAS" (80%)
*Objetivo: Sair dos slides e ir para as ferramentas demonstrar cenários reais. A apresentação vira um showcase de casos de uso dinâmicos.*

### Cenário Prático 1: Documentação e Requisitos (O Novo Fluxo)
* **A Dor:** Ninguém gosta de escrever documentação extensa do zero.
* **A Demonstração:**
  1. Pegar um resumo de transcrição do Teams ou algumas *bullet-points* brutas.
  2. Usar uma IA (Chat ou NotebookLM) informando a Diretriz: "Transforme isso em uma User Story com critérios de aceite BDD".
  3. Revisar o resultado ao vivo, notar um erro, ajustar a diretriz ("Adicione o critério de erro de validação") e regerar.

### Cenário Prático 2: Entendendo e Refatorando Código Legado
* **A Dor:** Entrar em um arquivo complexo e sem comentários que outra pessoa fez.
* **A Demonstração:** 
  1. Abrir um arquivo complexo no Antigravity.
  2. Pedir para a IDE: "Explique o que este método faz de forma resumida".
  3. Pedir a refatoração: "Extraia essa lógica complexa para funções menores com nomes claros e adicione Javadoc/Docstrings".

### Cenário Prático 3: O Fim dos Testes Manuais Tediosos
* **A Dor:** Escrever o *setup* de testes unitários e os *mocks* demora muito.
* **A Demonstração:**
  1. Pegar a função refatorada no cenário anterior.
  2. Usar o Antigravity para gerar: "Crie a suíte de testes unitários para este arquivo, cobrindo cenários de sucesso, erro e *edge-cases*, usando *framework X*".
  3. Mostrar o código sendo gerado em segundos.

### Cenário Prático 4: Automação de CI/CD e Code Review
* **A Dor:** Pull Requests gigantes e sem descrição.
* **A Demonstração:** 
  1. Mostrar como um Agente de CI/CD (ou script rodando local) pode ler o "diff" do código e gerar automaticamente o título e a sumarização do PR.
  2. Mostrar como a IA pode apontar possíveis vulnerabilidades ou *code smells* antes do revisor humano atuar.

---

## 3. Conclusão e Próximos Passos
* **A IA é o Co-piloto, Você é o Piloto:** A responsabilidade final pela segurança e lógica de negócios é sempre do engenheiro.
* **Segurança da Informação:** O que **NUNCA** compartilhar (chaves, dados de clientes).
* **Call to Action:** Vamos adotar o novo modelo de "Diretrizes + Revisão" a partir de amanhã.
* **Perguntas e Respostas.**
