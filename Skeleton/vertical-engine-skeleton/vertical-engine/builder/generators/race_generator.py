"""
Lee data/races/*.json y genera una página estática por carrera.
No conoce nada del Engine: solo consume JSON ya calculado.
"""
import json
from pathlib import Path
from builder.env import env, write_page

DATA_DIR = Path(__file__).parent.parent.parent / "data" / "races"


def load_races() -> list[dict]:
    races = []
    for f in sorted(DATA_DIR.glob("*.json")):
        races.append(json.loads(f.read_text(encoding="utf-8")))
    return races


def generate() -> list[dict]:
    """Genera todas las páginas de carrera y devuelve la lista de carreras
    (la homepage y el sitemap la reutilizan, así se lee el JSON una sola vez)."""
    template = env.get_template("race.html")
    races = load_races()

    for race in races:
        html = template.render(race=race)
        write_page(f"races/{race['slug']}/index.html", html)

    return races


if __name__ == "__main__":
    generate()
