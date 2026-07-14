# Design System: Mira Sketch

Este documento define as diretrizes visuais e técnicas para a criação de ícones e ilustrações em SVG no estilo "Mira Sketch" (usado em exemplos como `clock.svg` e `lock.svg`). O objetivo é garantir que todos os novos desenhos mantenham a consistência da estética desenhada à mão (hand-drawn), orgânica e perfeitamente legível em qualquer ambiente de visualização.

---

## 1. Identidade Visual (A Filosofia)

O estilo "Mira Sketch" simula um desenho analógico feito de forma ágil com caneta nanquim sobre papel branco, com pequenos toques de marcador aquarelável para volume e sombreamento.

- **Orgânico e Imperfeito:** Linhas retas exatas ou círculos matemáticos são proibidos. A beleza estética está na leve imprecisão intencional do traço humano.
- **Rabiscos e Sobreposições:** Para simular o vai-e-vem da caneta, as bordas principais do objeto frequentemente recebem linhas duplas ou sobrepostas (uma mais grossa e outra mais fina, levemente desalinhadas e transpassando as pontas).
- **Sem Bordas Transparentes em Tela Escura:** O fundo das ilustrações simula o papel branco fisicamente. Isso impede que os traços pretos desapareçam ou sejam "engolidos" quando abertos em visualizadores ou sites que usam *Dark Mode*.

---

## 2. Guia de Implementação (Especificações Técnicas)

Para traduzir a filosofia acima em código SVG para IAs e Desenvolvedores, siga as regras matemáticas abaixo:

### Canvas e Fundo
- **ViewBox:** Sempre fixado em `0 0 200 200`. Facilita o cálculo mental das coordenadas. O objeto deve ocupar o centro, com pelo menos `10px` de margem de respiro.
- **Background Anti-Dark-Mode:** Todo arquivo **DEVE** conter a tag `<rect x="0" y="0" width="200" height="200" fill="#ffffff" />` na primeira camada do desenho.

### Paleta de Cores Base
- **Traço Principal (Caneta):** `#1a1a1a` (Cinza muito escuro). Evite o `#000000` (preto absoluto) para um contraste mais elegante e realista.
- **Preenchimento Base do Objeto:** `#ffffff` (Branco). Usado no `fill` do corpo para garantir que a forma tape o sombreamento que vazar ou as linhas de fundo.
- **Sombreamento (Marcador Cyan):** `#82e0d8`. Aplicado sempre como um `stroke` de alta espessura (`15` a `18`) com `opacity="0.6"` ou `opacity="0.5"`. A sombra entra **antes** dos traços pretos (para ficar por baixo) e **depois** do preenchimento branco base.

### Configurações de Traço (Stroke)
Todas as tags ou grupos (`<g>`) de traçado negro devem carregar por padrão:
- `stroke-linecap="round"`
- `stroke-linejoin="round"`
- `fill="none"`

**Espessuras de Caneta (Stroke-width):**
- **`4.5` (Contorno Principal):** Define as bordas externas e as geometrias grandes do objeto.
- **`2.0` ou `2.5` (Linha Sketch/Rabiscos):** Usado para reescrever as mesmas linhas do contorno principal com coordenadas levemente desviadas, criando a ilusão de esboço manual.
- **`3.0` (Detalhes Finos):** Parafusos, miolos (como o buraco da fechadura) e traços internos curtos.

### Geometria e Caminhos (Paths)
- Nunca confie nas tags básicas como `<rect>`, `<circle>`, `<polygon>` ou `<line>` para compor as formas orgânicas. 
- Use **exclusivamente a tag `<path>`**.
- Construa o formato usando as Curvas Bézier: `C` (curvas cúbicas) e `Q` (curvas quadráticas).
- Mesmo se for desenhar uma "caixa" (como a base do cadeado), use um `<path>` cujas retas sejam feitas por nós (`L`) ligeiramente irregulares.

---

## 3. Template Boilerplate

Sempre que for gerar um SVG novo no estilo Mira Sketch (ou injetar esse formato num Prompt), utilize a estrutura base abaixo. Ela já agrupa as camadas na ordem correta de renderização.

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <!-- ==========================================
       Design System: MIRA SKETCH
       ========================================== -->
  
  <!-- 1. Fundo Base (Proteção contra Dark Mode) -->
  <rect x="0" y="0" width="200" height="200" fill="#ffffff" />
  
  <!-- 2. Preenchimento do Corpo (Esconde a sobreposição traseira) -->
  <!-- Ex: <path d="..." fill="#ffffff" /> -->
  
  <!-- 3. Sombreamento em Cores (Marcador Aquarela - Fica por baixo do traço) -->
  <g stroke="#82e0d8" fill="none" stroke-linecap="round" stroke-linejoin="round" opacity="0.6">
    <!-- Ex: <path d="..." stroke-width="18" /> -->
  </g>

  <!-- 4. Contornos e Rabiscos (A Caneta Nanquim) -->
  <g stroke="#1a1a1a" fill="none" stroke-linecap="round" stroke-linejoin="round">
    
    <!-- Camada de Traço Principal (Caneta Grossa) -->
    <g stroke-width="4.5">
      <!-- Inserir Paths principais -->
    </g>
    
    <!-- Camada de Efeito Sketch (Caneta Fina e Irregular) -->
    <g stroke-width="2.0">
      <!-- Inserir Paths secundários sobrepostos -->
    </g>

    <!-- Detalhes Internos -->
    <g stroke-width="3.0">
      <!-- Inserir pequenos Paths de marcação -->
    </g>
    
  </g>

  <!-- 5. Elementos Finais (Olhos, Reflexos Brancos, Miolos Escuros) -->
  <g>
    <!-- Preenchimentos pretos sólidos ou linhas brancas brilhantes (#ffffff) que devem vir por cima de tudo -->
  </g>
</svg>
```
