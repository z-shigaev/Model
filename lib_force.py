import numpy as np


def force_electric(electric_field, charge):
    fx = charge*electric_field[0]
    fy = charge*electric_field[1]
    fz = charge*electric_field[2]
    return np.array([fx, fy, fz])


def force_magnet(magnet_field, velocity, charge):
    fx = (velocity[1]*magnet_field[2]-velocity[2]*magnet_field[1])
    fy = (velocity[2]*magnet_field[0]-velocity[0]*magnet_field[2])
    fz = (velocity[0]*magnet_field[1]-velocity[1]*magnet_field[0])
    return fx, fy, fz
    # return charge*np.cross(velocity, magnet_field)


def force_gravity(AoFF, weight):
    # AoFF - Acceleration of Free Fall
    fx = weight*AoFF[0]
    fy = weight*AoFF[1]
    # print('force')
    # print(fx, fy)
    fz = weight*AoFF[2]
    return np.array([fx, fy, fz])

