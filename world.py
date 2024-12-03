import pybullet as p

class WORLD:
    def __init__(self):
        self.planeID = p.loadURDF("plane.urdf")
        self.loadSDF = p.loadSDF("world.sdf")