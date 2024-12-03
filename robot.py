from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotID = p.loadURDF("body.urdf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, total_time, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(total_time, t)

    def Prepare_To_Act(self, total_time):
        for jointName in pyrosim.jointNamesToIndices:
            # print(jointName)
            self.motors[jointName] = MOTOR(self, jointName, total_time)

    def Act(self, t):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName].Set_Value(t)