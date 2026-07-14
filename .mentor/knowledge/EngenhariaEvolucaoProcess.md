# O Processo Mentor

O Processo Mentor é um fluxo de trabalho estruturado e documentado em seu repositório (baseado nas diretrizes da pasta `.mentor`) que guia a construção de software desde a concepção do produto até a implementação técnica final de ponta a ponta. Ele divide o desenvolvimento em etapas interligadas onde a saída de uma fase é a entrada da próxima, garantindo consistência, previsibilidade e integração entre UI/UX, Banco de Dados e Backend.

Dependendo da fase, o processo é conduzido por agentes especializados (`project-planner`, `orchestrator`, `frontend-specialist`, `backend-specialist`, etc.) e utiliza uma série de **Workflows** (`/Personas`, `/Jornadas`, `/Features`, `/Api`, etc.) definidos na pasta `.mentor/workflows`.

Abaixo está o detalhamento completo de ponta a ponta:

---

## 0. Fase de Arquitetura e Design System
Define as fundações técnicas, padrões visuais e o stack tecnológico que norteará todo o desenvolvimento e as fases seguintes.

### Etapa 0.1: Definição de Arquitetura
* **Workflow:** `/Architecture` (ou processo de documentação técnica)
* **Agentes:** `orchestrator` / `expert-architect`
* **Entradas:** Requisitos de alto nível, restrições não funcionais, escopo do negócio.
* **Saídas:** Documento Principal de Arquitetura (`docs/architecture.md`) definindo o stack (MVC, SPA, Mobile, etc), e Architecture Decision Records (ADRs) armazenados em `docs/architecture/`.

### Etapa 0.2: Design System
* **Workflow:** `/DesignSystem`
* **Agentes:** `frontend-specialist` / `designer`
* **Entradas:** Diretrizes de marca, requisitos visuais.
* **Saídas:** Documento de Design System (ex: `docs/ai/design/designsystem.md`) estabelecendo tokens de cores, tipografia e componentes base.

---

## 1. Fase de Concepção de Produto (Product)
Onde o sistema é idealizado sob a ótica de quem vai usá-lo.

### Etapa 1.1: Personas
* **Workflow:** `/Personas`
* **Agentes:** `project-planner` / `orchestrator`
* **Entradas:** Contexto do negócio, perfis de usuários ideais.
* **Saídas:** Arquivo atualizado `docs/ai/product/lean-inception.md` (Adicionando a "Persona", com Perfil, Objetivo e Interações).

### Etapa 1.2: Jornadas de Usuário
* **Workflow:** `/Jornadas`
* **Agentes:** `project-planner`
* **Entradas:** O arquivo `lean-inception.md` gerado anteriormente e os objetivos das Personas.
* **Saídas:** Arquivo atualizado `docs/ai/product/lean-inception.md` contendo um passo a passo do fluxo que o usuário percorrerá no sistema, citando entidades e telas.

---

## 2. Fase de Requisitos (Requirements)
Onde as jornadas se transformam em especificações funcionais claras.

### Etapa 2.1: Features (Visão Macro)
* **Workflow:** `/Features`
* **Agentes:** `orchestrator`
* **Entradas:** Jornadas e listagem de telas do Lean Inception.
* **Saídas:** Arquivo `docs/ai/requirements/feature-{ViewName}.md` (Define o objetivo da tela, inputs, outputs, e ações do sistema).
* **Conexão:** Finalizar uma Feature engatilha obrigatoriamente a criação das User Stories e Protótipos.

### Etapa 2.2: Histórias de Usuário (Visão Micro/Gherkin)
* **Workflow:** `/userstory`
* **Agentes:** `project-planner` / `orchestrator`
* **Entradas:** A Feature da visão macro, Personas.
* **Saídas:** Arquivo `docs/ai/requirements/user-stories/{ViewName}/{ID}-{Title}.md` (Detalhamento técnico, Critérios de Aceitação e *Definition of Done* (DoD) para a equipe de desenvolvimento).

---

## 3. Fase de Design e Prototipação (Design)
Processo conduzido na abordagem **"UI-First" (Momento 1)**, separando completamente o visual do backend.

### Etapa 3.1: Entidades de Negócio (Dados)
* **Workflow:** `/BusinessEntities`
* **Agentes:** `database-design` / `backend-specialist`
* **Entradas:** Requisitos da Feature e User Story (quais campos precisam ser salvos).
* **Saídas:** Arquivo de definição de entidade `docs/ai/design/data/{EntityName}.md` (Define atributos, relacionamentos 1-N, tipos, etc).

