# gsd-verify-work (`gsd-verify-work`)

> **Categoría**: Open-GSD: Core Engineering & Quality  
> **Autor / Organización**: [Open-GSD](https://github.com/open-gsd)  
> **Repositorio de Origen**: [gsd-core](https://github.com/open-gsd/gsd-core)  
> **Licencia**: MIT  

---

## 📌 ¿Qué hace este Skill?

Validate built features through conversational UAT

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
- **Repositorio**: [gsd-core](https://github.com/open-gsd/gsd-core)
- **Ruta original**: `open-gsd/gsd-core`

---

## 🎯 Disparadores y Palabras Clave (Triggers)

El agente activa este skill automáticamente ante menciones directas como:
- `$gsd-verify-work`
- `gsd-verify-work`
- Invocaciones del router de fases de GSD o peticiones específicas relacionadas con su funcionalidad.

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras ejecutables por el agente.
- `README.md`: Documentación y referencias (este archivo).
