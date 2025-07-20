import tkinter as tk
from tkinter import simpledialog
point=0
adder=1
up1cost=10

#function:
def click():
    global point
    point+=adder
    pointLabelPoint.config(text=str(point)+' coin')
def up1():
    global point,adder,up1cost
    if point>up1cost:
        adder+=1
        point-=up1cost
        pointLabelPoint.config(text=str(point) + ' coin')
        pointLabelPower.config(text=str(adder) + ' click power')

#window create:
game=tk.Tk()
game.title("clicker")
game.geometry("800x450")

#random:
player_name = simpledialog.askstring("Player Name", "Enter your name:", parent=game)
if not player_name:
    player_name = "Player"

#frame:
Frame=tk.Frame(game)

#button
click_me=tk.Button(
    game,
    text=str(player_name),
    font=('Ariel',50),
    command=click
)
upgrade1=tk.Button(
    game,
    text=f"+1 click power {up1cost} coin",
    font=('Ariel' ,20),
    command=up1,
    height=1,
    width=20
)

#label:
pointLabelPoint=tk.Label(game,text=str(point)+' coin',font=('Ariel',30))
pointLabelPower=tk.Label(game,text=str(adder)+' click power')

#display:
pointLabelPoint.pack()
pointLabelPower.pack()
click_me.pack()
upgrade1.pack(side='right')
game.mainloop()