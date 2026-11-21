# agent-inbox (`agent-inbox`)

> **Categoría**: Open-GSD: Developer & Browser Automation  
> **Autor / Organización**: [Open-GSD](https://github.com/open-gsd)  
> **Repositorio de Origen**: [agent-inbox](https://github.com/open-gsd/agent-inbox)  
> **Licencia**: MIT  

---

## 📌 ¿Qué hace este Skill?

Create temporary email inboxes and receive emails for testing auth flows, email verification, account confirmation, and any scenario where an AI agent needs to receive an email. Uses the agent-inbox MCP server with mail.tm + 1secmail fallback.

---

## ⚙️ ¿Cómo lo hace?

Este skill forma parte del ecosistema **Open-GSD** (*Git. Ship. Done.*), diseñado para garantizar que los agentes de programación operen de forma determinista y estructurada:
- Define directivas claras de meta-prompting y contratos de entrada/salida para el agente.
- Establece puntos de control (*gates*) de calidad antes de avanzar a la siguiente etapa.
- Asegura que el código se pruebe, valide y registre en git con trazabilidad absoluta.
- Minimiza la dispersión de contexto y evita que el agente tome decisiones unilaterales sin validación.

---

## 🔗 Referencia a la Fuente

- **Organización**: Open-GSD
- **Repositorio**: [agent-inbox](https://github.com/open-gsd/agent-inbox)
- **Ruta original**: `open-gsd/agent-inbox`

---

## 🎯 Disparadores y Palabras Clave (Triggers)

El agente activa este skill automáticamente ante menciones directas como:
- `$agent-inbox`
- `agent-inbox`
- Invocaciones del router de fases de GSD o peticiones específicas relacionadas con su funcionalidad.

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras ejecutables por el agente.
- `README.md`: Documentación y referencias (este archivo).
