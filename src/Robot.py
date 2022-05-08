class Robot:
    def __init__(self, pos_x: float, pos_y: float):
        self.rotation = 0
        self.size = 20
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocity = 0