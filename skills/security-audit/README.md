# Cloudflare Source-First Security Audit (`security-audit`)

> **Categoría**: Security & Vulnerability Assessment  
> **Autor / Creador**: Cloudflare  
> **Fuente de origen**: [Cloudflare Security Audit Skill](https://github.com/cloudflare/security-audit-skill)

---

## 📌 ¿Qué hace este Skill?

Marco de auditoría de seguridad defensiva enfocado en el código fuente para detectar, evaluar y corregir vulnerabilidades reales que violan límites de confianza en repositorios, microservicios, APIs y librerías.

---

## ⚙️ ¿Cómo lo hace?

Ejecuta una metodología rigurosa en 6 fases:
1. **Fase 1 - Alcance & Límites de Confianza**: Identifica actores, privilegios esperados y datos sensibles.
2. **Fase 2 - Reconocimiento de Superficie**: Cartografía rutas de entrada, endpoints desprotegidos y flujos de entrada no sanitizados.
3. **Fase 3 - Análisis de Candidatos**: Evaluación estricta de posibles fallos (inyecciones, fallos de autorización/IDOR, CSRF, SSRF, desbordamientos).
4. **Fase 4 - Verificación & Reproducción**: Pruebas de concepto seguras y no destructivas en entorno local.
5. **Fase 5 - Clasificación & Severidad**: Calificación fundamentada en impacto real (evitando falsos positivos).
6. **Fase 6 - Remediación**: Propuesta de parches mínimos efectivos con pruebas de regresión asociadas.

---

## 🔗 Referencia a la Fuente

- **Origen**: Cloudflare Security Audit Skill
- **Enlace oficial**: [https://github.com/cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)
- **Autoría**: Cloudflare

---

## 🎯 Disparadores y Palabras Clave (Triggers)

Este skill es activado automáticamente por el agente ante las siguientes intenciones o menciones:

- `security audit`
- `vulnerability review`
- `pen test`
- `auditoria de seguridad`
- `analisis de vulnerabilidades`
- `revisar seguridad`

---

## 📂 Archivos del Skill

- `SKILL.md`: Instrucciones maestras del skill (formato nativo de agentes IA).
- `README.md`: Documentación, origen y cómo funciona (este archivo).
- *Archivos complementarios*: Si el skill incluye plantillas, scripts de evaluación o guías de referencia, se encuentran ubicados en subcarpetas dentro de este directorio.
