# gsd-loop-schedule (`gsd-loop-schedule`)

> **Categoría**: Open-GSD: Spec-Build Iterative Loop  
> **Autor / Organización**: [Open-GSD](https://github.com/open-gsd)  
> **Repositorio de Origen**: [gsd-spec-build-loop](https://github.com/open-gsd/gsd-spec-build-loop)  
> **Licencia**: MIT  

---

## 📌 ¿Qué hace este Skill?

Create or update a native recurring task that repeatedly runs one-pass gsd-loop builder or reviewer work. Use when asked to keep the build or review queue running, schedule gsd-loop, or automate repeated passes.

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
- **Repositorio**: [gsd-spec-build-loop](https://github.com/open-gsd/gsd-spec-build-loop)
- **Ruta original**: `open-gsd/gsd-spec-build-loop`

---

## 🎯 Disparadores y Palabras Clave (Triggers)

El agente activa este skill automáticamente ante menciones directas como:
- `$gsd-loop-schedule`
- `gsd-loop-schedule`
- Invocaciones del router de fases de GSD o peticiones específicas relacionadas con su funcionalidad.

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras ejecutables por el agente.
- `README.md`: Documentación y referencias (este archivo).
