---
description: Create or Revise a User Story based on updated inputs.
---

1- **Inputs:**
    1. **Feature Name:** The feature/module this view belongs to (e.g., `Configurar Campanha`, `Filtrar Solicitações`, `Visualizar Ofertas`)

2- **Verify Changes:**
    1. The new User History should be based on the changes found.
    2. If changes are not found, ask for changes to be perfomed.

3- **Identify Context:**
    - Ask for the **Functionality/Goal** of the user story.
    - Ask for the **User Story ID** (e.g., US003) if not provided.
    - Ask for unexpected conditions or edge cases, clarifying then in Acceptance Criteria.

4- **Analyze Requirements**:
    - Based on the functionality, infer the **Persona** (defaults to "Gestor de Partnership" or similar if evident, otherwise ask).
    - Check related Business Entities at `docs/ai/design/data/` (to verify fields and relationships to be used, or to be created). 
    - Outline the **Acceptance Criteria**.
    - Identify relevant **Technical Notes** (Screen, Entities, APIs).

5- Group changes by affected View begerating a User Story for each View changes.

6- **Generate Content**:
    - Create the file content using the template below.

    ```markdown
    # História de Usuário: {Title}

    ## Propósito (Contexto .agent)
    *   **Problema**: [Descreva o problema que esta US resolve]
    *   **Objetivos e Não-Objetivos**: [Liste o que entra e o que não entra no escopo]

    ## User Story
    **Como** {Persona}  
    **Quero** {Goal}  
    **Para** {Benefit}

    ## Critérios de Aceitação

    - [ ] {Criteria 1}
    - [ ] {Criteria 2}
    - [ ] ...

    ## Definição de Pronto (DoD)

    - [ ] Produto, Personas e Jornadas revisados (docs/ai/product/lean-inception.md)
    - [ ] Funcionalidades da View revisadas (docs/ai/requirements/feature-{ViewName}.md)
    - [ ] Business Entities revisadas (docs/ai/design/data/{EntityName}.md)
    - [ ] Database Scripts revisados (infrastructure/sql/Scripts.sql)
    - [ ] Prototype revisado (docs/ai/design/prototypes/{FeatureName}/{ViewName}.html)
    - [ ] Código das APIs, Models, Controllers e Views revisado de acordo com objetivo da User Story

    ## Notas Técnicas

    - **View:** {Screen Name}
    - **Business Entities:** {Entities} (List of entities/fields affected by the user story)
        - {Entity Name}.{Field Name} {Type} {Description}
    - **API:** {API Name}

    ## Estimativa

    **Story Points:** {Points}

    ## Dependências

    - {Dependency 1}
    - {Dependency 2}
    ```

    6.  **Save File**:
        - Construct the file path inside the .agent context: `docs/ai/requirements/user-stories/{ViewName}/{ID}-{Title_Slug}.md`.
    - Create the file.
