# Modern Web Guidance (Chrome & MDN Standards) (`modern-web-guidance`)

> **Categoría**: Web Platform & Extensions  
> **Autor / Creador**: Google Chrome, MDN, Microsoft Edge, Mozilla Firefox  
> **Fuente de origen**: [Google Chrome Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance)

---

## 📌 ¿Qué hace este Skill?

Herramienta de búsqueda y manual de referencia de mejores prácticas web modernas. Asegura el uso prioritario de APIs nativas de navegadores antes de recurrir a dependencias externas o librerías pesadas.

---

## ⚙️ ¿Cómo lo hace?

Provee una CLI integrada (`npx -y modern-web-guidance@latest search "<query>"`) y guías categorizadas:
- **Plataforma Nativa**: Diálogos modales con `<dialog>`, menús y popovers con Popover API, acordeones con `<details>/<summary>`, anclaje contextual con CSS Anchor Positioning.
- **CSS Moderno**: Layouts con CSS Grid y Subgrid, estilos modulares con Container Queries (`@container`), selectores relacionales con `:has()`, anidamiento nativo CSS y colores en `oklch()`.
- **Core Web Vitals & Rendimiento**: Prevención de CLS mediante `aspect-ratio`, optimización de LCP (`fetchpriority="high"`, `loading="lazy"`), protección de INP fragmentando tareas con `scheduler.yield()`.
- **Formularios & A11y**: Validación nativa con `:user-invalid`, semántica accesible y autofill adecuado.

---

## 🔗 Referencia a la Fuente

- **Origen**: Google Chrome Modern Web Guidance
- **Enlace oficial**: [https://github.com/GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)
- **Autoría**: Google Chrome, MDN, Microsoft Edge, Mozilla Firefox

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `modal`
- `dialog`
- `popover`
- `container queries`
- `view transitions`
- `scroll-driven animations`
- `core web vitals`
- `INP`
- `LCP`
- `CLS`
- `css has`
- `subgrid`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
