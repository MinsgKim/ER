import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import os


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotID)
print("Available joints:", pyrosim.jointNamesToIndices.keys())
backLegSensorValues = np.zeros(500)
FrontLegSensorValues = np.zeros(500)
for i in range(500):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    FrontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = b'BackLeg_Torso',
        controlMode = p.POSITION_CONTROL,
        targetPosition = 0.0,
        maxForce = 500)
    time.sleep(1/60)
    print(backLegSensorValues[i])
    print(i)

p.disconnect()

os.makedirs('data', exist_ok=True)
file_path1 = os.path.join('data', 'backLegSensorValues.npy')
file_path2 = os.path.join('data', 'FrontLegSensorValues.npy')
np.save(file_path1,backLegSensorValues)
np.save(file_path2,FrontLegSensorValues)