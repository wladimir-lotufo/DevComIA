---
description: Define or update Personas in lean-inception.md
---

# Workflow: Personas

- **Objective**: Define or update the **Personas** section in `docs/ai/product/lean-inception.md`.

- **Inputs**:
    1. **Lean Inception File**: `docs/ai/product/lean-inception.md`.
    2. **Persona Details**: Name, Profile, Objective, Interactions.

- **Outputs**:
    1. **Updated Lean Inception File**: `docs/ai/product/lean-inception.md` with new or updated Personas.

- **Steps**:
    1. **Read Lean Inception**: Read `docs/ai/product/lean-inception.md` and locate the `# Personas` section.
    2. **Identify Persona**: Check if the persona already exists.
    3. **Update/Create**:
        - If it exists, update the Profile, Objective, or Interactions as requested.
        - If new, append a new subsection `### {Icon} {Persona Name}`.
        - Format:
            ```markdown
            ### 👩‍🏫 Gestor de Partnership
            * **Perfil:** Responsável por...
            * **Objetivo:** Engajar sócios...
            * **Interações:** Cria campanhas...
            ```
    4. **Update RACI Matrix**: Check if the new persona needs to be added to the RACI matrix in the same file.

- **Example Usage**:
    - **Input**: Create persona "Auditor Externo".
    - **Output**: `Lean Inception.md` updated with "Auditor Externo" details.
