# Esquema de datos ("backend")

No hay backend ni autenticación: sitio estático. El "esquema" es el contrato de datos que
alimenta el build.

## projects.json (incrustado en build)
```jsonc
{
  "generated_at": "2026-10-15",          // fecha del último refresh
  "projects": [{
    "slug": "qzero",                      // id interno
    "name": "QZero",
    "tagline": "Zero-day network threat detection with QSVM + QI-VAE",
    "description": "…2 frases para RRHH…",
    "demo_url": "https://thempra.github.io/qzero/",
    "repo_url": "https://github.com/Thempra/qzero",
    "screenshot": "assets/qzero.webp",
    "stack": ["Python","Quantum ML","NDR","MIT"],
    "accent": "#8A5CFF",                  // tinte del borde de acento de la tarjeta
    "metrics": {
      "ncloc": 6001,
      "coverage_pct": 0.0,                // null → ocultar celda
      "bugs": 1,
      "vulnerabilities": 0,
      "code_smells": 129,
      "sources": ["SonarQube","DefectDojo","GitHub"]
    },
    "last_push": "2026-10-14",            // badge ACTIVE (se ocultan >90 días)
    "featured": true
  }]
}
```

## Reglas de visualización de métricas
- `vulnerabilities == 0` → se muestra en verde; `>0` → se oculta del sitio público
  (no se publican debilidades abiertas).
- `coverage_pct < 5` → se omite la celda (no mostrar 0%).
- `last_push` > 90 días → quitar chip ACTIVE, no mostrar fecha.

## Flujo de generación (pipeline de datos)
`GitHub API + SonarQube API + DefectDojo API (local, con tokens) → scripts/metrics_pull.py →
projects.json → build_index.py → index.html → git push → GitHub Pages`.

## Autenticación
Solo en el lado del pipeline (tokens locales `~/.sonar_token`, `~/.defectdojo_token`,
PAT en `~/.git-credentials`). Nada de credenciales en el repositorio público.
