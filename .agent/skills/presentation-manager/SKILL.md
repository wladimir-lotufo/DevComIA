---
name: presentation-manager
description: Manage HTML slides, update index.html navigation, enforce the Engineering Blueprint design system, and ensure new slides are created with slugs.
---

# Presentation Manager Skill

This skill is designed to help you maintain the HTML presentation structure and enforce its strict visual identity.

## Core Rules

1. **Naming Convention:** Whenever creating a new slide or renaming an existing one, the `.html` file must be named using a slug of its title.
   * Example: A slide titled "The Future of AI" must be saved as `the-future-of-ai.html`.
   * **NEVER** use generic names like `slide12.html` ou `slide_new.html`.

2. **Navigation (`index.html`):** The presentation flow is controlled by the `slides` array inside the Javascript block of `index.html`.
   * To add a slide to the presentation, you must append its path (e.g., `'slides/the-future-of-ai.html'`) to the `slides` array in the correct order.
   * To remove a slide from the presentation, just remove it from the `slides` array.

3. **Data Preservation:**
   * If a slide is removed from the presentation (`index.html`), **DO NOT delete the `.html` file**. The file must remain in the `slides/` directory for historical purposes or future use.

## Design System: Engineering Blueprint
**ALL NEW SLIDES MUST STRICTLY ADHERE TO THIS DESIGN SYSTEM.**

* **Tone:** Analítico, Preciso, Pedagógico, Estruturado, Profissional
* **Identity:**
  * Background: `#F9F9F9`
  * Text Color: `#222222`
  * Accent Color: `#5B9BD5` (Blue)
  * Secondary Colors: `#C0392B` (Red), `#EAF4FC` (Light Blue), `#888888` (Gray), `#FFFFFF`, `#D3D3D3`
* **Style:** Arte linear técnica, marcadores de dimensão, símbolos de plantas baixas, layout isométrico. Textura limpa esquemática com grid ao fundo (`bg-grid`).
* **Composition:** Split-screen, fluxo vertical hierárquico, muito espaço em branco (whitespace), alinhamento a grades rigoroso.
* **Line Weight:** Traços finos e precisos (1px-2px) para caixas e estruturas. Linhas tracejadas para setas e fluxos.
* **Visual Aids:** Use `#EAF4FC` (Azul claro) para backgrounds de caixas destacadas ou ativas. Use `#C0392B` tracejado para atenção ou erros.
* **Typography:**
  * Headers: Helvetica Neue, Bold/800
  * Body: Inter, Regular/Medium
  * Labels/Tags: Roboto Mono

4. **Slide Structure:**
   * New slides should follow the standard structure of the presentation, which uses `styles.css`. The CSS classes `.bg-grid`, `.slide-container`, `.glass-card` handle the visual rendering of the Blueprint style.
   * Base Template:
     ```html
     <!DOCTYPE html>
     <html lang="pt-BR">
     <head>
       <meta charset="UTF-8">
       <link rel="stylesheet" href="styles.css">
     </head>
     <body>
       <div class="bg-grid"></div>
       <div class="slide-container">
         <div class="slide-header">
           <div class="slide-badge">Badge Text</div>
           <h1 class="slide-title">Slide Title</h1>
         </div>
         <div class="slide-content">
           <div class="glass-card">
              <!-- Content goes here -->
           </div>
         </div>
       </div>
       <script>
         window.addEventListener('keydown', (e) => {
           if (e.key === 'ArrowRight' || e.key === ' ') window.parent.postMessage('next', '*');
           if (e.key === 'ArrowLeft') window.parent.postMessage('prev', '*');
         });
       </script>
     </body>
     </html>
     ```

## Workflow
- When a user asks to add a slide, generate the HTML using the standard template, apply Blueprint UI logic within the `.glass-card`, save it as a slugified file in the `slides/` folder, and update the `slides` array in `index.html`.
- When a user asks to remove or hide a slide, just remove its reference from `index.html` but do not touch the HTML file.
