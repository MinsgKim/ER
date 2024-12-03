import pyrosim.pyrosim as pyrosim
import numpy as np
import os

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = []


    def Get_Value(self, total_time, t):
        self.values = np.zeros(total_time)
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        os.makedirs('data', exist_ok=True)
        file_path = os.path.join('data', f'{self.linkName}SV.npy')
        np.save(file_path,self.values)
