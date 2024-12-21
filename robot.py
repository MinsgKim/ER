from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotID = p.loadURDF("body.urdf")  # a body ID, the unique ID of a body in the simulation.
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            # print(linkName)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, total_time, t):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName].Get_Value(total_time, t)

    def Prepare_To_Act(self, total_time):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(self, jointName, total_time)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                # jointName = jointName.decode("utf-8")
                self.motors[jointName].Set_Value(desiredAngle)
                # print(f"{neuronName}\t{jointName}\t{desiredAngle}\n")

        # for jointName in pyrosim.jointNamesToIndices:
        #     self.motors[jointName].Set_Value(t)


    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID, 0)
        # it is a tuple with a bunch of tuples inside it.
        # the first tuple contains the position of the link
        xCoordinateOfLinkZero = stateOfLinkZero[0][0]
        f = open("fitness.txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        # print(xCoordinateOfLinkZero)
        exit()