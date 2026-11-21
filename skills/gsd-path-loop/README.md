# gsd-path-loop (`gsd-path-loop`)

> **Categoría**: Open-GSD: Path Lifecycle Pipeline  
> **Autor / Organización**: [Open-GSD](https://github.com/open-gsd)  
> **Repositorio de Origen**: [gsd-path](https://github.com/open-gsd/gsd-path)  
> **Licencia**: MIT  

---

## 📌 ¿Qué hace este Skill?

Use only when the user explicitly invokes $gsd-path-loop. Runs one bounded loop pass from a LOOP.md spec — gate checks, independent verification, one fix worker, telemetry. Autonomy lives in the external scheduler that invokes this skill; the skill never schedules itself.

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
- **Repositorio**: [gsd-path](https://github.com/open-gsd/gsd-path)
- **Ruta original**: `open-gsd/gsd-path`

---

## 🎯 Disparadores y Palabras Clave (Triggers)

El agente activa este skill automáticamente ante menciones directas como:
- `$gsd-path-loop`
- `gsd-path-loop`
- Invocaciones del router de fases de GSD o peticiones específicas relacionadas con su funcionalidad.

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras ejecutables por el agente.
- `README.md`: Documentación y referencias (este archivo).
