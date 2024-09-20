import math
def polar_a_cartesianas(polar):
    r, theta = polar
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (x, y)
coordenada_polar = (5, math.pi / 4)

coordenada_cartesiana = polar_a_cartesianas(coordenada_polar)
print(f"Coordenadas cartesianas: {coordenada_cartesiana}")