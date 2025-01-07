import numpy as np
import os
import random
import pyrosim.pyrosim as pyrosim
import time

class SOLUTION:

    def __init__(self, myID):
        self.weights = 2 * np.random.rand(3, 2) - 1 # create an m x n matrix with random numbers from -1 to 1
        self.fitness = []
        self.myID = myID

    def Set_ID(self, newID):
        self.myID = newID

    def Start_Simulation(self, DirectOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # 하나 실행하는동안 동시에 다른 것도 실행
        os.system(f"start /B python simulate.py {DirectOrGUI} {self.myID}")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)
        else:
            pass

        f = open(f"fitness{self.myID}.txt")
        val = float(f.read())
        self.fitness = val
        f.close()
        os.system(f"del fitness{self.myID}.txt")

    def Mutate(self):
        randomRow = random.randint(0, 2) # choose a random value from [0, 2] inclusive
        randomColumn = random.randint(0,1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1


    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")

        pyrosim.End()

    def Create_Body(self):

        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0.0, 0, 1.5],
                          size=[1, 1, 1])
        pyrosim.Send_Joint(name= "Torso_BackLeg", parent="Torso",
                           child="BackLeg", type="revolute",
                           position=[-0.5, 0, 1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5],
                          size=[1, 1, 1])
        pyrosim.Send_Joint(name= "Torso_FrontLeg", parent="Torso",
                           child="FrontLeg", type="revolute",
                           position=[0.5, 0, 1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5],
                          size=[1, 1, 1])

        pyrosim.End()

    def Create_Brain(self):

        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # sensor neurons
        pyrosim.Send_Sensor_Neuron(name= 0, linkName= "Torso")
        pyrosim.Send_Sensor_Neuron(name= 1, linkName= "BackLeg")
        pyrosim.Send_Sensor_Neuron(name= 2, linkName= "FrontLeg")

        # motor neurons
        pyrosim.Send_Motor_Neuron(name= 3, jointName= "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name= 4, jointName= "Torso_FrontLeg")

        # two nested for loops
        for currentRow in [0, 1, 2]:
            for currentColumn in [0, 1]:
                pyrosim.Send_Synapse(sourceNeuronName= currentRow,
                                     targetNeuronName= currentColumn + 3,
                                     weight= self.weights[currentRow][currentColumn])

        pyrosim.End()

