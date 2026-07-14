# Estrutura do Documento Lean Inception

Este documento define a estrutura padrão e exemplos para o documento `Lean Inception.md`.

# Estrutura

## 1. Visão Produto
*   **Objetivo**: Definir o propósito fundamental do produto, o valor que ele entrega e para quem ele é destinado.
*   **Conteúdo**: Declarar de forma concisa o que é o produto, seus benefícios e diferencial.

## 1.1 Escopo e Restrições
*   **Objetivo**: Delimitar claramente as fronteiras do produto e evitar *Scope Creep*.
*   **Conteúdo**:
    *   **Out of Scope (Não-Objetivos)**: O que o sistema ou feature expressamente NÃO fará nesta versão ou fase de desenvolvimento operacional.
    *   **Constraints (Restrições)**: Limitações técnicas (ex: banco legado que não pode ser alterado), restrições de prazo ou orçamento, compatibilidade ou regulações exigidas.

## 2. Personas
*   **Objetivo**: Identificar e descrever os tipos de usuários e stakeholders.
*   **Conteúdo**:
    *   **Identificação**: Nome e ícone (ex: 👩‍🏫 Gestor).
    *   **Perfil**: Papel e responsabilidades.
    *   **Objetivo**: O que deseja alcançar.
    *   **Interações**: Principais ações no sistema.

## 3. Matriz de Responsabilidades (RACI)
*   **Objetivo**: Clarificar papéis em relação aos processos.
*   **Conteúdo**: Tabela cruzando *Atividades* x *Personas* (R, A, C, I).

## 4. Journeys (Jornadas do Usuário)
*   **Objetivo**: Mapear fluxos de trabalho essenciais.
*   **Conteúdo**:
    *   **Nome da Jornada**: Ação macro.
    *   **Objetivo**: Resultado esperado.
    *   **Entidades**: Dados envolvidos.
    *   **Passo a Passo**: Sequência numerada com referência `{View/Feature: Nome da View/Nome da Funcionalidade}`.

## 5. Workflows
*   **Objetivo**: Definir os fluxos de estado e transições para entidades do sistema.
*   **Conteúdo**:
    *   **Nome do Workflow**: Título do Workflow (ex: `### Workflow Nome`).
    *   **Campo Associado**: Link para o campo da entidade de negócio (ex: `**Campo Associado:** [Entidade.Campo](#link)`).
    *   **Estados**: Lista de estados e transições.
    *   **1. [Nome do Estado]**: Estado atual (ex: `1. Rascunho`).
        *   **1. para [Nome do Novo Estado]**: Transição (ex: `1. para Ativa`).
            *   **1. Regras**:
                *   **1. Personas que tem permissão**: Lista de personas.
                *   **2. Outras regras**: Lista de regras.

## 6. ViewsAndFeatures
*   **Objetivo**: Detalhar as interfaces e funcionalidades técnicas derivadas das jornadas.
*   **Conteúdo**: Cada View é armazenada em um arquivo separado na pasta `4-ViewsAndFeatures`.
    *   **Arquivo**: `{NomeDaView}.md`
    *   **Conteúdo do Arquivo**:
        *   **[Nome da View]**
            *   **Objetivo**: Propósito da interface.
            *   **Features**:
                *   ### Feature: [Nome da Funcionalidade]
                    *   **Descrição**: O que a funcionalidade faz tecnicamente.
                    *   **Regra**: O nome da Feature deve sempre ter um verbo de ação do usuário.
                    *   #### User Inputs
                        *   1. [Nome do Input]: Descrição.
                    *   #### System
                        *   1. [Ação do Sistema]: Descrição.
                    *   #### Actions
                        *   1. **[Nome da Ação]**
                            *   [Detalhe da ação]


## 7. BusinessEntities (Entidades de Negócio)
*   **Objetivo**: Definir o modelo de dados.
*   **Conteúdo**: Cada Entidade é armazenada em um arquivo separado na pasta `docs/ai/design/data`.
    *   **Arquivo**: `{NomeDaEntidade}.md`
    *   **Conteúdo do Arquivo**:
        *   **Entidade**: Nome da tabela.
        *   **Campos**: Tabela (Nome, Tipo, Tamanho, Descrição).
        *   **Relacionamentos**: Estrangeiras.

## 8. Glossário
*   **Objetivo**: Padronizar termos técnicos e de negócio.
*   **Conteúdo**: Lista de termos com definição.

# Exemplo

## 1. Visão Produto
> O **PartnerShip** é uma plataforma para **escritórios de advocacia** que **automatiza a gestão de dividendos**, diferente do **Excel** que **é manual e propenso a falhas**.

## 2. Personas
> **👩‍⚖️ Sócio Admin**
> *   **Objetivo**: Ter visibilidade total da distribuição de lucros.
> *   **Interações**: Aprovar pagamentos, visualizar relatórios.

## 3. Matriz de Responsabilidades (RACI)
> | Atividade | Sócio Admin | Advogado |
> | :--- | :---: | :---: |
> | Aprovar Pagamento | R | I |

## 4. Journeys (Jornadas do Usuário)
> **Jornada: Realizar Pagamento**
> 1. Usuário acessa lista de pendências `{View/Feature: Painel de Pagamentos/Listar}`.
> 2. Seleciona itens e confirma `{View/Feature: Painel de Pagamentos/Confirmar}`.

## 5. Workflows
> **### Workflow Pagamento**
> **Campo Associado:** [Pagamento.Status](#pagamento)
>
> 1. Pendente
>     1. para Pago
>         1. Regras:
>             1. Personas que tem permissão
>                 * Administrador
>             2. Outras regras
>                 * Saldo deve ser suficiente.

## 6. ViewsAndFeatures
> **Painel de Pagamentos**
> *   **Objetivo**: Confirmar pagamentos pendentes.
>
> ### Feature: Confirmar Pagamento
> **Descrição**: Processa o pagamento selecionado.
>
> #### User Inputs
> 1. **Data Efetiva** (Date).
>
> #### System
> 1. **ID Pagamento** (UUID), Status (Enum: Pago).
> 2. **Valor Total** (Decimal) - Só consulta.


## 7. BusinessEntities (Entidades de Negócio)
> **Pagamento**
> | Campo | Tipo | Descrição |
> | :--- | :--- | :--- |
> | id_Pagamento | UUID | PK |
| Status | [Workflow](#workflow-pagamento) | Status do pagamento |

## 8. Glossário
> **Cota**: Unidade de participação societária.
