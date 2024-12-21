from simulation import SIMULATION
import sys

DirectOrGUI = sys.argv[1]

simulation = SIMULATION(DirectOrGUI)
simulation.run()
simulation.Get_Fitness()