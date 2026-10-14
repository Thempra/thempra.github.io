# Flujo de la app

Es una landing estática de una sola página; el "flujo" es el recorrido de lectura/scroll.

## Recorrido del visitor (recruiter)
1. **Entrada** → `https://thempra.github.io/`
2. **Hero (above the fold)**: nombre + rol ("Building shipped software, not demos") + 2 CTAs:
   - `View projects` → scroll suave a `#projects`
   - `GitHub ↗` → `https://github.com/Thempra` (pestaña nueva)
3. **Strip de credenciales**: 4 stats agregadas (proyectos activos, LOC totales, 0 vulns
   abiertas, cobertura media) — gancho cuantitativo en 3 s.
4. **Grid #projects**: tarjetas. Cada tarjeta:
   - Click en screenshot o `Live demo ↗` → abre la GitHub Page del proyecto (pestaña nueva)
   - Click en `Source` → abre el repo (pestaña nueva)
   - Chip `● ACTIVE` con último push → informational (no clic)
   - Fila de métricas → informational, tooltips nativos `title` explican la fuente
5. **#quality**: bloque "How this is measured" — SonarQube + DefectDojo autoalojados,
   scans en CI. Enlace a los dashboards públicos donde exista.
6. **Footer**: contacto (email), GitHub, "Built with zero frameworks" (guiño técnico).

## Estados
- Sin JS: los enlaces y anclas funcionan; si JS ausente, nada se rompe.
- Imagen falla → `alt` + fondo de gradiente de marca (la tarjeta sigue siendo usable).

## Navegación secundaria
- Ninguna. No hay menú, no hay rutas. Una página, un scroll, muchos enlaces salientes.
