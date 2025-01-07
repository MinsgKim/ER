from solution import SOLUTION
import pyrosim.pyrosim as pyrosim
import constants as c
import copy
import numpy as np

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i]=SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        self.children = {}
        self.parents_fitness_results = np.zeros((c.numberOfGeneration, c.populationSize))
        self.children_fitness_results = np.zeros((c.numberOfGeneration, c.populationSize))
        self.best_parent = {}

    def Evolve(self):

        self.Evaluate(self.parents)

        for i in range(c.numberOfGeneration):
            self.Evolve_For_One_Generation(i)

        self.Show_Best("GUI")

    def Evolve_For_One_Generation(self, iterate):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print(iterate)
        self.Select()

    def Spawn(self):
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i]) # deepcopy: copy all date in the object
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children.keys():
            self.children[i].Mutate()

    def Print(self, iterate):
        i = 0
        for key in self.parents:
            self.parents_fitness_results[iterate, i] = self.parents[key].fitness
            self.children_fitness_results[iterate, i] = self.children[key].fitness
            i += 1
        print(self.parents_fitness_results[iterate])
        print(self.children_fitness_results[iterate])

    def Select(self):

        for key in self.parents.keys():
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]
            else:
                self.parents[key] = self.parents[key]

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Show_Best(self, GUI):
        for i in range(c.populationSize - 1):
            if self.parents[i].fitness < self.parents[i + 1].fitness:
                self.best_parent = self.parents[i]
            else:
                self.best_parent = self.parents[i + 1]

        self.best_parent.Start_Simulation(GUI)
        self.best_parent.Wait_For_Simulation_To_End()

