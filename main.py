import random  # Required import for random.choice()

def player_move(grid, player):
    while True:
        try:
            move = input(f"Player with '{player}', enter your move (row,column, between 1 and 3): ")
            row, col = map(int, move.split(','))
            row -= 1
            col -= 1
            
            if 0 <= row < 3 and 0 <= col < 3:
                if grid[row][col] == ' ':
                    grid[row][col] = player
                    break
                else:
                    print("This cell is already occupied. Try another one.")
            else:
                print("Coordinates must be between 1 and 3. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Make sure to enter valid coordinates (e.g.: 1,2).")

def ai_move(grid, ai_symbol, player_symbol, difficulty):
    if difficulty == 'easy':
        row, col = ai_choose_random_cell(grid)
    else:  # Difficulty 'hard'
        row, col = ai_choose_improved_cell(grid, ai_symbol, player_symbol)
    grid[row][col] = ai_symbol
    print(f"AI plays at ({row + 1}, {col + 1})")

def display_grid(grid):
    for row in grid:
        print(' | '.join(row))
        print('-' * 9)

def check_victory(grid):
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True, f"The player with '{row[0]}' won."

    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
            return True, f"The player with '{grid[0][col]}' won."

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return True, f"The player with '{grid[0][0]}' won."
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return True, f"The player with '{grid[0][2]}' won."

    return False, "No victory yet."

def check_draw(grid):
    return all(cell != ' ' for row in grid for cell in row)

def choose_game_mode():
    while True:
        mode = input("Choose the game mode:\n1 - Play against AI\n2 - Play with two players\nYour choice (1 or 2): ")
        if mode in ['1', '2']:
            return int(mode)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def choose_difficulty():
    while True:
        difficulty = input("Choose AI difficulty level:\neasy - Random AI\nhard - Smart AI\nYour choice: ").lower()
        if difficulty in ['easy', 'hard']:
            return difficulty
        else:
            print("Invalid choice. Please enter 'easy' or 'hard'.")

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

#################################################################
##################### Game initialization #######################
#################################################################


grid = [[' ' for _ in range(3)] for _ in range(3)]

player_symbol = 'X'
ai_symbol = 'O'

# Choose game mode
game_mode = choose_game_mode()

if game_mode == 1:
    print("Game mode: Player vs AI.")
    difficulty = choose_difficulty()
else:
    print("Game mode: Two players.")

# Main loop
while True:
    display_grid(grid)
    
    # Player 1's turn
    player_move(grid, player_symbol)
    victory, message = check_victory(grid)
    if victory:
        display_grid(grid)
        print(message)
        break
    if check_draw(grid):
        display_grid(grid)
        print("It's a draw!")
        break

    if game_mode == 1:  # Player vs AI
        # AI's turn
        ai_move(grid, ai_symbol, player_symbol, difficulty)
    else:  # Two players mode
        # Player 2's turn
        display_grid(grid)
        player_move(grid, ai_symbol)

    victory, message = check_victory(grid)
    if victory:
        display_grid(grid)
        print(message)
        break
    if check_draw(grid):
        display_grid(grid)
        print("It's a draw!")
        break
