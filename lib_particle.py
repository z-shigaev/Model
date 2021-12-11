import math

class Particle:
    def __init__(self, weight, charge, coords, velocity):
        self.weight = weight
        self.charge = charge
        self.coords = coords
        self.velocity = velocity

    def change_moving(self, power, time):
        x = (power[0]*math.pow(time, 2))/(2*self.weight)+velocity[0]*time+coords[0]
        y = (power[1]*math.pow(time, 2))/(2*self.weight)+velocity[1]*time+coords[1]
        z = (power[2]*math.pow(time, 2))/(2*self.weight)+velocity[2]*time+coords[2]
        vx = (power[0] * time) / self.weight + self.velocity[0]
        vy = (power[1] * time) / self.weight + self.velocity[1]
        vz = (power[2] * time)  /self.weight + self.velocity[2]
        self.coords = [x, y, z]
        self.velocity = [vx, vy, vz]
        return x, y, z




if __name__ == "__main__":
    coords = [1, 1, 1]
    velocity = [0, 0, 0]
    particle = Particle(1, 1, coords, velocity)



