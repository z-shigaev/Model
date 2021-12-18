import numpy as np
import math

def get_field(coords, coeff):
    mod = math.pow(coords[0], 2) + math.pow(coords[1], 2)
    r = math.pow(mod, 0.5)
    ex = (coeff/r)*(coords[0]/r)
    ey = (coeff/r)*(coords[1]/r)
    return ex, ey, 0
