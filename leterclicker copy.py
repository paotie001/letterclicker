import tkinter as tk
from tkinter import simpledialog

point = 0
clickPower = 1

# --- Upgrade Class ---
class Upgrade:
    def __init__(self, level, cost):
        self.level = level
        self.cost = cost

    def update(self):
        self.level += 1
        self.cost = int(self.cost * 1.15) + 1

# --- Object ---
upgrade1_obj = Upgrade(0, 10)

# --- Functions ---
def click():
    global point
    point += clickPower
    pointLabelPoint.config(text=str(point) + ' coin')

def up1():
    global point, clickPower
    if point >= upgrade1_obj.cost:
        point -= upgrade1_obj.cost
        clickPower += 1
        upgrade1_obj.update()
        pointLabelPoint.config(text=str(point) + ' coin')
        pointLabelPower.config(text=str(clickPower) + ' click power')
        upgrade1_button.config(
            text=f"({upgrade1_obj.level}) +1 click power {upgrade1_obj.cost} coin"
        )

# --- Window ---
game = tk.Tk()
game.title("Clicker")
game.geometry("800x450")

player_name = simpledialog.askstring("Player Name", "Enter your name:", parent=game)
if not player_name:
    player_name = "Player"

# --- Widgets ---
pointLabelPoint = tk.Label(game, text=str(point) + ' coin', font=('Ariel', 30))
pointLabelPower = tk.Label(game, text=str(clickPower) + ' click power')

click_me = tk.Button(
    game, text=f"Click, {player_name}!", font=('Ariel', 50), command=click
)

upgrade1_button = tk.Button(
    game,
    text=f"({upgrade1_obj.level}) +1 click power {upgrade1_obj.cost} coin",
    font=('Ariel', 20),
    command=up1,
    height=1,
    width=30
)

# --- Layout ---
pointLabelPoint.pack()
pointLabelPower.pack()
click_me.pack()
upgrade1_button.pack(side='right')

# --- Mainloop ---
game.mainloop()
