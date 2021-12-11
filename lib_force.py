import numpy as np


def force_electric(electric_field, charge):
    fx = charge*electric_field[0]
    fy = charge*electric_field[1]
    fz = charge*electric_field[2]
    return np.array([fx, fy, fz])


def force_magnet(magnet_field, velocity, charge):
    # print(charge*np.cross(velocity, magnet_field))
    return charge*np.cross(velocity, magnet_field)


def force_gravity(AoFF, weight):
    # AoFF - Acceleration of Free Fall
    fx = weight*AoFF[0]
    fy = weight*AoFF[1]
    fz = weight*AoFF[2]
    return np.array([fx, fy, fz])

