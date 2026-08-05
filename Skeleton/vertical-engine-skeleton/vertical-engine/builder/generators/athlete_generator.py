"""
Lee data/athletes/*.json y genera una página estática por atleta.
"""
import json
from pathlib import Path
from builder.env import env, write_page

DATA_DIR = Path(__file__).parent.parent.parent / "data" / "athletes"


def load_athletes() -> list[dict]:
    athletes = []
    for f in sorted(DATA_DIR.glob("*.json")):
        athletes.append(json.loads(f.read_text(encoding="utf-8")))
    return athletes


def generate() -> list[dict]:
    template = env.get_template("athlete.html")
    athletes = load_athletes()

    for athlete in athletes:
        html = template.render(athlete=athlete)
        write_page(f"athletes/{athlete['slug']}/index.html", html)

    return athletes


if __name__ == "__main__":
    generate()
