"""
Configuración central del entorno Jinja2.
Todos los generators importan `env` desde acá para no repetir setup.
"""
from pathlib import Path
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES_DIR = Path(__file__).parent / "templates"
OUTPUT_DIR = Path(__file__).parent.parent / "output"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=select_autoescape(["html"]),
    trim_blocks=True,
    lstrip_blocks=True,
)

# Variables globales disponibles en todos los templates
env.globals["current_year"] = datetime.now().year


def write_page(relative_path: str, html: str) -> None:
    """
    Escribe una página HTML dentro de output/, creando carpetas si hace falta.
    relative_path ejemplo: 'races/aran-2026/index.html'
    """
    target = OUTPUT_DIR / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(f"  ✓ {relative_path}")
