import matplotlib.pyplot as plt
import numpy as np


backLegSensorValues = np.load('data/BackLegSV.npy')
FrontLegSensorValues = np.load('data/FrontLegSV.npy')
targetAngles_back = np.load('data/BackLeg_Torso.npy')
targetAngles_front = np.load('data/Torso_FrontLeg.npy')
# print(backLegSensorValues)

errors = targetAngles_front-targetAngles_back
print(errors)

plt.plot(targetAngles_front)
plt.plot(targetAngles_back)
# plt.plot(FrontLegSensorValues)
# plt.plot(backLegSensorValues)


plt.show()