from solution import SOLUTION
import pyrosim.pyrosim as pyrosim
import constants as c
import copy
import numpy as np

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()
        self.child = []
        self.fitness_results = np.zeros((c.numberOfGeneration, 2))
        # self.weights = self.parent.weights

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for i in range(c.numberOfGeneration):
            self.Evolve_For_One_Generation(i)

        print(self.fitness_results)

    def Evolve_For_One_Generation(self, iterate):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print(iterate)
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent) # deepcopy: copy all date in the object
        # copy of self.parent's weights and its fitness

    def Mutate(self):
        self.child.Mutate()
        self.Create_Brain(self.child)

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
        else:
            self.parent = self.parent

    def Print(self, iterate):
        self.fitness_results[iterate, 0] = self.parent.fitness
        self.fitness_results[iterate, 1] = self.child.fitness
        print(self.fitness_results[iterate])



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

    def Create_Brain(self,who):

        pyrosim.Start_NeuralNetwork("brain.nndf")

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
                                     weight= who.weights[currentRow][currentColumn])

        pyrosim.End()
