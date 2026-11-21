# gsd-atlas-module-author (`gsd-atlas-module-author`)

> **Categoría**: Open-GSD: Developer & Browser Automation  
> **Autor / Organización**: [Open-GSD](https://github.com/open-gsd)  
> **Repositorio de Origen**: [gsd-atlas](https://github.com/open-gsd/gsd-atlas)  
> **Licencia**: MIT  

---

## 📌 ¿Qué hace este Skill?

Walks a contributor through writing a gsd-atlas language module: the atlas-lang.json manifest, the three query files (tags.scm, refs.scm, imports.scm), fixtures with golden files, the grammar lock and the parse-error budget, using the built-in TypeScript module as the worked example. Use when asked to add or fix a language module, edit a query, or make `gsd-atlas lang test` pass.

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
- `$gsd-atlas-module-author`
- `gsd-atlas-module-author`
- Invocaciones del router de fases de GSD o peticiones específicas relacionadas con su funcionalidad.

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras ejecutables por el agente.
- `README.md`: Documentación y referencias (este archivo).
