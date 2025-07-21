import tkinter as tk
from tkinter import simpledialog

point =11000
CP = 1
multi=1
# --- Classes ---
class Perk:
    def __init__(self,type,cost,power,tier):
        self.type=type
        self.cost=cost
        self.power=power
        self.tier=tier
        self.button=None
    def command(self):
        global point, CP,multi
        if point >= self.cost:
            point -= self.cost
            multi *= self.power
            player['font'].append(self.type)
            click_me.config(font=('Ariel', 50 ,' '.join(player['font'])))
            pointLabelPoint.config(text=str(point) + ' coin')
            pointLabelPower.config(text=str(CP*multi) + ' click power')
            self.button.destroy()

    def checkconp(self):#check condition
        if point >= self.cost/2 and not self.button.winfo_ismapped():
            self.button.grid(row=self.tier,column=2)
        elif point < self.cost/2 and self.button.winfo_ismapped():
            self.button.grid_forget()
class Upgrade:
    def __init__(self, level, cost,power,tier):
        self.level = level
        self.cost = cost
        self.power=power
        self.tier=tier
        self.button=None
    def update(self):
        self.level += 1
        self.cost = int(self.cost * 1.15) + 1

    def command(self):
        global point, CP,multi
        if point >= self.cost:
            point -= self.cost
            CP += self.power
            self.update()
            pointLabelPoint.config(text=str(point) + ' coin')
            pointLabelPower.config(text=str(CP*multi) + ' click power')
            if self.button:
                self.button.config(
                    text=f"({self.level}) +1 CP \n{self.cost} coin"
                )
    def checkconu(self):#check condition
        if point >= self.cost/2 and not self.button.winfo_ismapped():
            self.button.grid(row=self.tier,column=1)
        elif point < self.cost/2 and self.button.winfo_ismapped():
            self.button.grid_forget()
# --- Objects ---
player={
    'fontstyle':'Ariel',
    'font':['normal'],
    "color":'',
    'bg':''
}
upgrade1 = Upgrade(0, 10,1,0)
upgrade2= Upgrade(0, 200,5,1)
perk1=Perk('bold',100,1.5,0)
perk2=Perk('italic',1000,2,1)
# --- Functions ---
def click():
    global point
    point += (CP*multi)
    pointLabelPoint.config(text=str(point) + ' coin')
    perk1.checkconp()
    upgrade2.checkconu()
    perk2.checkconp()
def toggle_menu():
    if upframe.winfo_ismapped():
        upframe.place_forget()
        toggle_button.config(text="Show Menu")
    else:
        upframe.place(anchor='s',relx=0.5,rely=1)
        toggle_button.config(text="Hide Menu")
# --- Windows ---
game = tk.Tk()
game.title("Clicker")
game.geometry("450x800")

player_name = simpledialog.askstring("Player Name", "Enter your name:", parent=game)
if not player_name:
    player_name = "Player"
## --- Frames ---
upframe=tk.LabelFrame(
    game,
    text="upgrades and perks",
    width=200,
    height=100
)
# --- Widgets ---
pointLabelPoint = tk.Label(
    game,
    text=str(point) + ' coin',
    font=('Ariel', 30))
pointLabelPower = tk.Label(
    game,
    text=str(CP*multi) + ' click power')

click_me = tk.Button(
    game,
    text=str(player_name),
    fg=('black'),
    bg=('white'),
    font=('Ariel', 50,' '.join(player['font'])),
    command=click
)
toggle_button = tk.Button(
    game,
    text="Hide Menu",
    command=toggle_menu)

#upgrade button:
upgrade1.button = tk.Button(
    upframe,
    text=f"({upgrade1.level}) +1 CP \n{upgrade1.cost} coin",
    font=('Ariel', 20),
    command= upgrade1.command,
    height=2,
    width=10
)
upgrade2.button = tk.Button(
    upframe,
    text=f"({upgrade2.level}) +5 CP \n{upgrade2.cost} coin",
    font=('Ariel', 20),
    command= upgrade2.command,
    height=2,
    width=10
)
perk1.button = tk.Button(
    upframe,
    text=f"BOLD x1.5 CP \n{perk1.cost} coin",
    font=('Ariel', 20),
    command=perk1.command,
    height=2,
    width=10
)
perk2.button = tk.Button(
    upframe,
    text=f"ITALIC x2 CP \n{perk2.cost} coin",
    font=('Ariel', 20),
    command=perk2.command,
    height=2,
    width=10
)
# --- Layout ---
#"450x800"
pointLabelPoint.place(anchor='n',relx=0.5,rely=0)
pointLabelPower.place(anchor='n',relx=0.5,rely=0.05)
click_me.place(anchor='n',relx=0.5,rely=0.4)
toggle_button.place(anchor='s',relx=0.15,rely=0.8)
upframe.place(anchor='s',relx=0.5,rely=1)
upframe.pack_propagate(False)
upgrade1.button.grid(row=0,column=1)
if point!=0: #every other upgrades and perk goes here
     perk1.button.grid(row=0,column=2)
     upgrade2.button.grid(row=1,column=1)
     perk2.button.grid(row=1, column=2)
# --- Mainloop ---
game.mainloop()

