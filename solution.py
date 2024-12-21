import numpy as np
import os
import random

class SOLUTION:

    def __init__(self):
        self.weights = 2 * np.random.rand(3, 2) - 1 # create an m x n matrix with random numbers from -1 to 1
        self.fitness = []

    def Evaluate(self, DirectOrGUI):
        os.system(f"python simulate.py {DirectOrGUI}")
        f = open("fitness.txt")
        val = float(f.read())
        self.fitness = val
        f.close()

    def Mutate(self):
        randomRow = random.randint(0, 2) # choose a random value from [0, 2] inclusive
        randomColumn = random.randint(0,1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

