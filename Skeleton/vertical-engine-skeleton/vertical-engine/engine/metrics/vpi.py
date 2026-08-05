"""
Vertical Power Index (VPI): metros de desnivel positivo por hora
en tramos de fuerte pendiente (>= 12%).

TODO: portar acá la lógica de ventanas de 500m y allocation
proporcional por esfuerzo que ya está validada en el Streamlit app.
Este módulo NUNCA debe importar nada de builder/ ni generar HTML.
"""


def calculate_vpi(segments: list[dict]) -> float:
    """
    segments: lista de tramos con 'distance_m', 'elevation_gain_m', 'time_s', 'slope_pct'
    Devuelve el VPI en m/h sobre los tramos de fuerte pendiente.
    """
    raise NotImplementedError("Portar lógica desde el Streamlit app.py")
