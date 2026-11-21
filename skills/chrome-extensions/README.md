# Chrome Extensions Manifest V3 Mastery (`chrome-extensions`)

> **Categoría**: Web Platform & Extensions  
> **Autor / Creador**: Google Chrome Team  
> **Fuente de origen**: [Google Chrome / Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance)

---

## 📌 ¿Qué hace este Skill?

Guía integral y reglas de desarrollo para construir extensiones de Chrome modernas y listas para producción utilizando Manifest V3, cumpliendo con todos los estándares y políticas de Chrome Web Store para garantizar su aprobación.

---

## ⚙️ ¿Cómo lo hace?

Aplica directivas obligatorias para Manifest V3:
- Arquitectura de Service Workers efímeros sin estado global persistente (uso obligatorio de `chrome.storage.local/session` o alarmas de Chrome).
- Aislamiento riguroso de Content Scripts y comunicación bidireccional mediante `chrome.runtime.sendMessage` y `Port`.
- Filtrado y redirección de red declarativa mediante `chrome.declarativeNetRequest` (reemplazo de `webRequestBlocking`).
- Cumplimiento estricto de Content Security Policy (CSP): eliminación de `eval()` y scripts remotos.
- Preparación para Chrome Web Store: redacción de justificaciones de permisos, sidebars, popups, opciones y políticas de privacidad.

---

## 🔗 Referencia a la Fuente

- **Origen**: Google Chrome / Modern Web Guidance
- **Enlace oficial**: [https://github.com/GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)
- **Autoría**: Google Chrome Team

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `Chrome extension`
- `browser extension`
- `manifest.json`
- `content script`
- `service worker`
- `side panel`
- `declarativeNetRequest`
- `publish extension`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
