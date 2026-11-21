# Dynamic Python Workflow Scripting (`run-workflow`)

> **Categoría**: Agent Architecture & Multi-Agent Orchestration  
> **Autor / Creador**: Google DeepMind  
> **Fuente de origen**: [Google Antigravity Builtin Core](https://github.com/google/antigravity)

---

## 📌 ¿Qué hace este Skill?

Orquestación programática avanzada mediante scripts dinámicos en Python para ejecutar pipelines de agentes, procesamientos por fases y fan-out masivo sobre archivos o módulos.

---

## ⚙️ ¿Cómo lo hace?

Expone primitivas de flujo de control para agentes:
- `agent()`: Invocación de subagentes con roles específicos.
- `parallel()`: Ejecución concurrente sobre colecciones de datos o archivos.
- `pipeline()`: Encadenamiento donde la salida de un agente nutre de entrada al siguiente.
- `phase()`: Segmentación de grandes proyectos en etapas ordenadas con puntos de control.

---

## 🔗 Referencia a la Fuente

- **Origen**: Google Antigravity Builtin Core
- **Enlace oficial**: [https://github.com/google/antigravity](https://github.com/google/antigravity)
- **Autoría**: Google DeepMind

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `run workflow`
- `script de orquestacion`
- `pipeline de agentes`
- `ejecutar workflow python`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
