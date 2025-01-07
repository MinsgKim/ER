import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
import numpy as np
from math import pi
import os


class MOTOR:
    def __init__(self, robot, jointName, total_time):
        self.robot = robot
        self.jointName = jointName
        self.motorValues = []
        # self.amplitude = c.amplitude
        # self.frequency = c.frequency
        # self.phaseOffset = c.phaseOffset
        self.total_time = total_time
        # self.Prepare_To_Act()


    def Set_Value(self, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot.robotID,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 200)