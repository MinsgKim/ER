from simulation import SIMULATION

# from symbol import pass_stmt
#
# import pybullet_data
# import pybullet as p
# import constants as c
# import pyrosim.pyrosim as pyrosim
# import time
# import numpy as np
# import os
# from math import pi
# import random
#
#

# backLegSensorValues = np.zeros(500)
# FrontLegSensorValues = np.zeros(500)
# targetAngles_back = np.zeros(500)
# targetAngles_front = np.zeros(500)
# for k in range(500):
#     t = 2*pi*k/500
#     targetAngles_back[k] = (c.amplitude_back *
#                             np.sin(c.frequency_back * t + c.phaseOffset_back))
#     targetAngles_front[k] = (c.amplitude_front *
#                              np.sin(c.frequency_front * t + c.phaseOffset_front))
#
# file_path3 = os.path.join('data','targetAngles_back.npy')
# np.save(file_path3,targetAngles_back)
# file_path4 = os.path.join('data','targetAngles_front.npy')
# np.save(file_path4,targetAngles_front)
#
# for i in range(500):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     FrontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotID,
#         jointName = b'BackLeg_Torso',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAngles_back[i],
#         maxForce = 30)
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotID,
#         jointName = b'Torso_FrontLeg',
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = -targetAngles_front[i],
#         maxForce = 30)
#     time.sleep(1/60)
#     print(backLegSensorValues[i])
#     print(i)
#
# p.disconnect()
#
# os.makedirs('data', exist_ok=True)
# file_path1 = os.path.join('data', 'backLegSensorValues.npy')
# file_path2 = os.path.join('data', 'FrontLegSensorValues.npy')
# np.save(file_path1,backLegSensorValues)
# np.save(file_path2,FrontLegSensorValues)

simulation = SIMULATION()
simulation.run()