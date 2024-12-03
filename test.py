import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Morpion")
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.player_symbol = 'X'
        self.ia_symbol = 'O'
        self.game_mode = None
        self.turn = "Player"  # Alternates between "Player" and "IA"

        self.create_start_screen()

    def create_start_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Choisissez le mode de jeu", font=("Arial", 14)).pack(pady=20)
        tk.Button(self.root, text="Joueur contre IA", command=self.start_game_vs_ia).pack(pady=5)
        tk.Button(self.root, text="Deux joueurs", command=self.start_game_two_players).pack(pady=5)

    def start_game_vs_ia(self):
        self.game_mode = 1
        self.create_game_board()

    def start_game_two_players(self):
        self.game_mode = 2
        self.create_game_board()

    def create_game_board(self):
        self.clear_screen()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                command=lambda x=i, y=j: self.handle_click(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def handle_click(self, row, col):
        if self.grid[row][col] == ' ':
            if self.game_mode == 1 and self.turn == "Player":
                self.grid[row][col] = self.player_symbol
                self.buttons[row][col].config(text=self.player_symbol)
                self.check_game_state()
                self.turn = "IA"
                self.root.after(500, self.ia_move)
            elif self.game_mode == 2:
                current_symbol = self.player_symbol if self.turn == "Player" else self.ia_symbol
                self.grid[row][col] = current_symbol
                self.buttons[row][col].config(text=current_symbol)
                self.check_game_state()
                self.turn = "Player" if self.turn == "IA" else "IA"

    def ia_move(self):
        if self.turn == "IA":
            row, col = self.ia_choose_random_cell()
            self.grid[row][col] = self.ia_symbol
            self.buttons[row][col].config(text=self.ia_symbol)
            self.check_game_state()
            self.turn = "Player"

    def ia_choose_random_cell(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.grid[i][j] == ' ']
        return random.choice(empty_cells)

    def check_game_state(self):
        victory, message = self.check_victory()
        if victory:
            self.end_game(message)
        elif self.check_draw():
            self.end_game("Match nul !")

    def check_victory(self):
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True, f"Le joueur avec '{row[0]}' a gagné !"

        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != ' ':
                return True, f"Le joueur avec '{self.grid[0][col]}' a gagné !"

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != ' ':
            return True, f"Le joueur avec '{self.grid[0][0]}' a gagné (diagonale) !"
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != ' ':
            return True, f"Le joueur avec '{self.grid[0][2]}' a gagné (diagonale) !"

        return False, ""

    def check_draw(self):
        return all(cell != ' ' for row in self.grid for cell in row)

    def end_game(self, message):
        messagebox.showinfo("Fin de la partie", message)
        self.create_start_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Lancement du jeu
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
