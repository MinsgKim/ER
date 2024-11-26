import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
x = 0
y = 0
z = 0.5
length = 1
width = 1
height = 1
# pyrosim.Send_Cube(name="Box1" , pos=[x,y,z] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box2" , pos=[0.7*x+x,y,height+z] , size=[length,width,height])
for i in range(8):
    for j in range(8):
        for k in range(8):
            pyrosim.Send_Cube(name="Box", pos=[x+i, y+j, z+k], size=[length*(1-0.1*(k-1)), width*(1-0.1*(k-1)), height*(1-0.1*(k-1))])
pyrosim.End()