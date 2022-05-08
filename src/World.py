from Maze import Maze

from random import randint

from Robot import Robot

class World:
    def __init__(self, width: int, height: int):
        self.maze = Maze(width, height)
        self.map = self.maze.to_map()

        self.width = self.map.width 
        self.height = self.map.height

        while True:
            robot_pos = randint(0, len(self.map.data) - 1)    

            if self.map.data[robot_pos] == 0: break

        robot_x = robot_pos % self.width
        robot_y = robot_pos / self.height

        self.robot = Robot(robot_x, robot_y)

    def update(self):
        # Do something to update the world
        pass