import matplotlib.pyplot as plt
import numpy as np


backLegSensorValues = np.load('data/backLegSensorValues.npy')
FrontLegSensorValues = np.load('data/FrontLegSensorValues.npy')
# print(backLegSensorValues)

plt.plot(FrontLegSensorValues)
plt.plot(backLegSensorValues)

plt.legend()

plt.show()