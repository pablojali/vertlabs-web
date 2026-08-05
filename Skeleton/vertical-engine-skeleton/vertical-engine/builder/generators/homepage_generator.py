"""
Genera index.html a partir de la lista de carreras ya generada por race_generator.
Recibe `races` para no releer el JSON dos veces.
"""
from builder.env import env, write_page


def generate(races: list[dict]) -> None:
    template = env.get_template("index.html")
    # más recientes primero
    ordered = sorted(races, key=lambda r: (r["year"], r["date"]), reverse=True)
    html = template.render(races=ordered)
    write_page("index.html", html)


if __name__ == "__main__":
    from builder.generators.race_generator import load_races
    generate(load_races())
