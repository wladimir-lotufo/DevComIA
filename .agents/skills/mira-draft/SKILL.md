---
name: draft
description: Cria e mantém apresentações HandDrawn via injeção no DOM do visualizador. SSOT para coordenadas é o roteiro.md.
allowed-tools: Read, Write, Command
---

# /draft - Motor de Apresentações Mira Sketch

Esta skill é responsável por orquestrar a elaboração, manutenção e consolidação de apresentações Infinite Canvas no estilo HandDrawn (Mira Sketch). 

## 🎯 Objetivo Principal
Manter o arquivo `roteiro.md` e o visualizador `[nomeDaPasta].html` perfeitamente em sincronia. O agente gera SVGs individuais na pasta `.assets/` e os posiciona na tela obedecendo às coordenadas declaradas no roteiro.

---

## 🏗️ Comandos da Skill

### `/draft iniciar`
Quando chamado em uma pasta vazia (ou nova pasta de apresentação), a IA deve:
1. Copiar o template HTML (Infinite Canvas) de `.agents/skills/mira-draft/templates/viewer.html` para a raiz do projeto atual, renomeando-o para `[nomeDaPasta].html`.
2. Criar a pasta `.assets/`.
3. Copiar o template de Roteiro de `.agents/skills/mira-draft/templates/roteiro.md` para iniciar o documento base.

### `/draft consolidar` (ou atualizações implícitas)
Quando o usuário pede para "consolidar", "atualizar tela", "montar slide", ou sempre que você (a IA) adicionar uma imagem nova no roteiro:
1. **Leia** o arquivo `roteiro.md`.
2. Para cada imagem mencionada que possua coordenadas, extraia o path (ex: `.assets/minha_img.svg`) e suas coordenadas (`x` e `y`).
3. **Escreva** (Injete) o código abaixo no arquivo `[nomeDaPasta].html`, exatamente entre as marcações `/* MIRA: INICIO JSON ASSETS */` e `/* MIRA: FIM JSON ASSETS */`:
   `{ src: ".assets/arquivo.svg", x: X, y: Y, w: W, r: R },`
4. Se uma imagem for gerada/alterada, assegure-se de que a dupla de arquivos (`roteiro.md` e o HTML) estão em sincronia.

---

## 🔧 Regras de Atuação (MANDATORY)

1. **Single Source of Truth (SSOT):** O arquivo `roteiro.md` manda no posicionamento, tamanho e rotação. Se o usuário quiser que a imagem mude, você altera os valores de `x`, `y`, `w` (width) e `r` (rotation) no roteiro, e então replica isso gerando o JSON atualizado. 
   - Padrão esperado no roteiro: `[img: .assets/arquivo.svg | x:500, y:300, w:400, r:15]` (ou notação semelhante).
   - **Transições e Coreografia:** O roteiro suporta a declaração explícita de fluxo usando "Transições de Entrada". Em vez de separar slides e transições rigidamente, a transição (ex: seta de conexão) pertence ao slide de destino, declarando sua origem no campo `De:`.
     - *Exemplo:* `* **Transição:** De: "2. O que é IA?" | Imagem de conexão: [img: .assets/seta.svg | x: 250, y: 0] (Clique 1)`
     - O agente deve respeitar a ordem desses eventos (Cliques) e o mapeamento de conexões não-lineares ao consolidar o HTML (ex: injetando atributos `data-step` para animações em ordem).
2. **Isolamento de SVGs:** Você sempre criará imagens completas em código SVG e as salvará na pasta `.assets/`. O HTML nunca deve conter SVGs inline; ele apenas referencia as imagens vetoriais como tags `<img>`.
3. **Motor Semi-Intocável:** O arquivo HTML possui funções JavaScript essenciais para **Pan (arrastar)**, **Zoom (scroll do mouse)**, **Régua (Rules Overlay)** e o novo **Modo Edição (Drag de assets)**. Você **JAMAIS** deve editar as tags `<script>` ou o CSS global da estrutura do Viewer (a não ser que o usuário peça uma manutenção na skill em si). Em cenários normais, sua área de atuação é estritamente dentro da marcação `<!-- MIRA: INICIO ASSETS -->`.
4. **Vibe Coding & Design (Estilo Visual):** 
   - Ao desenhar SVGs individuais que o usuário pede, você lê o documento raiz (`style.md`) do projeto para importar estilos, traços HandDrawn e Cores.
   - **Paleta e Elementos Vazados:** Privilegie usar uma paleta de cores primárias básicas (ex: traços em Cyan, Laranja, Chumbo). Proponha desenhos vazados, usando predominantemente *linhas coloridas* ao invés de blocos maciços de cor.
   - **Textos Integrados:** Os textos dentro dos SVGs também podem e devem adotar as mesmas cores da paleta para manter a coesão do design.
5. **Organização de Scripts (.scripts/):** É OBRIGATÓRIO que todo arquivo gerador (scripts Python `.py`, scripts Node, bash, etc.) criado durante a sessão seja salvo na pasta `.scripts/` dentro do diretório da apresentação, e não na raiz.
6. **Consolidação em Lote (Clipboard):** Quando o usuário colar no chat um texto do tipo `Atualize o roteiro.md com as seguintes coordenadas ajustadas:`, você deve atualizar o `roteiro.md` com os novos valores de `x`, `y`, `w` e `r` e imediatamente acionar o comando implícito `/draft consolidar` para injetar o layout atualizado no HTML.
7. **Fundo Transparente:** As imagens SVG geradas DEVEM SEMPRE ter fundo transparente. Nunca adicione `<rect>` de fundo branco, preto ou colorido que preencha o canvas inteiro simulando background.
8. **Limites do Canvas (ViewBox):** Ao gerar os SVGs, verifique rigorosamente se todos os textos e imagens/desenhos CABEM na janela definida pelo viewBox. Nunca deixe textos cortados pelas bordas do SVG.
9. **Contraste no Fundo Branco:** Como o fundo do visualizador (Viewer) é branco, **NUNCA utilize linhas, traços ou textos na cor branca (`#ffffff` ou `white`)**, pois eles ficarão invisíveis. Use cores escuras ou os tons vivos da paleta para garantir a legibilidade.

---

## 📐 Boas Práticas
- Ao gerar uma imagem vetorial nova, certifique-se de que o SVG tenha larguras e alturas bem definidas (viewBox e `width/height="100%"` do próprio frame) para que a tag `<img>` ocupe o tamanho correto no DOM.
- Use `replace_file_content` para alterar as posições dentro de `[nomeDaPasta].html` sem estragar os scripts.
