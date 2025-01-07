import os
import constants as c
from parallelhillclimber import PARALLEL_HILL_CLIMBER

for i in range(2 + 2 * c.populationSize):
    os.system(f"del brain{i}.nndf")
    os.system(f"del fitness{i}.txt")
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()

# print(phc.parents[0].fitness)
# print(phc.parents[1].fitness)
