import os
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.Create_World()
hc.Create_Body()
hc.Create_Brain(hc.parent)

hc.Evolve()

os.system("python simulate.py GUI")