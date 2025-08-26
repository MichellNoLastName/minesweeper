from inspect import getcoroutinelocals
import stat
from tkinter import Button, Label, messagebox
import logging
import random
import settings
import sys
import ctypes

logging.basicConfig(level=logging.DEBUG,format='%(message)s')
class Cell:
    all = []
    cellCount = settings.CELL_COUNT
    cellCountLabelObject = None
    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.isOpened = False
        self.isMineCandidate = False
        self.cellBtnObject = None
        self.x = x
        self.y = y
        self.minesCount = 0
        self.surroundedCells = []

        Cell.all.append(self)
    
    def winGame(self):
        if Cell.cellCount == 0:
            ctypes.windll.user32.MessageBoxW(0,"Congratulations! ", "Game Over", 0)

    def createBtnObject(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text="",
            bg="white"
        )
        btn.bind("<Button-1>", self.leftClickActions)
        btn.bind("<Button-3>", self.rightClickActions)
        self.cellBtnObject = btn
        self.cellBtnObject.grid(column=self.y,row=self.x)

    @staticmethod
    def createCellCountLabel(location):
        label = Label(
            location,
            bg="black",
            fg="white",
            width=12,
            height=4,
            text=f'Cells Left: {Cell.cellCount}',
            font=("",30)
        )
        label.place(x=0,y=0)
        Cell.cellCountLabelObject = label


    def leftClickActions(self,event):
        logging.debug(event)
        logging.debug("left clicked!")
        if self.isMine:
            self.showMine()
        else:
            self.showCell()
            if self.minesCount == 0:
                    for cell in self.surroundedCells:
                        cell.showCell()
        self.winGame()

    def rightClickActions(self,event):
        logging.debug(event)
        logging.debug("Right clicked!")
        if self.isMine:
            self.cellBtnObject.configure(bg="green")
            self.refreshLabel()
            self.cellBtnObject.unbind("<Button-1>")
            self.cellBtnObject.unbind("<Button-3>")
            self.winGame()
        
        elif not self.isMineCandidate:
            self.cellBtnObject.configure(bg="orange")
        elif self.isMineCandidate:
            self.cellBtnObject.configure(bg="white")
        self.isMineCandidate = True


    def getCellByAxis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def showMine(self):
        #A logic do interrupt the game and display a message that player lost
        self.cellBtnObject.configure(bg="red")
        messagebox.showerror(message="You pressed a mine", title="GAME OVER")
        sys.exit(0)
    
    def surroundCells(self):
        cells = []
        for x in range(self.x -1, self.x +2):
            for y in range(self.y - 1, self.y + 2):
                cell = self.getCellByAxis(x,y)
                cells.append(cell)
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surroundMines(self):
        counter = 0
        self.surroundedCells = self.surroundCells()
        for cell in self.surroundedCells:
            if cell.isMine:
                counter += 1

        return counter
    
    def refreshLabel(self):
        Cell.cellCount -= 1
        if Cell.cellCountLabelObject:
                Cell.cellCountLabelObject.configure(text=f'Cells Left: {Cell.cellCount}')

    def showCell(self):
        if not self.isOpened:
            self.minesCount = self.surroundMines
            self.cellBtnObject.configure(text=f'{self.minesCount}')
            self.refreshLabel()
        self.isOpened = True

    @staticmethod
    def randomizeMines():
        pickedCells = random.sample(Cell.all,settings.MINES_COUNT)
        for picked in pickedCells:
            picked.isMine = True
    
