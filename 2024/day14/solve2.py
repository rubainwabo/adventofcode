import sys
import re

input = open(sys.argv[1]).read().strip().split('\n')

class Robot:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel     

    def move(self, size):
        w, l = size
        d_x = self.pos[0] + self.vel[0]
        d_y = self.pos[1] + self.vel[1]
        if d_x < 0:
            new_x = d_x % (-1 * l)
            if new_x < 0:
                new_x += l
        else:
            new_x = d_x % l
        if d_y < 0:
            new_y = d_y % (-1 * w)
            if new_y < 0:
                new_y += w            
        else:
            new_y = d_y % w
        self.pos = (new_x, new_y)

    def move_x_seconds(self, size, x_seconds):
        w, l = size
        d_x = self.pos[0] + x_seconds * self.vel[0]
        d_y = self.pos[1] + x_seconds * self.vel[1]
        if d_x < 0:
            new_x = d_x % (-1 * l)
            if new_x < 0:
                new_x += l
        else:
            new_x = d_x % l
        if d_y < 0:
            new_y = d_y % (-1 * w)
            if new_y < 0:
                new_y += w            
        else:
            new_y = d_y % w
        self.pos = (new_x, new_y)

    def getPosition(self):
        return self.pos

class Main:
    def __init__(self, file):
        self.file = file
        self.height = 103
        self.width = 101
        self.board = []
        self.visu = []
        self.robots = []
        self.load_board()
    
    def load_board(self):
        self.fill_board()
        input = open(self.file).read().strip().split('\n')
        for line in input: 
            n = re.findall(r'-?\d+', line)
            pos = (int(n[0]), int(n[1]))
            vel = (int(n[2]), int(n[3]))
            robot = Robot(pos, vel)
            self.robots.append(robot)
        #self.print_board()
    
    def fill_board(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.visu = [['.' for _ in range(self.width)] for _ in range(self.height)]
    
    def print_board(self):
        for i, line in enumerate(self.board):
            for j, n in enumerate(line):
                if n == 0:
                    self.visu[i][j] = '.'
                else:
                    self.visu[i][j] = str(n)
        for line in self.visu:
            print("".join(line))

    def visualize(self):
        for i in range(7093, 7094):
            self.fill_board()
            for robot in self.robots:
                robot.move_x_seconds((self.height, self.width), i)
                pos = robot.getPosition()
                self.board[pos[1]][pos[0]] += 1
            self.print_board()
    
    def check_board(self):
        for x in range(self.height):
            for y in range(self.width):
                isCandidate = True
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= x + i < self.height and 0 <= y + j < self.width:
                            if self.board[x + i][y + j] == 0:
                                isCandidate = False
                if isCandidate:
                    return True
        return False

    def find_easter_egg(self):
        seconds = 1
        while True:
            self.fill_board()
            for robot in self.robots:
                robot.move((self.height, self.width))
                pos = robot.getPosition()
                self.board[pos[1]][pos[0]] += 1
            if self.check_board():
                print(f"answer found after {seconds} seconds")
                break
            seconds += 1

if __name__ == "__main__":
    file = sys.argv[1]
    _main = Main(file)
    _main.find_easter_egg()
    # Visualizes the beautiful hardcoded chritsmas tree
    _main.visualize()