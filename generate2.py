import pyrosim.pyrosim as pyrosim


def create_world():
    pyrosim.Start_SDF("world.sdf")

    pyrosim.End()


def create_robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="BackLeg", pos=[0, 0, 0.5],
                      size=[1, 1, 1])
    pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg",
                       child="Torso", type="revolute",
                       position=[0.5, 0, 1])
    pyrosim.Send_Cube(name="Torso", pos=[0.5, 0, 0.5],
                      size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                       child="FrontLeg", type="revolute",
                       position=[1, 0, 0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5],
                      size=[1, 1, 1])

    pyrosim.End()


create_world()
create_robot()
