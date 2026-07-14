# MENTOR.md - Treinamentos Personalizados e Workflows Adicionais

> Este arquivo complementa o `GEMINI.md`, definindo os conhecimentos e fluxos de trabalho específicos e prioritários deste repositório, localizados no diretório `.mentor`.

---

## 🌟 TREINAMENTOS PERSONALIZADOS (PRIORIDADE MÁXIMA) 

> **MANDATORY:** O diretório `@[.mentor]` contém workflows, prompts, dados e conhecimentos personalizados de fluxo de trabalho que complementam (ou substituem) a base oficial do kit (`.agent`).

1. **Routing de Conhecimento:** Antes de aplicar qualquer regra padrão da pasta `.agent`, VERIFIQUE PRIMEIRO se existe um conhecimento correspondente em `@[.mentor/knowledge]` ou comandos em `@[.mentor/workflows]`.
2. **Prioridade de Sobrescrita:** Se uma instrução em `.mentor` entrar em conflito com uma instrução de `.agent`, **as regras de `.mentor` SÃO AS VENCEDORAS**.
3. **Uso de Prompts Customizados:** Utilize os modelos presentes em `@[.mentor/prompts]` sempre que a requisição de trabalho coincidir com o tema deles.

---

## 🤖 WORKFLOWS ADICIONAIS

Os comandos customizados existentes na pasta `.mentor` devem ser monitorados e priorizados caso invocados:

- **Todos os itens** dentro de `@[.mentor/workflows]` devem ser considerados comandos válidos com igual ou maior autoridade aos encontrados em `@[.agent/workflows]`.
