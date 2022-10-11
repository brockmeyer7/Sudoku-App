from puzzle import Puzzle

# Get user input to choose between solving Sudoku and entering sudoku to be solved

while True:
    print("\n")
    print("------------------MENU-------------------")
    print("1) Play Sudoku\n2) Exit game")
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
            puzzle = Puzzle(file_name)
            if puzzle.solve_puzzle():
                while not puzzle.check_solution():
                    puzzle.render_puzzle()
                    puzzle.solve_puzzle()
        else:
            print("\nPlease enter valid option")
    elif choice == "2":
        exit()
    else:
        print("\nPlease enter valid option\n")
