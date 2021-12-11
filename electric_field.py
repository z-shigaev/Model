import numpy as np
import math

def get_field(coords, coeff):
    mod = math.pow(coords[0], 2) + math.pow(coords[1], 2)
    r = math.pow(mod, 0.5)
    ex = (coeff/math.pow(r, 2))*(coords[0]/mod)
    ey = (coeff/math.pow(r, 2))*(coords[1]/mod)
    return ex, ey, 0
