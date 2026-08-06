# vertlabs-web

Sitio estático de **Vertical Trail Labs** (`vertlabs.run`).

Este repo es público y contiene únicamente el resultado generado por el
Builder del repo privado `Vert_engine` (rama `web-builder`): HTML, CSS,
JS, imágenes/charts públicos y JSON públicos (`race.json`, `profile.json`,
`search.json`). No contiene Python, GPX crudos, ni resultados de timing
crudos.

No editar este contenido a mano: se regenera corriendo `python publish.py`
en `Vert_engine` y volviendo a copiar `output/` acá.

Deploy: Cloudflare Pages, build command vacío, output directory `/`.
