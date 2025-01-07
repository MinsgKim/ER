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

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
        else:
            self.parent = self.parent

    def Print(self, iterate):
        self.fitness_results[iterate, 0] = self.parent.fitness
        self.fitness_results[iterate, 1] = self.child.fitness
        print(self.fitness_results[iterate])

    def Show_Best(self):
        self.parent.Evaluate("DIRECT")