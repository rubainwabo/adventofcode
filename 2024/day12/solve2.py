import sys
from collections import defaultdict

class Checked_point:
    def __init__(self, pos):
        self.pos = pos
        #left, right, top, bot
        self.directions = [-2, -2, -2, -2]

    def set_direction(self, index, value):
        self.directions[index] = value
    def get_direction(self, index):
        return self.directions[index]
    def top_point(self):
        return (self.pos[0] - 1, self.pos[1])
    def left_point(self):
        return (self.pos[0], self.pos[1] - 1)  


class Region:
    def __init__(self, file):
        self.file = file
        self.board = []
        self.regions = defaultdict(set)
        self.visited = set()
        self.sides = defaultdict(int)
        self.leni = 0
        self.lenj = 0
        self.load_board()

    def load_board(self):
        input = open(self.file).read().strip().split('\n')
        self.board = [list(line) for line in input]
        self.leni, self.lenj = len(input), len(input[0])
    
    def find_region(self, car, car_saved, pos):
        if self.board[pos[0]][pos[1]] != car:
            return
        self.visited.add(pos)
        self.regions[car_saved].add(pos)
        i, j = pos
        self.board[i][j] = car_saved
        choices = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for ch in choices:
            if 0 <= ch[0] < self.leni and 0 <= ch[1] < self.lenj and self.board[ch[0]][ch[1]] == car and ch not in self.visited:
                self.find_region(car, car_saved, ch)

    def sort_regions(self):
        sorted_regions = {}
        for key, points in self.regions.items():
            sorted_points = sorted(points)
            sorted_regions[key] = sorted_points
        return sorted_regions

    def determine_regions(self):
        for i in range(self.leni):
            for j in range(self.lenj):
                car, car_saved = self.board[i][j], self.board[i][j]
                if (i, j) not in self.visited:
                    while car_saved in self.regions:
                        car_saved += car
                    self.find_region(car, car_saved, (i, j))
        self.regions = self.sort_regions()
        return self.sort_regions()
    
    def contains(self, checked_point, checked_points):
        for p in checked_points:
            if p.pos[0] == checked_point[0] and p.pos[1] == checked_point[1]:
                return p
        return None


    def pretty_print(self, check_points):
        for p in check_points:
            print(f"{p.pos} directions {p.directions}")

    # We check left or top since we read from left to right, top to bottom
    def check_perpendicular_direction(self, index, checked_point, checked_points):
        # check top and bottom
        if index <= 1:
            top_point = self.contains(checked_point.top_point(), checked_points)
            if top_point == None:
                return 1
            else:
                if top_point.get_direction(index) == 1 or top_point.get_direction(index) == -1:
                    return -1
                return 1
        else :
            left_point = self.contains(checked_point.left_point(), checked_points)
            if left_point == None:
                return 1
            else:
                if left_point.get_direction(index) == 1 or left_point.get_direction(index) == -1:
                    return -1
                return 1

    
    def calculate_sides(self):
        for r in self.regions:
            checked_points = []
            for p in self.regions[r]:
                i, j = p
                # left, right, top, bot
                choices = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]
                for c in choices:
                    index = choices.index(c)
                    point = self.contains(p, checked_points)
                    if point is None:
                        point = Checked_point(p)
                    #We found nothing in that direction
                    if c not in self.regions[r]:
                        value = self.check_perpendicular_direction(index, point, checked_points)
                        if value == 1:
                            self.sides[r] += 1
                        point.set_direction(index, value)
                    else:
                        point.set_direction(index, 0)
                    checked_points.append(point)
            #self.pretty_print(checked_points)
        return self.sides



if __name__ == "__main__":
    file = sys.argv[1]
    region_finder = Region(file)
    regions = region_finder.determine_regions()  
    sides = region_finder.calculate_sides()
    res = 0
    for r in regions:
        res += sides[r] * len(regions[r])
    print(res)
