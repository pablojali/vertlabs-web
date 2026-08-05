"""
Punto de entrada único del pipeline de publicación.

    python publish.py

Flujo:
  1. (futuro) correr el Engine para recalcular VPI/DMI/ER y refrescar data/
  2. generar páginas de carrera
  3. generar páginas de atleta
  4. generar homepage
  5. generar search.json
  6. generar sitemap.xml + robots.txt
  7. copiar assets estáticos
  8. copiar output/ al repo público (o dejar que GitHub Actions lo haga)
"""
import shutil
from pathlib import Path

from builder.generators import (
    race_generator,
    athlete_generator,
    homepage_generator,
    search_generator,
    sitemap_generator,
)

ROOT = Path(__file__).parent
ASSETS_SRC = ROOT / "assets"
OUTPUT_DIR = ROOT / "output"


def copy_assets() -> None:
    dest = OUTPUT_DIR / "assets"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(ASSETS_SRC, dest)
    print(f"  ✓ assets/ copiados a output/assets/")


def main() -> None:
    print("1/6 Generando páginas de carrera...")
    races = race_generator.generate()

    print("2/6 Generando páginas de atleta...")
    athletes = athlete_generator.generate()

    print("3/6 Generando homepage...")
    homepage_generator.generate(races)

    print("4/6 Generando índice de búsqueda...")
    search_generator.generate(races, athletes)

    print("5/6 Generando sitemap y robots.txt...")
    sitemap_generator.generate(races, athletes)

    print("6/6 Copiando assets estáticos...")
    copy_assets()

    print(f"\nListo. Sitio generado en: {OUTPUT_DIR}")
    print("Siguiente paso: commitear/pushear output/ al repo vertlabs-site")
    print("(manual por ahora; automatizar con GitHub Actions, ver README).")


if __name__ == "__main__":
    main()
