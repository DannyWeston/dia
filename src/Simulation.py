from time import sleep

from World import World

class SimConfig:
    def __init__(self):
        self.Width = 0
        self.Height = 0
        self.Seed = 0

class Simulation:
    def __init__(self, config: SimConfig):
        # Do something
        self.m_Config = config

        self.m_World = World(self.m_Config.Width, self.m_Config.Height)

        self.finished = False

    def update(self):
        # Update the world
        self.m_World.update()

    def end(self):
        self.finished = True