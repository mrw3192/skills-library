# Amazon Affiliate Comparison & Niche Studio (`crear-web-afiliados-amazon`)

> **Categoría**: Commercial & Monetization Web Apps  
> **Autor / Creador**: Skilio / Affiliate Studio v2  
> **Fuente de origen**: [Skilio (5 Skills para Ganar Dinero)](https://recursos.skilio.com/5-skills-ganar-dinero/)

---

## 📌 ¿Qué hace este Skill?

Construye sitios web de afiliados de Amazon basados en datos y comparadores interactivos de productos, listos para desplegar en Hostinger. Permite convertir listados planos de afiliados en motores de recomendación estructurados con fichas de producto, comparativas lado a lado, guías por categoría y paneles de radar-score.

---

## ⚙️ ¿Cómo lo hace?

Implementa un pipeline modular compuesto por 4 capacidades independientes:
1. **Conexión**: Conecta de forma segura y verifica la cuenta de Hostinger mediante el conector del agente.
2. **Arquitectura & Esquema**: Genera un esquema de datos normalizado (`productos.json` / `db.js`) y vistas web reactivas con HTML5, CSS moderno y Vanilla JavaScript sin dependencias pesadas.
3. **Pipeline de Poblado (Scraping & Normalización)**: Extrae datos desde URLs de afiliados mediante un scraper robusto con `google_search=True` para evadir anti-bots, preservando los tags de afiliado intactos, descargando imágenes en WebP y calculando puntuaciones editoriales.
4. **Despliegue & Producción**: Publica el sitio en Hostinger, valida pre-deploy checklists (tamaño < 8MB, sin dependencias de servidor complejas) y añade páginas de créditos y términos requeridos por Amazon Associates.

---

## 🔗 Referencia a la Fuente

- **Origen**: Skilio (5 Skills para Ganar Dinero)
- **Enlace oficial**: [https://recursos.skilio.com/5-skills-ganar-dinero/](https://recursos.skilio.com/5-skills-ganar-dinero/)
- **Autoría**: Skilio / Affiliate Studio v2

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `crea una web de afiliados`
- `web de comparativas de amazon`
- `blog de afiliados`
- `añade estos productos con mis enlaces`
- `amazon affiliate site`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
