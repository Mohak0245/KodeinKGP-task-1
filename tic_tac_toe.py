import random

grid = [[" "," "," "], [" "," "," "], [" "," "," "]]

def check_win():

    if grid[0][0] == grid[1][0] == grid[2][0] != " ":
        return grid[0][0]
    elif grid[0][1] == grid[1][1] == grid[2][1] != " ":
        return grid[0][1]
    elif grid[0][2] == grid[1][2] == grid[2][2] != " ":
        return grid[0][2]
    elif grid[0][0] == grid[0][1] == grid[0][2] != " ":
        return grid[0][0]
    elif grid[1][0] == grid[1][1] == grid[1][2] != " ":
        return grid[1][0]
    elif grid[2][0] == grid[2][1] == grid[2][2] != " ":
        return grid[2][0]
    elif grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return grid[0][2]
    else:
        return "Draw"

def is_empty():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                return True
    return False

def rand_coord_gen():
    comp_coord_x = random.randint(0, 2)
    comp_coord_y = random.randint(0, 2)
    return [comp_coord_x, comp_coord_y]

def take_inp(user_choice):
    row = int(input("Enter the input row location\n"))
    col = int(input("Enter the input col location\n"))
    grid[row - 1][col - 1] = user_choice
    coord = rand_coord_gen()
    if user_choice == "X":
        comp_choice = "O"
    else:
        comp_choice = "X"
    if is_empty():
        while grid[coord[0]][coord[1]] != " ":
            coord = rand_coord_gen()
        else:
            grid[coord[0]][coord[1]] = comp_choice

def print_grid():
        print(f"[{grid[0][0]}] [{grid[0][1]}] [{grid[0][2]}]\n[{grid[1][0]}] [{grid[1][1]}] [{grid[1][2]}]\n[{grid[2][0]}] [{grid[2][1]}] [{grid[2][2]}]")


while 1:
    print_grid()
    take_inp("X")
    result = check_win()
    if result == "X" or result == "O":
        print(f"{result} wins\n")
        print_grid()
        break
    elif result == "Draw":
        if is_empty():
            pass
        else:
            print(result)
            print_grid()
            break
