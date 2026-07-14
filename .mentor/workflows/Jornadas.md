---
description: Define or update User Journeys in lean-inception.md
---

# Workflow: Jornadas

- **Objective**: Define or update the **Jornadas de Usuário** section in `docs/ai/product/lean-inception.md`.

- **Inputs**:
    1. **Lean Inception File**: `docs/ai/product/lean-inception.md`.
    2. **Journey Details**: Persona, Journey Name, Objective, Entities involved, Step-by-step flow.

- **Outputs**:
    1. **Updated Lean Inception File**: `docs/ai/product/lean-inception.md` with new or updated Journeys.

- **Steps**:
    1. **Read Lean Inception**: Read `docs/ai/product/lean-inception.md` and locate the `# Jornadas de Usuário` section.
    2. **Locate Persona**: Find the subsection for the relevant Persona (e.g., `## 👩‍🏫 Gestor de Partnership`).
    3. **Update/Create Journey**:
        - Add a new journey or update an existing one.
        - Format:
            ```markdown
            ### Jornada X: {Nome da Jornada}
            *   **Objetivo:** {Descrição do objetivo}
            *   **Entidades:**
                *   `Entidade1` (Atributos)
            *   **Passo a Passo:**
                1.  Passo 1. {Tela: NomeDaTela}
                2.  Passo 2. {Tela: NomeDaTela}
            ```
    4. **Verify Views**: Ensure that every step referencing a `{Tela: ...}` corresponds to a Feature/View defined in `docs/ai/requirements/feature-{...}.md` (or triggers the **Features** workflow to create it).

- **Example Usage**:
    - **Input**: Add "Jornada 3: Cancelar Campanha" for "Gestor".
    - **Output**: `lean-inception.md` updated with the new journey steps.
