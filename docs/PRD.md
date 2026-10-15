# PRD — Thempra Portfolio (thempra.github.io)

## Idea general
Página raíz del usuario GitHub de Thempra (`https://thempra.github.io/`), hoy en 404.
Un portfolio profesional de ingeniería que lista los proyectos publicados en GitHub Pages,
demuestra que están **vivos y activos** (métricas públicas reales) y enlaza a cada web.

## Público objetivo
1. **RRHH / recruiters**: necesitan entender en 10 segundos qué hace cada proyecto, en qué
   tecnologías está escrito y que el candidato mantiene software real en producción.
2. **Ingenieros / técnicos entrevistadores**: necesitan evidencia verificable (repo, métricas
   de calidad SAST/DAST, actividad reciente), no marketing.

## Funcionalidades
- **F-1 Landing single-page** con identidad personal (nombre, rol, tagline) y CTAs
  (GitHub, email/contacto).
- **F-2 Grid de proyectos activos**: 4 tarjetas (QZero, VagusTrader, Overmind NG, p92-checklist),
  cada una con:
  - Screenshot real de la web (self-hosted, WebP)
  - Qué es (1-2 frases orientadas a valor, sin jerga innecesaria)
  - Stack técnico (badges de tecnologías)
  - Métricas de calidad en vivo: LOC, cobertura, bugs/vulnerabilidades abiertas (SonarQube),
    hallazgos de seguridad (DefectDojo)
  - Enlace "Ver demo" → GitHub Pages + enlace "Código" → repo GitHub
- **F-3 Sección "Calidad verificable"**: explica de dónde salen las métricas (SonarQube +
  DefectDojo autoalojados) — diferenciador frente a portfolios con proyectos juguete.
- **F-4 Badges "ACTIVE"** con fecha del último push real de cada repo.
- **F-5 Bilingüe pasivo**: contenido en inglés por defecto (estándar dev internacional),
  sin toggle (coste/beneficio bajo para una landing).
- **F-6 Responsive** (móvil primero en ancho de tarjeta; many recruiters scan on phones).
- **F-7 Sin frameworks ni build step**: HTML+CSS estático, carga <1s, zero deps.

## Fuera de alcance
- Proyectos no publicados en Pages (se listan en una fila discreta "more on GitHub").
- Animaciones pesadas, contador de visitas, analítica.
- Backend propio.

## Criterios de aceptación
- AC-1: `https://thempra.github.io/` devuelve 200 y muestra el portfolio.
- AC-2: Cada tarjeta enlaza a su demo y a su repo (URLs verificadas 200).
- AC-3: Métricas mostradas provienen de datos reales extraídos de SonarQube/DefectDojo/GitHub
  (nunca inventadas); se regeneran con un script.
- AC-4: Lighthouse performance ≥ 95, accesibilidad ≥ 95.
- AC-5: Render correcto a 375px, 768px y 1440px.
