# Agent Settings Migration Assistant (`migrate-agent-settings`)

> **Categoría**: Agent Architecture & Multi-Agent Orchestration  
> **Autor / Creador**: Google DeepMind  
> **Fuente de origen**: [Google Antigravity Builtin Core](https://github.com/google/antigravity)

---

## 📌 ¿Qué hace este Skill?

Herramienta de migración automática de configuraciones, servidores MCP, skills y reglas procedentes de otros asistentes de programación (Claude Code, Cursor, Codex, Gemini CLI) hacia Antigravity.

---

## ⚙️ ¿Cómo lo hace?

Escanea y convierte entornos de trabajo existentes:
- Localiza archivos de configuración ajenos (`claude.json`, `.cursorrules`, `settings.json`).
- Extrae definiciones de herramientas y las empaqueta ordenadamente en un nuevo plugin nativo de Antigravity sin pérdidas de funcionalidad.

---

## 🔗 Referencia a la Fuente

- **Origen**: Google Antigravity Builtin Core
- **Enlace oficial**: [https://github.com/google/antigravity](https://github.com/google/antigravity)
- **Autoría**: Google DeepMind

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `migrate agent`
- `migrar de claude code`
- `importar desde cursor`
- `importar reglas cursor`
- `migrar mcp`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
