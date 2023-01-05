from puzzle import Puzzle
from computersolve import ComputerSolve
import sys

# Get user input to choose between solving Sudoku and entering sudoku to be solved

while True:
    print("\n")
    print("------------------MENU-------------------")
    print("1) Play Sudoku\n2) Computer Solve\n3) Exit game")
    choice = input("Choose your mode: ")

    if choice == "1":

        print("\nChoose difficulty:\n1) Novice\n2) Easy\n3) Medium\n4) Hard\n5) Impossible")
        user_input = input("Selection: ")

        if user_input == "1":
            level = "novice"
        elif user_input == "2":
            level = "easy"
        elif user_input == "3":
            level = "medium"
        elif user_input == "4":
            level = "hard"
        elif user_input == "5":
            level = "impossible"
        elif user_input == "6":
            level = "test"
        else:
            level = ""
        if level != "":
            file_name = "puzzles/" + level + ".csv"
            puzzle = Puzzle()
            puzzle.load_puzzle(file_name)
            if puzzle.solve_puzzle():
                while not puzzle.check_solution():
                    puzzle.show_puzzle()
                    puzzle.solve_puzzle()
        else:
            print("\nPlease enter valid option")
    elif choice == "2":
        puzzle = ComputerSolve()
        print(
            "Choose puzzle input style:\n1) User entered puzzle\n2) Randomly chosen puzzle")
        user_input = input("Selection:")
        if user_input == "1":
            puzzle.show_puzzle()
            puzzle.fill_puzzle()
        elif user_input == "2":
            pass
        puzzle.solve()
    elif choice == "3":
        sys.exit()
    else:
        print("\nPlease enter valid option\n")
