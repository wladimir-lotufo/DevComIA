# Roteiro da Apresentação: Desenvolvimento de Software Integrado com IA

Este documento estrutura a apresentação com um foco de **20% em Contexto/Teoria e 80% em Demonstração Prática**, visando mostrar o impacto real da IA no dia a dia do engenheiro.

---

## PARTE 1: CONTEXTO E MUDANÇA DE PARADIGMA (20%)
*Objetivo: Nivelar o conhecimento do público rapidamente e apresentar o novo modelo mental de trabalho.*

### 1. O que é IA?
* **Conteúdo:** Hoje chamamos de "IA" um conjunto de algoritmos de software que simulam a inteligencia humana, como:
  1. LLM (destaque e coloca do lado direito da imagem, e redistribui os demais)
  2. Visão Computacional
  3. IA Preditiva Machine Learning
  4. Melhor Caminho A*
  5. E outros...
* **Visual:** **[img: .assets/ai_types.svg | x: 7, y: -6, w: 324]**

### 2. LLM
* **Transição:** De: "1. O que é IA?" | Imagem de conexão: [img: .assets/seta.svg | x: 237, y: -2, w: 100, autoNext: true] (Clique 1) | Efeito: Aparecer
* **Conteúdo:** Vamos focar nosso bate-papo nas LLMs, que nada mais são que redes neurais. Como a LLM funciona, ela recebe um Contexto, Processa, e gera um Resultado. Então se você muda o contexto, o resultado será diferente. Esta LLM é uma API, um serviço que as aplicaçoes chamam para usar a IA dentro delas. Sugestão imagem: @brain2.svg.
* **Visual:** **[img: .assets/llm_process.svg | x: 478, y: 4]** (Clique 2)

### 3. Provedores de IA
* **Transição:** De: "2. LLM" | Imagem de conexão: [img: .assets/seta.svg | x: 496, y: -181, w: 100, r: -89, autoNext: true] (Clique 1) | Efeito: Aparecer
* **Conteúdo:** Estes serviços de LLMs são mantidos por empresas como OpenAI (ChatGPT), Google (Gemini), Anthropic (Claude) e Meta (Llama). Alternativa: Criar seu próprio servidor de LLM local (ex: Ollama).
* **Imagem:** Uma imagem estilo sketch mostrando os logotipos das empresas e os nomes e logotipos das ferramentas mais populares: OpenAI / ChatGPT, Google / Gemini, Anthropic / Claude, Meta / Llama 3, e Ollama / Local LLM.
* **Visual:** **[img: .assets/providers.svg | x: 489, y: -315, w: 300]** (Clique 2)

### 4. Tokens
* **Transição:** De: "2. LLM" | Imagem de conexão: [img: .assets/seta.svg | x: 413, y: 170, w: 100, r: 94, autoNext: true] (Clique 1) | Efeito: Aparecer
* **Conteúdo:** Tokens são pedaços de palavras. Eles representam o "pedágio" ou o limite de banda. Injetar o contexto correto sem estourar o limite de tokens é a chave para a engenharia de IA.
* **Imagem:** Um funil ou tubo medidor, por onde passam pequenas peças de quebra-cabeça e blocos com letras (representando os pedaços de palavras/tokens). O tubo tem uma linha tracejada vermelha ou escura indicando um "limite" (simbolizando o pedágio/limite de contexto). Tudo no estilo Mira Sketch.
* **Visual:** **[img: .assets/tokens.svg | x: 413, y: 325, w: 200]** (Clique 2)

### 5. Cifrão
* **Transição:** De: "4. Tokens" 
* **Conteúdo:** Mostrar um cifrão sobre o funil para demostrar o custo da IA
* **Imagem:** Cifrão vermelho
* **Visual:** **[img: .assets/cifrao.svg | x: 494, y: 318, w: 96]** (Clique 2)

### 6. Aplicações
* **Transição:** De: "2. LLM" | Imagem de conexão: [img: .assets/seta.svg | x: 768, y: 15, w: 100, autoNext: true] (Clique 1) | Efeito: Aparecer
* **Conteúdo:** Vamos categorizar as Aplicações de IA em: 1. Geração de Texto 2. Geração de Código 3. Processamento de Imagem 4. Processamento de Áudio 
Exemplos de aplicações:
   - Chat ChatGPT, Gemini (chat)) 
   - Notebook LM
   - Ferramentas de Apresentação
   - Aplicações customizadas 
   - Chatbots (Aplicação e Whatsapp)
   - Ferramentas desenvlvimento (Antigravity, Claude, Codex)
   - Ferramentas de imagem (nano Banana, Leonardo)
   - Ferramentas de audio (whisper, audiobox)
