# TRD — Requisitos técnicos

## Stack
| Capa | Decisión | Justificación |
|---|---|---|
| Sitio | HTML estático + CSS moderno (grid, custom props) + ~0 JS | Zero-deps, Lighthouse 100 posible, sin build step que rompa Pages |
| Hosting | Repo `Thempra/thempra.github.io` rama `main` → GitHub Pages (user site) | Publica automáticamente en la raíz pedida |
| Imágenes | WebP auto-generadas (screenshots headless Chrome → ImageMagick) | <60 KB cada una |
| Tipografía | System font stack (`-apple-system, Inter, Segoe UI, Roboto…`) | Cero peticiones externas, aspecto profesional |
| Datos | `projects.json` embebido en el HTML, regenerado por script | Sin API runtime; métricas horneadas en el build |

## Fuentes de datos (scripts de regeneración)
1. **GitHub REST API** (sin auth, rate 60/h suficientegit): `pushed_at`, stars, language por repo → badge "Active".
2. **SonarQube** `sast.thempra.net/api/measures/component` (token local `~/.sonar_token`):
   ncloc, coverage, bugs, vulnerabilities, code_smells, ratings.
3. **DefectDojo** `dojo.thempra.net/api/v2/findings/?product_name=X&active=true` (token local,
   `--resolve dojo.thempra.net:443:192.168.50.5`): conteos por severidad.
4. **Screenshots**: `google-chrome --headless=new --window-size=1440,900 --screenshot` de cada demo.

## Restricciones duras
- Los tokens **nunca** se suben al repo ni aparecen en el HTML. El script corre en local; el
  repo solo contiene los números agregados.
- Métricas de seguridad: se publican solo métricas favorables y verdaderas (0 vulnerabilities,
  cobertura real). No se publican counts de hallazgos abiertos de DAST (sensibles); sí "0
  critical/high SAST" cuando sea cierto.
- No dependencias de CDN externas (ni fuentes, ni JS): el sitio debe funcionar offline-first.

## Mapa proyectos → recursos
| demo URL | repo | sonar key | dojo product |
|---|---|---|---|
| /qzero/ | Thempra/qzero | qzero | qzero |
| /vagustrader/ | Thempra/vagustrader | vagustrader | vagustrader |
| /overmind-ng/ | Thempra/overmind-ng | overmind_flutter | overmind_flutter |
| /kidsclock/ | Thempra/kidsclock | (no scaneado → ocultar bloque métricas) | — |

## Deploy
`git push origin main` → Pages. Repo creado vía API con PAT fine-grained.
