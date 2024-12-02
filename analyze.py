import matplotlib.pyplot as plt
import numpy as np


backLegSensorValues = np.load('data/backLegSensorValues.npy')
FrontLegSensorValues = np.load('data/FrontLegSensorValues.npy')
targetAngles_back = np.load('data/targetAngles_back.npy')
targetAngles_front = np.load('data/targetAngles_front.npy')
# print(backLegSensorValues)

plt.plot(targetAngles_front)
plt.plot(targetAngles_back)
# plt.plot(FrontLegSensorValues)
# plt.plot(backLegSensorValues)

plt.legend()

plt.show()