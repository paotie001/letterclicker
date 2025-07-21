import tkinter as tk
from tkinter import simpledialog

point = 0
CP = 1

# --- Classes ---
class Perk:
    def __init__(self,type,cost):
        self.type=type
        self.cost=cost
        self.button=None
    def command(self):
        global point, CP
        if point >= self.cost:
            point -= self.cost
            CP *= 1.5
            click_me.config(font=('Ariel', 50, self.type))
            pointLabelPoint.config(text=str(point) + ' coin')
            pointLabelPower.config(text=str(CP) + ' click power')
            self.button.destroy()

    def checkconp(self):#check condition
        if point >= self.cost/2 and not self.button.winfo_ismapped():
            self.button.pack(side='left')
        elif point < self.cost/2 and self.button.winfo_ismapped():
            self.button.pack_forget()
class Upgrade:
    def __init__(self, level, cost):
        self.level = level
        self.cost = cost
        self.button=None
    def update(self):
        self.level += 1
        self.cost = int(self.cost * 1.15) + 1

    def command(self):
        global point, CP
        if point >= self.cost:
            point -= self.cost
            CP += 1
            self.update()
            pointLabelPoint.config(text=str(point) + ' coin')
            pointLabelPower.config(text=str(CP) + 'CP')
            if self.button:
                self.button.config(
                    text=f"({self.level}) +1 CP {self.cost} coin"
                )
    def checkconu(self):#check condition
        if point >= self.cost/2 and not self.button.winfo_ismapped():
            self.button.pack(side='right')
        elif point < self.cost/2 and self.button.winfo_ismapped():
            self.button.pack_forget()
# --- Objects ---
upgrade1 = Upgrade(0, 10)
perk1=Perk('bold',100)

# --- Functions ---
def click():
    global point
    point += CP
    pointLabelPoint.config(text=str(point) + ' coin')
    perk1.checkconp()

# --- Windows ---
game = tk.Tk()
game.title("Clicker")
game.geometry("450x800")

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
    text=str(CP) + ' click power')

click_me = tk.Button(
    game,
    text=str(player_name),
    fg=('black'),
    bg=('white'),
    font=('Ariel', 50),
    command=click
)

upgrade1.button = tk.Button(
    game,
    text=f"({upgrade1.level}) +1 CP \n{upgrade1.cost} coin",
    font=('Ariel', 20),
    command= upgrade1.command,
    height=2,
    width=10
)
perk1.button = tk.Button(
    game,
    text=f"BOLD x1.5 CP \n{perk1.cost} coin",
    font=('Ariel', 20),
    command=perk1.command,
    height=2,
    width=10
)
# --- Layout ---
pointLabelPoint.pack()
pointLabelPower.pack()
click_me.pack()
upgrade1.button.pack(side='left')
if point!=0: #every other upgrades and perk goes here
    perk1.button.pack(side='right')
# --- Mainloop ---
game.mainloop()
print()
