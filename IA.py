import random  # Required import for random.choice()

def ai_choose_random_cell(board):
    empty_cells = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return random.choice(empty_cells)

def ai_choose_improved_cell(grid, ai_symbol, player_symbol):
    # Check if the AI can win
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                grid[i][j] = ai_symbol
                if check_victory(grid)[0]:  # If the AI wins with this move
                    return i, j
                grid[i][j] = ' '  # Undo the test

    # Block an imminent victory of the player
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                grid[i][j] = player_symbol
                if check_victory(grid)[0]:  # If the player wins with this move
                    grid[i][j] = ' '  # Undo the test
                    return i, j
                grid[i][j] = ' '  # Undo the test

    # Otherwise, choose a random cell
    return ai_choose_random_cell(grid)
