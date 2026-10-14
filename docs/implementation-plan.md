# Plan de implementación

1. [x] Descubrimiento: enumerar repos con Pages activas (API) + verificar 200 en cada demo.
2. [x] Repo user-site `Thempra/thempra.github.io` creado vía API.
3. [x] Screenshots headless (Chrome) + conversión WebP.
4. [x] Extracción de métricas reales: SonarQube (ncloc/coverage/bugs/vulns) y DefectDojo
   (hallazgos activos por severidad) + GitHub (pushed_at, language).
5. [ ] Redactar los 6 docs fundacionales (este documento) ✔ en curso→hecho.
6. [ ] `build_index.py`: template HTML + inyección de projects.json + copiado de assets.
7. [ ] QA local: servir con `python -m http.server`, screenshots a 375/768/1440,
    visión self-check, links verificados con curl.
8. [ ] Push a `main`, esperar Pages, verificar `https://thempra.github.io/` 200.
9. [ ] Script `scripts/refresh_metrics.py` versionado (sin tokens) para mantener fresco.
10. [ ] Informe final al usuario con screenshots y URL.

## Criterio de terminado
Lo mismo que AC-1..AC-5 del PRD, verificado con ejecución real (no asumido).
