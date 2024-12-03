from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:
    def __init__(self):     # constructor, 생성자

        self.physicsClient = p.connect(p.GUI)
        self.setAdditionalSearchPath = p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.setGravity = p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        self.Prepare_To_Simulate = pyrosim.Prepare_To_Simulate(self.robot.robotID)
        self.total_time = 200
        self.Prepare_To_Sense = self.robot.Prepare_To_Sense()
        self.Prepare_To_Act = self.robot.Prepare_To_Act(self.total_time)


    def run(self):

        for t in range(self.total_time):
            p.stepSimulation()
            self.robot.Sense(self.total_time, t)
            self.robot.Act(t)
            for linkName, sensor in self.robot.sensors.items():
                print(f"Step {t}, Link: {linkName}, Sensor Value: {sensor.values[t]}")
            time.sleep(1/60)
    #     print(backLegSensorValues[i])
    #         print(t)

    def __del__(self):      # destructor, 소멸자

        p.disconnect()
        for linkName in pyrosim.linkNamesToIndices:
            self.robot.sensors[linkName].Save_Values()

        for jointName in pyrosim.jointNamesToIndices:
            self.robot.motors[jointName].Save_Values()