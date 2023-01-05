from puzzle import Puzzle
from random import choice
import csv


class UserSolve(Puzzle):

    def __init__(self, file):
        super().__init__()
        self.grid, self.solution = self.load_puzzle(file)
        self.original = tuple(self.grid)

    def load_puzzle(self, file):
        with open(file, 'r') as file:
            puzzle_pool = list(csv.reader(file))
            puzzle_pool.pop(0)
            puzzle_data = choice(puzzle_pool)
            grid = []
            solution = []
            for item in puzzle_data[1]:
                if item == ".":
                    grid.append(0)
                else:
                    grid.append(int(item))
            for item in puzzle_data[2]:
                solution.append(int(item))

        return grid, solution

    def check_solution(self):
        counter = 0
        for i in range(len(self.grid)):
            if self.grid[i] != self.solution[i]:
                counter += 1

        if counter == 0:
            print("Congratulations! Your solution is correct!")
            return True
        else:
            print(f"Oops, you have {counter} incorrect cells")
            print("\n1) Clear errors and continue solving\n2) Quit")
            user_input = input("Selection: ")
            if user_input == "1":
                for i in range(len(self.grid)):
                    if self.grid[i] != self.solution[i]:
                        self.grid[i] = 0
                return False
            elif user_input == "2":
                return True

    def solve_puzzle(self):
        while 0 in self.grid:
            self.grid_idx = 0
            while self.grid[self.grid_idx] != 0:
                self.grid_idx += 1

            self.show_puzzle()
            if self.navigate_grid():
                while True:
                    value = input(
                        "Enter value from 1 - 9 or enter 0 to clear cell:\n")
                    if len(value) == 1 and value in "0123456789":
                        self.grid[self.grid_idx] = int(value)
                        break
                    else:
                        print("Invalid value, please enter number from 1 to 9\n")
            else:
                return False

        self.show_puzzle()
        return True
