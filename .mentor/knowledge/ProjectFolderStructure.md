# Estrutura de Pastas de um projeto gerenciado por Simplex

Esta é a definição da estrutura padrão de pastas de acordo com o modelo Simplex.

## docs/architecture
*   **Documento Principal**: `docs/architecture.md` (Ponto central contendo a definição da arquitetura do projeto, stack base e padrões).
*   **Decisões e ADRs**: Dentro do diretório `docs/architecture/` ficarão as subpastas ou arquivos contendo os **Architecture Decision Records (ADR)** com justificativas e trade-offs técnicos.


## 1-Design System
*   **Conteúdo**: Dentro da pasta 1-Design System teremos os arquivos que definem o Design System do projeto, com padrões visuasi e de código dos componenentes a serem utilizados nas telas do sistema.
    *   **Organização**: Podem ser organizados em subpastas de acordo com a conveniência do usuário.

## 2-Lean Inception
*   **Documento Principal**: [Lean Inception.md](../../2-Lean Inception/Lean%20Inception.md)

## 3-User Stories
*   **Subpastas**: Releases.
    *   **Convenção de Nome**: "Release {versão}"
    *   **Formato da Versão**: 3 números separados por ponto (ex: 1.0.0).
*   **Conteúdo**: Dentro da pasta da Release teremos os arquivos das User Stories.
    *   **Organização**: Podem ser organizados em subpastas de acordo com a conveniência do usuário.

## 4-ViewsAndFeatures
*   **Conteúdo**: Arquivos .md, onde cada arquivo corresponde a uma View.
*   **Estrutura Interna**: Dentro de cada arquivo de View estão as definições das features desta View.

## docs/ai/design/data
*   **Conteúdo**: Um arquivo .md para cada entidade de negócio.

## infrastructure/sql
*   **Conteúdo**: Scripts de criação do banco de dados.

## docs/ai/design/prototypes
*   **Conteúdo**: Protótipos padrão.
