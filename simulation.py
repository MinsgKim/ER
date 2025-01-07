from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

class SIMULATION:
    def __init__(self, DirectOrGUI, solutionID):     # constructor, 생성자
        self.DirectOrGUI = DirectOrGUI
        if self.DirectOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        self.setAdditionalSearchPath = p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.setGravity = p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        self.Prepare_To_Simulate = pyrosim.Prepare_To_Simulate(self.robot.robotID)
        self.total_time = c.numTotalTime
        self.Prepare_To_Sense = self.robot.Prepare_To_Sense()
        self.Prepare_To_Act = self.robot.Prepare_To_Act(self.total_time)


    def run(self):

        if self.DirectOrGUI == "GUI":
            for t in range(self.total_time):
                p.stepSimulation()
                self.robot.Sense(self.total_time, t)
                self.robot.Think()
                self.robot.Act()
                time.sleep(c.numTimeSteps)
        else:
            for t in range(self.total_time):
                p.stepSimulation()
                self.robot.Sense(self.total_time, t)
                self.robot.Think()
                self.robot.Act()

    def Get_Fitness(self):
        self.robot.Get_Fitness()


    def __del__(self):      # destructor, 소멸자

        p.disconnect()