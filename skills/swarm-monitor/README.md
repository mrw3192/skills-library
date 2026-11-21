# Swarm Health Monitor & Stall Detector (`swarm-monitor`)

> **Categoría**: Agent Architecture & Multi-Agent Orchestration  
> **Autor / Creador**: Google DeepMind  
> **Fuente de origen**: [Google Antigravity Builtin Core](https://github.com/google/antigravity)

---

## 📌 ¿Qué hace este Skill?

Guardián de ejecución para enjambres multiagente. Detecta si el grupo de trabajo se ha quedado bloqueado o sin actividad y reactiva al miembro adecuado.

---

## ⚙️ ¿Cómo lo hace?

Opera como un watchdog en segundo plano:
- Supervisa los tiempos de respuesta y la presencia de bloqueos en el tablero de mensajes compartido.
- Notifica al coordinador o al trabajador específico para destrabar el avance sin reiniciar todo el enjambre.

---

## 🔗 Referencia a la Fuente

- **Origen**: Google Antigravity Builtin Core
- **Enlace oficial**: [https://github.com/google/antigravity](https://github.com/google/antigravity)
- **Autoría**: Google DeepMind

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `swarm monitor`
- `destrabar swarm`
- `supervisar enjambre`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
