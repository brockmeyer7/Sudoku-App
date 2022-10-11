import csv
from random import choice
from readchar import readkey, key


class Puzzle:
    def __init__(self, file):
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

            self.original = tuple(grid)
            self.grid = grid
            self.solution = tuple(solution)
            self.grid_idx = 0

    def render_puzzle(self):

        def subrow(start, end, row_start):
            string = ""
            for i in range(start, end):
                if row_start + i == self.grid_idx and 0 in self.grid:
                    string += "| \u25AE "
                elif self.grid[row_start + i] == 0:
                    string += "|   "
                else:
                    string += "| " + str(self.grid[row_start + i]) + " "
            return string

        def print_row(row):
            row_start = row * 9
            row_string = subrow(0, 3, row_start)
            row_string += "|"
            row_string += subrow(3, 6, row_start)
            row_string += "|"
            row_string += subrow(6, 9, row_start)
            row_string += "|"
            print(row_string)

        def print_line():
            print(" --- --- ---  --- --- ---  --- --- --- ")

        print("\n" * 50)
        print_line()
        for i in range(3):
            print_row(i)
            print_line()
        print_line()
        for i in range(3, 6):
            print_row(i)
            print_line()
        for i in range(6, 9):
            print_line()
            print_row(i)
        print_line()
        print("\n")

    def solve_puzzle(self):
        while 0 in self.grid:
            self.grid_idx = 0
            while self.grid[self.grid_idx] != 0:
                self.grid_idx += 1

            self.render_puzzle()
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

        self.render_puzzle()
        return True

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

    def navigate_grid(self):

        print('Use arrow keys to navigate, press enter to fill highlighted cell, or press "Q" to exit to main menu:')

        def move_right():
            if self.grid_idx % 9 != 8:
                self.grid_idx += 1

        def move_left():
            if self.grid_idx % 9 != 0:
                self.grid_idx -= 1

        def move_up():
            if self.grid_idx // 9 != 0:
                self.grid_idx -= 9

        def move_down():
            if self.grid_idx // 9 != 8:
                self.grid_idx += 9

        while True:
            k = readkey()
            if k == key.RIGHT:
                move_right()
                while self.is_original_cell():
                    move_right()
                    if self.grid_idx % 9 == 8:
                        while self.is_original_cell():
                            move_left()
                self.render_puzzle()
                print(
                    'Use arrow keys to navigate, press enter to fill highlighted cell, or press "Q" to exit to main menu:')
            elif k == key.LEFT:
                move_left()
                while self.is_original_cell():
                    move_left()
                    if self.grid_idx % 9 == 0:
                        while self.is_original_cell():
                            move_right()
                self.render_puzzle()
                print(
                    'Use arrow keys to navigate, press enter to fill highlighted cell, or press "Q" to exit to main menu:')
            elif k == key.UP:
                move_up()
                while self.is_original_cell():
                    move_up()
                    if self.grid_idx // 9 == 0:
                        while self.is_original_cell():
                            move_down()
                self.render_puzzle()
                print(
                    'Use arrow keys to navigate, press enter to fill highlighted cell, or press "Q" to exit to main menu:')
            elif k == key.DOWN:
                move_down()
                while self.is_original_cell():
                    move_down()
                    if self.grid_idx // 9 == 8:
                        while self.is_original_cell():
                            move_up()
                self.render_puzzle()
                print(
                    'Use arrow keys to navigate, press enter to fill highlighted cell, or press "Q" to exit to main menu:')
            elif k == key.ENTER:
                if self.original[self.grid_idx] != 0:
                    print(
                        'Use arrow keys to navigate, press enter to fill highlighted cell, or press "Q" to exit to main menu:')
                else:
                    self.render_puzzle()
                    return True
            elif k == "q":
                return False

    def is_original_cell(self):
        if self.original[self.grid_idx] != 0:
            return True
        return False
