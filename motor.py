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
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.phaseOffset = c.phaseOffset
        self.total_time = total_time
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.motorValues = np.zeros(self.total_time)
        for k in range(self.total_time):
            t = np.linspace(0, 2*pi, self.total_time)
            self.motorValues[k] = (self.amplitude * np.sin(self.frequency * t[k] + self.phaseOffset))

    def Set_Value(self,t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot.robotID,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = 30)

    def Save_Values(self):
        os.makedirs('data', exist_ok=True)
        file_path = os.path.join('data', f'{self.jointName.decode("utf-8")}.npy')
        np.save(file_path,self.motorValues)