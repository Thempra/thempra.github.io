# Brief de diseño

## Posicionamiento visual
"Taller de ingeniería serio", no plantilla de portfolio genérica. Referencias: landing de
Linear/Vercel en sobriedad, pero con personalidad propia oscura (consistente con las lands
existentes de QZero/VagusTrader: todas oscuras → identidad de familia).

## Paleta
- Fondo: `#0B0E14` (casi negro azulado), paneles `#11151F`, borde `#1C2333`
- Texto: `#E6EAF2` primario, `#8B94A7` secundario
- Acento primario: azul eléctrico `#4F7CFF` (CTAs, enlaces)
- Acento de estado "active": verde esmeralda `#2FD57F` (punto ● ACTIVE, métricas buenas)
- Alerta suave (solo si algo baja de umbral): ámbar `#F5A524`
- Degradado sutil de marca: azul→violeta (`#4F7CFF → #8A5CFF`) SOLO en el texto del H1, no en fondos.

## Tipografía
- System stack, sin descargas. H1 56/64px 700; H2 32px 650; cuerpo 16px/1.6; mono para
  métricas (`ui-monospace`) para look "terminal de ingeniero".

## Componentes
1. **Tarjeta de proyecto**: radio 14px, borde 1px `#1C2333`, sombra suave; screenshot arriba
   (ratio 16:10, recortado con object-fit), hover: borde azul + lift 2px. Contenido: título,
   tagline, badges de stack (píldoras discretas), fila de métricas monoespaciadas con
   etiquetas en mayúsculas pequeñas, dos botones (`Live demo` sólido azul / `Source` ghost).
2. **Chip ACTIVE**: punto verde parpadeante suave + "ACTIVE · pushed {mes año}".
3. **Stat strip**: 4 números grandes mono + label pequeño.
4. **Sección calidad**: 2 columnas (SonarQube | DefectDojo) con iconos inline SVG mínimos.

## Cada pantalla (única)
- **Hero**: alineado a la izquierda, badge superior "Open source · Self-hosted · Shipped",
  H1 en 2 líneas con degradado parcial, párrafo de 2 líneas, CTAs.
- **Projects**: grid 2 col @≥1024px, 1 col móvil, gap 24px, máx 1120px.
- **Calidad**: banda con fondo `#11151F` a ancho completo.
- **Footer**: centrado, 1 línea, gris.

## Tono
Copy en inglés, frases cortas, verbos de acción, cero buzzwords de IA. Los números hablan.
