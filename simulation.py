import pybullet_data
import pybullet as p
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
import time
p.setGravity(0,0,-9.8)
planeID = p.loadURDF("plane.urdf")
planeID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()