* **Imagem:** Acima oos icones das categorias. Abaixo os ícones para as aplicações. Colotar titulo nas aplicações. Dar destaque para Aplicações Customizadas e Ferramentas Desenvolvimento, vamos puxar slides a partir delas
* **Visual:** **[img: .assets/aplicacoes.svg | x: 1400, y: 1, w: 878]** (Clique 2)

### 7. Destaque Aplicações Customizadas
* **Transição:** De: "6. Aplicações"
* **Conteúdo:** Além de usar ferramentas prontas, uma grande frente do mercado é criar Aplicações Customizadas, integrando a IA via API diretamente nos negócios.
* **Visual:** **[img: .assets/destaque_customizadas.svg | x: 1754, y: -27, w: 143]**

### 8. Destaque Antigravity
* **Transição:** De: "7. Destaque Aplicações Customizadas"
* **Conteúdo:** Focar na aplicação Antigravity, nossa principal ferramenta agentica de desenvolvimento e aposta estratégica.
* **Visual:** **[img: .assets/destaque_antigravity.svg | x: 1231, y: 64, w: 137]**

### 9. É possível usar IA para grandes sistemas?
* **Transição:** De: "8. Destaque Antigravity"
* **Conteúdo:** 
  Qual o pulo do gato... O papel do Desenvolvedor passa a ser definir *Como* através de Especificações Técnicas de Arquitetura, de Especificações de Programas, de Regras Padronizadas de Geração de Código e Skills de IA que coordenam o trabalho.
  
  **Fluxo:**
  1. **Geração** Pedimos para a IA elaborar o documento ou código.
  2. **Revisão** Avaliamos o resultado com olhar crítico de engenharia.
  3. **Ajustes** Se o resultado não foi bom, não editamos o texto/código manualmente na hora; nós *ajustamos a diretriz original* e pedimos uma nova geração.
  4. **Tunning** Se o resultado não foi bom, não editamos o texto/código manualmente na hora; nós *ajustamos a diretriz original* e pedimos uma nova geração.
* **Imagem:** Um diagrama cíclico focado nos "Documentos de Diretrizes". À esquerda, ícones vazados de pranchetas/documentos (Arquitetura, Skills, Regras). Eles alimentam uma engrenagem central ou cérebro mecânico (Geração), que produz um bloco de código sob uma **Lupa** (Revisão). Da lupa, sai uma seta curva grande (laranja) que volta diretamente para as pranchetas iniciais (Ajuste de Diretrizes), formando um ciclo contínuo de retroalimentação.
* **Visual:** **[img: .assets/ciclo_feedback.svg | x: 1170, y: 500, w: 400]**

### 10. 
* **Transição:** De: "9. É possível usar IA para grandes sistemas?"
* **Conteúdo:** O maior esforço para ganhar escala ocorre na revisão das Skills de IA.
* **Visual:** **[img: .assets/destaque_item4.svg | x: 1182, y: 487, w: 642]**

### 11. Ferramentas e o Ecossistema: O Funil de Produtividade
* **O Novo Básico (Ferramentas Diversas):** A IA já é *commodity* em tarefas gerais. Chats (ChatGPT/Gemini) para brainstorm inicial, NotebookLM para consolidar PDFs e grandes regras de negócio, e Teams para transcrição e resumos de reuniões.
* **O Nosso Diferencial (Ferramentas para o Desenvolvedor):** Para escrever código, precisamos de contexto completo do repositório. Usamos IDEs Agênticas (ex: Cursor, Windsurf).
* **Nossa Aposta Estratégica: Antigravity:** O investimento massivo do Google em IA voltada para código nos dá uma ferramenta nativa de estado da arte para aplicar o novo processo de trabalho.
Baixo impacto se houver necessidade de troca de IDE agentico.

### 12. Vibe Coding 🌊 (Exploração/Design):
  * Abordagem intuitiva e rápida. Prompt -> Gera -> Testa -> Ajusta. Focado no resultado visual e "sentimento".
  * **Vantagem:** Prototipagem relâmpago, criatividade extrema.
  * **Desvantagem:** Código difícil de manter e escalar ("caixa preta").

- [x] **[img: .assets/vibe_coding.svg | x: -468, y: -6]**

### 13. Spec-Driven Development 📐 (Engenharia/Produção):
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
