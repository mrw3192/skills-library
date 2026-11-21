# gsd-atlas (`gsd-atlas`)

> **Categoría**: Open-GSD: Developer & Browser Automation  
> **Autor / Organización**: [Open-GSD](https://github.com/open-gsd)  
> **Repositorio de Origen**: [gsd-atlas](https://github.com/open-gsd/gsd-atlas)  
> **Licencia**: MIT  

---

## 📌 ¿Qué hace este Skill?

Use gsd-atlas before searching a repository for code by name, before editing a function, class or type, and when asked who calls, implements, extends or depends on something. It answers from a local, cited index: where a symbol is defined (code_find), every place that refers to it, calls it, extends it or implements it (code_refs), a symbol with its container and its file's imports (code_context), what is affected if it changes (code_impact), where an ADR file is and which code comments cite it (code_find and code_refs with kind: adr), why atlas said something (code_explain), and whether the index is current (atlas_status, lang_list). Prefer it to grep or to reading many files for a question about a function, class, method, type or ADR. Do not use it for text that is not a symbol (log messages, strings, config keys, comments) or when you already know the one file to read.

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
- **Repositorio**: [gsd-atlas](https://github.com/open-gsd/gsd-atlas)
- **Ruta original**: `open-gsd/gsd-atlas`

---

## 🎯 Disparadores y Palabras Clave (Triggers)

El agente activa este skill automáticamente ante menciones directas como:
- `$gsd-atlas`
- `gsd-atlas`
- Invocaciones del router de fases de GSD o peticiones específicas relacionadas con su funcionalidad.

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras ejecutables por el agente.
- `README.md`: Documentación y referencias (este archivo).
