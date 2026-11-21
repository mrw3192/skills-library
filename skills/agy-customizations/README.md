# Antigravity Customization Architecture (`agy-customizations`)

> **Categoría**: Agent Architecture & Multi-Agent Orchestration  
> **Autor / Creador**: Google DeepMind  
> **Fuente de origen**: [Google Antigravity Builtin Core](https://github.com/google/antigravity)

---

## 📌 ¿Qué hace este Skill?

Manual técnico sobre la arquitectura y el ciclo de vida de las extensiones de Antigravity: skills, reglas (`AGENTS.md`), plugins empaquetados, sidecars y servidores MCP.

---

## ⚙️ ¿Cómo lo hace?

Explica las entrañas del sistema de personalización:
- Jerarquía y precedencia de descubrimiento: extensiones integradas (`builtin`), globales de usuario (`~/.gemini/config/`) y específicas de workspace (`.agents/`).
- Límites de presupuesto de contexto (budgets) y políticas de inclusión automática vs bajo demanda.
- Especificación formal para empaquetado de plugins en `plugin.json` y gestión de permisos granulares.

---

## 🔗 Referencia a la Fuente

- **Origen**: Google Antigravity Builtin Core
- **Enlace oficial**: [https://github.com/google/antigravity](https://github.com/google/antigravity)
- **Autoría**: Google DeepMind

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `customizations`
- `como funcionan los skills`
- `priority skills`
- `crear customizacion`
- `reglas de workspace`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
