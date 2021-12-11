import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, weight, charge, coords, velocity):
        self.weight = weight
        self.charge = charge
        self.coords = coords
        self.velocity = velocity

    def change_moving(self, force, time):
        x = (force[0]*math.pow(time, 2))/(2*self.weight)+self.velocity[0]*time+self.coords[0]
        y = (force[1]*math.pow(time, 2))/(2*self.weight)+self.velocity[1]*time+self.coords[1]
        z = (force[2]*math.pow(time, 2))/(2*self.weight)+self.velocity[2]*time+self.coords[2]
        vx = (force[0] * time) / self.weight + self.velocity[0]
        vy = (force[1] * time) / self.weight + self.velocity[1]
        vz = (force[2] * time) / self.weight + self.velocity[2]
        self.coords = [x, y, z]
        self.velocity = [vx, vy, vz]
        return x, y, z

    def get_status(self):
        coords = self.coords
        vel = self.velocity
        print("Coords: {0}".format(coords))
        print("Velocity: {0}".format(vel))





if __name__ == "__main__":
    coords = [0, 0, 0]
    velocity = [200, 100, 0]
    particle = Particle(0.1, 0, coords, velocity)
    track_x = []
    track_y = []
    force = [0, 10, 0]
    time = 0.1
    track_x.append(coords[0])
    track_y.append(coords[1])
    for i in range(0, 20):
        x, y, z = particle.change_moving(force, time)
        track_x.append(x)
        track_y.append(y)
        # particle.get_status()
    plt.plot(track_x, track_y)
    plt.show()




