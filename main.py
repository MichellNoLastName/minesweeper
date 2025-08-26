from tkinter import *
import settings
import utils
from cell import Cell

root = Tk();
#settings of the window
root.configure(bg="Black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

topFrame = Frame(
    root,
    bg="black", #red
    width=settings.WIDTH,
    height=utils.heightPrct(25)
)

topFrame.place(x=0,y=0)

gameTitle = Label(
    topFrame,
    bg = "black",
    fg = "white",
    text="Minesweeper Game",
    font=("",48)
)

gameTitle.place(x=utils.widthPrct(25),y=0)

leftFrame = Frame(
    root,
    bg="black", #blue
    width=utils.widthPrct(25),
    height=utils.heightPrct(75)
)

leftFrame.place(x=0,y=utils.heightPrct(25))

centerFrame = Frame(
    root,
    bg="black", #green
    width=utils.widthPrct(75),
    height=utils.heightPrct(75)
)

centerFrame.place(x=utils.widthPrct(25),y=utils.heightPrct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.createBtnObject(centerFrame)

#Creation mines
Cell.randomizeMines()

Cell.createCellCountLabel(leftFrame)

root.mainloop();