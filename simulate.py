from simulation import SIMULATION
import sys

DirectOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(DirectOrGUI, solutionID)
simulation.run()
simulation.Get_Fitness()