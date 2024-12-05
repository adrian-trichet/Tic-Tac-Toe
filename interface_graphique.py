import tkinter as tk
import random

# Function to center the window on the screen
def center_window(window, width, height):
    """
    Centers the window of the application on the screen.
    
    Parameters:
        window (tk.Tk): The Tkinter window to be centered.
        width (int): The width of the window.
        height (int): The height of the window.
    """
    screen_width = window.winfo_screenwidth()  # Get the width of the screen
    screen_height = window.winfo_screenheight()  # Get the height of the screen
    position_top = int(screen_height / 2 - height / 2)  # Calculate the top position
    position_right = int(screen_width / 2 - width / 2)  # Calculate the left position
    window.geometry(f'{width}x{height}+{position_right}+{position_top}')  # Set window geometry

# Function to start the game based on the selected mode
def start_game():
    """
    Retrieves the selected mode (easy AI or 2 players)
    and launches the corresponding game function.
    """
    mode = mode_var.get()  # Get the selected mode
    root.destroy()  # Close the mode selection window
    if mode == "Easy AI":
        play_game(True, "easy")  # Easy AI mode
    else:
        play_game(False, "")  # 2 players mode

# Main function that handles the game logic
def play_game(is_ai_mode, ai_level):
    """
    Initializes and starts the Tic Tac Toe game.
    
    Parameters:
        is_ai_mode (bool): If True, AI plays against the player.
        ai_level (str): The AI difficulty level ("easy").
    """
    # Create the game window
    game_root = tk.Tk()
    game_root.title("Tic Tac Toe")
    game_root.resizable(False, False)  # Disable window resizing
    
    # Center the window
    center_window(game_root, 500, 500)

    current_player = 'X'  # The player starts with 'X'
    buttons = []  # List to store the buttons of the grid
    grid = [[' ' for _ in range(3)] for _ in range(3)]  # Matrix to represent the game state

    # Label to display victory or draw messages
    message_label = tk.Label(game_root, text="", font=("Arial", 20))
    message_label.grid(row=3, column=0, columnspan=3)

    def disable_buttons():
        """Disables all buttons after the game ends."""
        for row in buttons:
            for button in row:
                button.config(state="disabled")

    def button_click(row, col):
        """
        Handles button clicks in the grid, updates the game state,
        and checks for victory.
        
        Parameters:
            row (int): The row of the clicked button.
            col (int): The column of the clicked button.
        """
        nonlocal current_player
        if buttons[row][col]['text'] != " ":
            return  # Ignore click if the button is already occupied
        buttons[row][col].config(text=current_player)
        grid[row][col] = current_player
        victory, message = check_victory(grid)
        if victory:
            message_label.config(text=message)
            disable_buttons()
            return
        if all(cell != ' ' for row in grid for cell in row):  # Check if the grid is full
            message_label.config(text="Draw!")
            disable_buttons()
            return
        current_player = 'O' if current_player == 'X' else 'X'  # Switch players
        if is_ai_mode and current_player == 'O':
            ai_move(ai_level)

    def check_victory(grid):
        """
        Checks if there is a winner.
        
        Parameters:
            grid (list): The matrix representing the game state.
        
        Returns:
            tuple: A boolean indicating if a victory was detected,
                   and a victory or non-victory message.
        """
        # Check rows
        for row in grid:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True, f"Player '{row[0]}' wins (row)."
        # Check columns
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != ' ':
                return True, f"Player '{grid[0][col]}' wins (column)."
        # Check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
            return True, f"Player '{grid[0][0]}' wins (diagonal)."
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
            return True, f"Player '{grid[0][2]}' wins (diagonal)."
        return False, ""  # No winner yet

    def ai_move(level):
        """
        Handles the AI's move with a delay.
        
        Parameters:
            level (str): The difficulty level of the AI ("easy").
        """
        game_root.after(2000, make_ai_move, level)

    def make_ai_move(level):
        """Makes the AI move according to the selected difficulty level."""
        if level == "easy":
            easy_ai_move()  # Easy AI

    def easy_ai_move():
        """
        The easy AI chooses a random move from available empty spaces.
        """
        available = available_moves()
        if available:
            move = random.choice(available)  # Choose a random move
            button_click(move[0], move[1])

    def available_moves():
        """
        Returns a list of available moves (empty spaces).
        
        Returns:
            list: List of tuples (row, column) of empty spaces.
        """
        return [(r, c) for r in range(3) for c in range(3) if grid[r][c] == ' ']

    def create_buttons():
        """
        Creates the buttons for the Tic Tac Toe grid.
        """
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(game_root, text=" ", font=("Arial", 50), width=5, height=2,
                                   command=lambda r=row, c=col: button_click(r, c))
                button.grid(row=row, column=col, sticky="nsew")  # Use grid for flexible layout
                button_row.append(button)
            buttons.append(button_row)

        # Ensure the grid cells are resizable
        for i in range(3):
            game_root.grid_columnconfigure(i, weight=1)
            game_root.grid_rowconfigure(i, weight=1)

    create_buttons()  # Create the game grid
    game_root.mainloop()  # Start the main game loop

# Mode selection interface
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)  # Disable window resizing

# Center the mode selection window
center_window(root, 500, 500)

mode_var = tk.StringVar()
mode_var.set("2 Players")  # Default mode

# Create the mode selection radio buttons
tk.Radiobutton(root, text="2 Players", variable=mode_var, value="2 Players", font=("Arial", 20)).pack()
tk.Radiobutton(root, text="Play Versus Easy AI", variable=mode_var, value="Easy AI", font=("Arial", 20)).pack()

# Button to start the game
start_button = tk.Button(root, text="Start Game", font=("Arial", 20), command=start_game)
start_button.pack()

root.mainloop()  # Start the mode selection window
