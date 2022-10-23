
def locations_list(game_grid):
    mine_list = []
    for row in range(len(game_grid)):
        for col in range(len(game_grid[0])):
            if game_grid[row][col] == 1:
                mine_list.append((row, col))
    return mine_list
