# Permissioned GitHub Operations & Governance (`permissioned-github`)

> **Categoría**: Agent Architecture & Multi-Agent Orchestration  
> **Autor / Creador**: Google DeepMind  
> **Fuente de origen**: [Google Antigravity Builtin Core](https://github.com/google/antigravity)

---

## 📌 ¿Qué hace este Skill?

Guía de gobernanza para la ejecución segura, controlada y consentida de operaciones de Git y GitHub (creación de repositorios, branches, PRs y commits).

---

## ⚙️ ¿Cómo lo hace?

Establece barreras de seguridad para interacción con repositorios:
- Exige verificación de diffs antes de cualquier push o modificación de ramas remotas.
- Define políticas de manejo de credenciales para evitar fugas de tokens en logs o artefactos.

---

## 🔗 Referencia a la Fuente

- **Origen**: Google Antigravity Builtin Core
- **Enlace oficial**: [https://github.com/google/antigravity](https://github.com/google/antigravity)
- **Autoría**: Google DeepMind

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `permissioned github`
- `operaciones seguras de git`
- `politicas github`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
