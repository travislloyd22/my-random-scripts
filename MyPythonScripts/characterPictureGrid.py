# copy module for list manipulation
import copy

# Grid variable
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Remember print('Hello', end='') to avoid a newline when not needed


# Print the following picture from grid
# ..OO.OO.. 
# .OOOOOOO. 
# .OOOOOOO. 
# ..OOOOO.. 
# ...OOO... 
# ....O....

new_grid = copy.deepcopy(grid)

# Sets the new_grid list with empty lists
for i in range(len(grid)):
    new_grid[i] = []

# Moves the y values to x and x values to y
for x in range(len(grid)):
    for y in range(len(grid[x])):
        new_grid[y].append(grid[x][y])

# Prints the new_grid list to the screen
for x in range(len(new_grid)):
    # Ignores any empty lists that remain
    if new_grid[x]:
        for y in range(len(new_grid[x])):
            if y < len(new_grid[x]) - 1:
                print(new_grid[x][y], end='')
            else:
                print(new_grid[x][y])
