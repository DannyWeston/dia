from random import randint, seed

class MazeCell:
    def __init__(self):
        self.Left = False
        self.Right = False
        self.Top = False
        self.Bottom = False
        self.Visited = False

class Maze:
    def __init__(self, width: int, height: int, start_pos: tuple[int, int] = (0, 0), gen_seed: int = None):
        self.width = width
        self.height = height
        self.start_pos = start_pos   

        # Generate random seed if one isn't present, and initialise generator
        if gen_seed is None: self.m_Seed = randint(0, 100000000)
        else: self.m_Seed = gen_seed

        seed(self.m_Seed)

        self.data = [MazeCell() for i in range(self.width * self.height)]
        
        self.data[0].Top = True
        self.data[0].Left = True
        self.data[0].Bottom = True
        self.data[0].Right = True
        self.data[0].Visited = True

        # Make a stack with the start position inside of it
        stack: list[int] = [self.pos_from_xy(self.start_pos)]

        chosen = None

        while (0 < len(stack)):
            current = stack[-1]

            # Get unvisited neighbours
            p = self.get_neighbour_positions(current)
            neighbours = [n for n in p if not self.data[n].Visited]

            if (len(neighbours) == 0):
                stack.pop()
                continue
            
            chosen = neighbours[randint(0, len(neighbours) - 1)]

            self.data[chosen].Top = True
            self.data[chosen].Bottom = True
            self.data[chosen].Left = True
            self.data[chosen].Right = True
            self.data[chosen].Visited = True

            if chosen == current - self.width:
                self.data[current].Top = False
                self.data[chosen].Bottom = False

            elif chosen == current + self.width:
                self.data[chosen].Top = False
                self.data[current].Bottom = False
            
            elif chosen == current - 1:
                self.data[current].Left = False
                self.data[chosen].Right = False

            else:
                self.data[chosen].Left = False
                self.data[current].Right = False

            stack.append(chosen)

    def get_neighbour_positions(self, pos):
        neighbours = []

        if 0 <= pos - self.width: neighbours.append(pos - self.width)
        if 0 != pos % self.width: neighbours.append(pos - 1)
        if pos + self.width < self.width * self.height: neighbours.append(pos + self.width)
        if 0 != (pos + 1) % self.width: neighbours.append(pos + 1)

        return neighbours

    def to_map(self):
        return MazeMap(self)

    def pos_from_xy(self, pos):
        return pos[1] * self.width + pos[0]

class MazeMap:
    def __init__(self, maze: Maze):
        self.width = maze.width * 3
        self.height = maze.height * 3

        self.data: list[int] = [0 for i in range(self.width * self.height * 9)]

        j = 0
        for i in range(0, maze.width * maze.height):
            pos = i * 3

            if i != 0 and i % maze.width == 0: j += 2

            self.data[pos + j * self.width] = 1 if maze.data[i].Left or maze.data[i].Top else 0
            self.data[pos + j * self.width + 1] = 1 if maze.data[i].Top else 0
            self.data[pos + j * self.width + 2] = 1 if maze.data[i].Right or maze.data[i].Top else 0

            self.data[pos + (j + 1) * self.width] = 1 if maze.data[i].Left else 0
            # map[pos + (j + 1) * self.width + 1] = 0; # Skip setting center as by default empty
            self.data[pos + (j + 1) * self.width + 2] = 1 if maze.data[i].Right else 0

            self.data[pos + (j + 2) * self.width] = 1 if maze.data[i].Left or maze.data[i].Bottom else 0
            self.data[pos + (j + 2) * self.width + 1] = 1 if maze.data[i].Bottom else 0
            self.data[pos + (j + 2) * self.width + 2] = 1 if maze.data[i].Right or maze.data[i].Bottom else 0

    def print_data(self):
        for i in range(0, self.width * self.height):
            if i != 0 and i % self.width == 0: print()

            print(self.data[i], end = '')