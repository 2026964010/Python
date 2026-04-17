def sqrt_custom(x, g):
    if abs(g*g - x) < 0.0001: return g
    return sqrt_custom(x, (g + x/g) / 2)