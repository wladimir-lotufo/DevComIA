---
description: Create a visual, high-fidelity UI prototype using the technology stack defined in the Architecture document, without backend integration.
---

# Workflow: Prototype

- **Objective:** Create a purely visual, interactive prototype directly in the frontend technology defined for the project (as per `docs/architecture.md` or equivalent architecture document). This follows a 2-Phase "UI-First Development" approach (Prototipação em Código) where Phase 1 focuses entirely on layout, UX, and mock data, and Phase 2 connects the visual components to real backend logic and data.

## The Two-Phase Approach (UI-First Development)

1. **Momento 1 (Prototipação VISUAL):**
   - Criação das telas e componentes focando unicamente em UI/UX, acessibilidade e responsividade.
   - Dados devem ser estáticos (mockados em memória ou hardcoded diretamente na camada de visualização).
   - Sem requisições reais de API (sem `HttpClient` e endpoints reais), sem regras de negócio complexas, e sem conexão de banco de dados real.
   - O objetivo é homologar o visual, as micro-interações e o fluxo do usuário primeiro, criando o código visual definitivo.

2. **Momento 2 (Integração e Lógica):**
   - A equipe de engenharia/backend **reaproveita 100% do código visual gerado no Momento 1**, evitando qualquer retrabalho (desperdício zero).
   - O trabalho da engenharia consiste apenas em substituir os mocks por chamadas `HTTP` reais, adicionar gerenciamento de estado complexo, tratamento de erros de rede, validações de negócio profundas e regras de segurança (ex: JWT Authentication).

## Inputs

1. **Architecture Document:** (e.g., `docs/architecture.md`) to determine the exact tech stack (e.g., Blazor, MAUI, React, Next.js).
2. **User Story / Requirements:** The details of the feature/view to be prototyped (Functional and Non-Functional requirements).
3. **Design System / Style Guide:** The existing UI patterns to be followed (Colors, Typography, Components).
4. **User Journeys:** To understand the navigation flow between screens.

## Steps (Momento 1)

1. **Analyze Requirements & Identify Tech Stack:**
    - Consult the Architecture document to identify whether this view belongs to a Web project or Mobile project.
    - Identify the framework and file extension to be used (e.g., `.razor` for Blazor, `.xaml` for MAUI, `.tsx` for React).
    - **CRUCIAL**: Under no circumstances create an HTML/JS/jQuery prototype if the target architecture uses a specific component framework like Blazor or MAUI.

2. **Design UI Components & Layout:**
    - Identify the necessary views to accomplish the user journey (e.g., List View, Detail View, Edit Form).
    - Structure the layout using the project's styling solution (e.g., Vanilla CSS, Tailwind, or component libraries defined in architecture).
    - Break complex interfaces down into smaller, reusable UI components.

3. **Create the Visual Prototype Code:**
    - Create the actual files in the respective physical folders of the project (e.g., `web-blazor/ImobiliariaBlazor/Pages/`, `mobile-maui/ImobiliariaMobile/Views/`).
    - Add structured mock data directly to the view space or in a simple static list/variable in the code-behind.
    - Implement basic navigation between prototyped screens using the framework's native router (e.g., clicking a "View details" button on a grid row routes to the mockup detail page).

4. **Add Visual Interactivity (Optional but Recommended):**
    - Add simple client-side states (e.g., toggling a modal, expanding an accordion, showing a success toast message when clicking "Save").
    - Validate required fields on forms purely visually (to test error states without hitting a real backend).
    - Keep logic strictly UI-bound.

5. **Phase X / Audits (Mandatory Static Validation):**
    - **Stop and ask:** Before considering the prototype finished, you MUST pause and ask the user for permission to run the final checks (e.g., "son kontrolleri yap").
    - Once approved, run the following static validations (no server required):
      - **UX/UI:** Execute `python .agent/scripts/ux_audit.py` (or manual strict inspection) on the generated view files to ensure visual component conformity, responsiveness, and Design System rules.
      - **Accessibility (WCAG):** Execute `python .agent/skills/frontend-design/scripts/accessibility_checker.py` statically.
      - **Code Quality:** Execute `python .agent/scripts/lint_runner.py` on the generated UI code (`.razor`, `.xaml`, etc.).
    - **Blocker:** Do not proceed to the next step if there are critical validation errors. Refactor the prototype until it passes.

6. **Verify Completeness:**
    - Does the prototype visually cover all acceptance criteria of the User Story?
    - Is it using the correct technology as defined in the project Architecture?
    - Is it completely decoupled from real backend services?
    - Is the code structured in a clean, semantic way that developers can easily hook up real data in Phase 2?

## Output
- Mock data structures (ViewModels, Records, Interfaces) ready to be replaced/extended by real API models in Phase 2.
- A fully navigable visual experience that acts as the final UI codebase for the engineering team.
