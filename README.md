# thempra.github.io

Portfolio landing for https://thempra.github.io/ — one HTML file, one CSS block, zero frameworks.

- All metrics shown are real, pulled from SonarQube (`sast.thempra.net`) and DefectDojo
  instances plus the GitHub API. See `docs/` for the six foundation documents
  (PRD, TRD, flow, design brief, data schema, implementation plan).
- Refresh metrics locally: `python3 scripts/refresh_metrics.py` (reads local tokens from
  `~/.sonar_token`, `~/.defectdojo_token`, `~/.git-credentials`; never committed).
- Screenshots regenerated with headless Chrome; converted to WebP via ImageMagick.
