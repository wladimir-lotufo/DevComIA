---
description: Define or update Features in docs/ai/requirements folder
---

# Workflow: Features

- **Objective**: Define or update a **Feature** (macro View concept) in `docs/ai/requirements/feature-{FeatureName}.md`.

- **Inputs**:
    1. **Requirements Folder**: `docs/ai/requirements/`.
    2. **Feature Details**: Name, Description, Functionalities, Users.

- **Outputs**:
    1. **Updated Feature File**: `docs/ai/requirements/feature-{FeatureName}.md` with new or updated details.

- **Steps**:
    1. **Check Existence**: Check if `docs/ai/requirements/feature-{FeatureName}.md` exists.
    2. **Update/Create Feature**:
        - Add a new feature or update an existing one.
        - Format:
            ```markdown
            ## {View: NomeDaView}
            **Objetivo**: {Descrição}

            ### Feature: {Nome da Funcionalidade}
            **Descrição**: {Descrição detalhada}

            #### User Inputs
            1. **{Nome do Input}**: {Descrição}

            #### System
            1. **{Nome do Output}**: {Descrição}

            #### Actions
            1. **{Nome da Ação}**
                - {Detalhe da ação}
            
            ## User Stories
            - Relacione aqui os links para as micro US relativas a esta funcionalidade criadas em `docs/ai/requirements/user-stories/{FeatureName}/`.
            ```
    3. **Trigger User Story Workflow**: After defining the macro actions, trigger the **userstory** workflow to detail the Gherkin rules for each Action in individual files.
    4. **Trigger Prototype Workflow**: After defining all stories, it is recommended to run the **Prototype** workflow to create the HTML visualization.

- **Example Usage**:
    - **Input**: Define feature "RelatorioAdesao".
    - **Output**: `docs/ai/requirements/feature-relatorio-adesao.md` created with feature details.
