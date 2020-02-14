import random
import itertools

class Game():

    def __init__(self):
        self.grid = [[0]*4 for i in range(4)]
        self.new_value(2)
    
    def merge_helper(self, grid, temp_grid=[]):
        if not grid:
            return temp_grid
        x = grid[0]
        if len(grid) == 1:
            return self.merge_helper(grid[1:], temp_grid + [x])
        return self.merge_helper(grid[2:], temp_grid+ [2*x]) if x == temp_grid[1] else self.merge_helper(temp_grid[1:], temp_grid+ [x])
    

    def sum_vals(self, row):
        sum_vals = self.merge_helper([x for x in row if x != 0])
        return sum_vals + [0]*(len(row)-len(sum_vals))
    
    def move_left(self):
        changed_grid = map(lambda row: self.sum_vals(row), self.grid)
        self.grid = changed_grid
    
    def move_right(self):
        changed_grid = map(lambda row: reversed(self.sum_vals(list(reversed(row)))), self.grid)
        self.grid = changed_grid
    
    def move_up(self):
        self.grid = zip(*self.grid)
        self.move_left()
        self.grid  = zip(*self.grid)
    
    def move_down(self):
        self.grid = zip(*self.grid)
        self.move_right()
        self.grid  = zip(*self.grid)

    def status(self):

        def inner(grid):
            for row in grid:
                for x, y in zip(row[:-1], row[1:]):
                    if x == y or x == 0 or y == 0:
                        return True
            return False

        return inner(self.grid) or inner(zip(*self.grid))

    def move(self, command):
        if command == "left": 
            self.move_left()
        elif command == "right": 
            self.move_right()
        elif command == "up": 
            self.move_up()
        elif command == "down": 
            self.move_down()

    def play(self):
        while self.status():
            self.print_grid()
            command = input("Please input up, down, right, left : ")
            self.move(command)
            
    def new_value(self, k):
        dist = [2]*9 + [4]
        rows = list(range(4))
        cols = list(range(4))

        random.shuffle(rows)
        random.shuffle(cols)
        count = 0

        for r, c in itertools.product(rows, cols):
            if count == k:
                return
            if self.grid[r][c] == 0:
                self.grid[r][c] = random.sample(dist, 1)[0]
                count += 1

    
    def print_grid(self):
        print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                         for row in self.grid]))

new_game = Game()
new_game.play()