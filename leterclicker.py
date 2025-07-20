import tkinter as tk
from tkinter import simpledialog

point = 0
clickPower = 1

# --- Classes ---
class Perk:
    def __init__(self,type,cost):
        self.type=type
        self.cost=cost
class Upgrade:
    def __init__(self, level, cost):
        self.level = level
        self.cost = cost

    def update(self):
        self.level += 1
        self.cost = int(self.cost * 1.15) + 1

# --- Objects ---
upgrade1_obj = Upgrade(0, 10)
perk1_obj=Perk('bold',100)
def check_perk1():
    if point >= 50 and not perk1_button.winfo_ismapped():
        perk1_button.pack(side='left')  # Show if not already visible
    elif point < 50 and perk1_button.winfo_ismapped():
        perk1_button.pack_forget()
# --- Functions ---
def click():
    global point
    point += clickPower
    pointLabelPoint.config(text=str(point) + ' coin')
    check_perk1()

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
def perk1():
    global point, clickPower,perk1_obj
    if point >= perk1_obj.cost:
        point -= perk1_obj.cost
        clickPower *= 1.5
        click_me.config(font=('Ariel', 50,"bold"))
        pointLabelPoint.config(text=str(point) + ' coin')
        pointLabelPower.config(text=str(clickPower) + ' click power')
        perk1_button.destroy()
# --- Windows ---
game = tk.Tk()
game.title("Clicker")
game.geometry("800x450")

player_name = simpledialog.askstring("Player Name", "Enter your name:", parent=game)
if not player_name:
    player_name = "Player"

# --- Widgets ---
pointLabelPoint = tk.Label(
    game,
    text=str(point) + ' coin',
    font=('Ariel', 30))
pointLabelPower = tk.Label(
    game,
    text=str(clickPower) + ' click power')

click_me = tk.Button(
    game,
    text=str(player_name),
    fg=('black'),
    bg=('black'),
    font=('Ariel', 50),
    command=click
)

upgrade1_button = tk.Button(
    game,
    text=f"({upgrade1_obj.level}) +1 click power {upgrade1_obj.cost} coin",
    font=('Ariel', 20),
    command=up1,
    height=1,
    width=30
)
perk1_button = tk.Button(
    game,
    text=f"change color x1.5 click power {perk1_obj.cost} coin",
    font=('Ariel', 20),
    command=perk1,
    height=1,
    width=30
)
# --- Layout ---
pointLabelPoint.pack()
pointLabelPower.pack()
click_me.pack()
upgrade1_button.pack(side='right')
if point>=50:
    perk1_button.pack(side='left')
# --- Mainloop ---
game.mainloop()

