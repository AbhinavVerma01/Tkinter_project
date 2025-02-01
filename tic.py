import tkinter as tk
from tkinter import messagebox

# Function to check for a win or draw
def check_win():
    for i in range(3):
        # Check rows and columns
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    # Check for a draw
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] == '':
                return False
    return 'Draw'

# Function to handle button clicks
def button_click(row, col):
    if buttons[row][col]['text'] == '' and not winner_found:
        buttons[row][col]['text'] = player
        result = check_win()
        if result == 'Draw':
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        elif result:
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        else:
            switch_player()

# Function to switch players
def switch_player():
    global player
    player = 'O' if player == 'X' else 'X'

# Function to reset the game
def reset_game():
    global winner_found
    winner_found = False
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='')
    global player
    player = 'X'

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize the board and player
buttons = [[None, None, None] for _ in range(3)]
player = 'X'
winner_found = False

# Create the buttons for the board
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('normal', 40), width=5, height=2, command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the game loop
root.mainloop()
