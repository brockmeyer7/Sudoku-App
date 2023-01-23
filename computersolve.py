from puzzle import Puzzle
from random import choice
from readchar import readkey, key


class ComputerSolve(Puzzle):

    def __init__(self):
        super().__init__()

    def fill_puzzle(self):
        while True:
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

            self.grid_idx += 1

            self.show_puzzle()
            print(
                'Press "d" if puzzle is filled, or press any other key to continue filling puzzle')
            k = readkey()
            if k == "d":
                self.grid_idx = 0
                break

    def solve(self):
        # Check whether first cell is an original cell given in the puzzle and increment forward until it is an empty cell
        if self.grid_idx == 0:
            while self.original[self.grid_idx] != 0:
                self.grid_idx += 1

        # Check if all cells have been filled (beyond bounds of puzzle grid)
        if self.grid_idx == 81:
            return 1

        # Get available nums that can go in cell being filled
        safe_nums = self.get_safe_nums()

        # Return if no valid numbers can go in cell and decrement grid_idx
        if len(safe_nums) == 0:
            self.move_backward()
            return -1

        else:
            for num in safe_nums:
                self.grid[self.grid_idx] = num
                self.move_forward()

                if self.solve() in [1, 2]:
                    return 2
            self.grid[self.grid_idx] = 0
            self.move_backward()
            if self.grid_idx < 0:
                print("no solution found")

    def get_safe_nums(self):
        row_start = self.grid_idx // 9 * 9
        column_start = self.grid_idx % 9
        box_start = (self.grid_idx // 9 // 3 * 27) + \
            (self.grid_idx % 9 // 3 * 3)
        box = []
        box.extend(self.grid[box_start: box_start + 3])
        box.extend(self.grid[box_start + 9: box_start + 12])
        box.extend(self.grid[box_start + 18: box_start + 21])
        row_nums = {i for i in range(
            1, 10) if i not in self.grid[row_start: row_start + 9]}
        column_nums = {i for i in range(
            1, 10) if i not in self.grid[column_start:: 9]}
        box_nums = {i for i in range(1, 10) if i not in box}
        safe_nums = list(set.intersection(row_nums, column_nums, box_nums))
        safe_nums.sort()
        # print(f"safe_nums = {safe_nums}, grid_idx = {self.grid_idx}")
        return safe_nums

    def move_forward(self):
        self.grid_idx += 1
        if self.grid_idx < 80:
            while self.original[self.grid_idx] != 0:
                self.grid_idx += 1
                if self.grid_idx == 80 and self.original[self.grid_idx] != 0:
                    self.grid_idx += 1
                    break
                elif self.grid_idx == 80:
                    break

    def move_backward(self):
        self.grid_idx -= 1
        if self.grid_idx > 0:
            while self.original[self.grid_idx] != 0:
                self.grid_idx -= 1


if __name__ == "__main__":

    file_list = ["novice", "easy", "medium", "hard", "impossible"]
    difficulty = choice(file_list)
    file_name = "puzzles/" + difficulty + ".csv"

    puzzle = ComputerSolve()
    puzzle.load_puzzle(file_name)

    puzzle.show_puzzle()

    print("Puzzle difficulty =", difficulty)
    print("Press any key to continue...")
    k = readkey()
    print("Solving...")

    puzzle.grid_idx = 0
    puzzle.solve()
    puzzle.show_puzzle()
    puzzle.check_solution()