### Etapa 3.2: Protótipo Visual (UI)
* **Workflow:** `/Prototype`
* **Agentes:** `frontend-specialist`
* **Entradas:** Documento de Arquitetura, Feature, User Story, Design System.
* **Saídas:** Mockups e protótipos visuais de alta fidelidade gerados já na estrutura de código final usando as diretrizes de arquitetura de frontend predefinida no documento de arquitetura. O código gerado aqui (`.xaml`, `.razor`, `.tsx`, etc) será 100% reaproveitado no momento da integração com backend na Fase 4, adotando a abordagem UI-First.
* **Validação (Fase X):** Audita UX/UI, Acessibilidade (WCAG) e Qualidade estática.

---

## 4. Fase de Implementação Técnica (Momento 2)
É onde as Entidades e Protótipos viram código real em C#/SQL/Razor usando os arquivos gerados nas Fases 2 e 3.

### Etapa 4.1: Banco de Dados
* **Workflow:** `/Database`
* **Agentes:** `database-design`
* **Entradas:** Entidades de negócio (`docs/ai/design/data/*.md`).
* **Saídas:** 
    1. Arquivo SQL DDL incrementado (`infrastructure/sql/Scripts.sql`).
    2. Criação das Classes de Modelo em C# (`APIs/{Table}/Mod{Table}.cs` ou legados).

### Etapa 4.2: Construção da API (Data Access Layer)
* **Workflow:** `/Api`
* **Agentes:** `backend-specialist`
* **Entradas:** Modelo gerado anteriormente e o SQL Script.
* **Saídas:** Classe `APIs/{TableName}/Db{TableName}.cs` contendo os métodos CRUD (`DalIncluir`, `DalConsultar`, etc) com o mapeamento nativo (`SqlDataReader`) e as anotações **Simplex Notation**. Gera também Testes de Integração e Unidade.

### Etapa 4.3: Controller
* **Workflow:** `/Controller`
* **Agentes:** `backend-specialist`
* **Entradas:** Nome da View, Feature requirements e Protótipo frontend.
* **Saídas:** Arquivo `Controllers/{ControllerName}Controller.cs`. Ele interage com as APIs, manipula conexões e gera endpoints (ex: `JsonResult`) capazes de absorver as chamadas AJAX vindas do Frontend.
* **Validação:** Roda `security_scan.py` e linting no código.

### Etapa 4.4: View (Front + Back)
* **Workflow:** `/View`
* **Agentes:** `frontend-specialist`
* **Entradas:** Frontend Protótipo (`Momento 1`), Controller gerado (`Etapa 4.3`), APIs e User Stories.
* **Saídas:** 
    1. A página final conectada será gerada nativamente na tecnologia de frontend definida na arquitetura do projeto (reaproveitando o código e design do Momento 1).
    2. Para projetos de arquitetura padrão MVC/Simplex: gerada inicialização da **Simplex View Definition**, Model local e Razor view (`.cshtml`), com métodos JavaScript e AJAX vinculados aos endpoints REST do backend.
    3. Para projetos Web SPA/Mobile: Integração de HTTP Clients, validações de negócio profundas, gerenciamento de estados, e chamadas das APIs construídas na Etapa 4.2.

---

## 5. Fase de Integração e Entrega (CI/CD)
A esteira final que garante que as implementações técnicas da Fase 4 cheguem aos ambientes com segurança e automação.

### Etapa 5.1: Pipeline de Validação
* **Workflow:** Automático (Trigger via Merge/Pull Request)
* **Agentes:** `security-auditor` / `testing-patterns`
* **Entradas:** Código finalizado integrado na Fase 4.
* **Saídas:** Relatórios de Lints, Análise Estática (SAST/SCA) e Testes de Regressão Automatizados.

### Etapa 5.2: Release e Deploy
* **Workflow:** `/Deploy` (ou script manual `.agent/scripts/checklist.py --url`)
* **Agentes:** `orchestrator`
* **Entradas:** Código validado (Release Candidate).
* **Saídas:** Sistema ativado nos ambientes alvo (Homologação, Staging ou Produção).
* **Conexão:** Finaliza o ciclo iterativo do desenvolvimento para a respectiva Feature.

---

## Diagrama do Processo (Workflows)

Abaixo é possível visualizar como as etapas se integram. O diagrama completo no formato Draw.io (Flowchart) demonstrando todos os Workflows como ações, e os Artefatos de Entrada/Saída transitando entre as fases, foi extraído para o arquivo:

🔗 **[processos.drawio](file:///c:/Users/wladi/source/repos/Imobiliaria/.mentor/knowledge/processos.drawio)**
