---
description: Define or update Business Entities in docs/ai/design/data folder
---

# Workflow: BusinessEntities

- **Objective**: Define or update a **Business Entity** in `docs/ai/design/data/{EntityName}.md`.

- **Inputs**:
    1. **Business Entities Folder**: `docs/ai/design/data/`.
    2. **Entity Details**: Name, Attributes, Relationships.

- **Outputs**:
    1. **Updated Entity File**: `docs/ai/design/data/{EntityName}.md`.

- **Steps**:
    1. **Check Existence**: Check if `docs/ai/design/data/{EntityName}.md` exists.
    2. **Update/Create Entity**:
        - Add a new entity or update an existing one.
        - Format:
            ```markdown
            ### {Entity: NomeDaEntidade}
            *   **Descrição:** {Descrição}
            *   **Atributos:**
                *   {NomeDoAtributo}: {Tipo} - {Descrição}
            ```
    3. **Trigger Database Workflow**: After defining an Entity, it is recommended to run the **Database** workflow to generate the SQL script.

- **Example Usage**:
    - **Input**: Define entity "Notificacao".
    - **Output**: `docs/ai/design/data/Notificacao.md` created with table definition.
