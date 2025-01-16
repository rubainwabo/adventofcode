import sys
import re
from collections import defaultdict
from functools import reduce

input = open(sys.argv[1]).read().strip().split('\n')

class Robot:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel     

    def move_100_seconds(self, size):
        w, l = size
        d_x = (self.pos[0] + 100 * self.vel[0]) % l
        d_y = (self.pos[1] + 100 * self.vel[1]) % w           
        self.pos = (d_x, d_y)
    
    def getPosition(self):
        return self.pos

class Main:
    def __init__(self, file):
        self.file = file
        self.height = 103
        self.width = 101
        self.board = []
        self.load_board()
    
    def load_board(self):
        self.fill_board()
        input = open(self.file).read().strip().split('\n')
        for line in input: 
            n = re.findall(r'-?\d+', line)
            pos = (int(n[0]), int(n[1]))
            vel = (int(n[2]), int(n[3]))
            robot = Robot(pos, vel)
            robot.move_100_seconds((self.height, self.width))
            pos = robot.getPosition()
            self.board[pos[1]][pos[0]] += 1 
    
    def fill_board(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def count_robots_in_quadrants(self):
        res = defaultdict(int)
        mid_l = self.height // 2
        mid_w = self.width // 2

        for i, line in enumerate(self.board):
            for j, c in enumerate(line):
                if 0 <= i < mid_l and 0 <= j < mid_w:
                    res['1'] += c
                elif 0 <= i < mid_l and mid_w < j < self.width:
                    res['2'] += c
                elif mid_l < i < self.height and 0 <= j < mid_w:
                    res['3'] += c
                elif mid_l < i < self.height and mid_w < j < self.width:
                    res['4'] += c
        return reduce(lambda cc, x: cc * x, res.values())


if __name__ == "__main__":
    file = sys.argv[1]
    _main = Main(file)
    print(_main.count_robots_in_quadrants())