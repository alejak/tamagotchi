# Specifikation för uppgift 168 minröj
# OBS!!! Uppgiften är förenklad i förhållande till ursprungslydelsen


# Datastruktur: En matris av spelplanens rutnät där varje objekt har instansvariablerna:
# position: namnet på rutan, d v s rutans placering i rutnätet (ex. H5) (string)
# mine: om rutan innehåller en mina eller ej (boolean)
# vicinity: antalet minor runtom rutan (integer)


# Algoritm:
# I kronologisk ordning sker följande:
#   1 - Användaren matar in sitt namn, hur stor spelplan som önskas och antalet minor (max  % av antalet rutor)
#   2 - Spelplanen skapas och minor placeras ut slumpmässigt, tidtagarur startas
#   3 - Användaren matar in vilken ruta i rutnätet den vill undersöka
#   4 - Såvida inte en mina finnes: (1) Där finns ingen mina men ett antal angränsande minor
#       eller (2) där finns ingen mina och ingea angränsande minor
#   5 - (1) Rutan anger en siffra som motsvarar antalet angränsande minor
#       alt. (2) spelplanet öppnas upp runtom rutan
#   6 - Spelet är slut när en mina sprängs, alt. när alla rutor utan minor undersökts
#   7 - Tidtagaruret stannar och tiden bedöms relativt till antalet minor för att forma ett resultat
#   8 - Om resultatet är bland de 10 bästa sparas det till en permanent fil medde bästa användarna 

from tkinter.ttk import *
from tkinter import *
import math
import random
import time


class MenuWindow:

    def __init__(self, master):
        self.master = master
        self.master.geometry("360x140")
        self.master.title("Mine Sweeper")
        self.master.configure(bg="grey")

        self.introText = Label(self.master, text = "Welcome to Mine Sweeper!", bg="grey", fg="black", font=("Arial", 20, "bold"))
        self.introText.pack()

        self.ngButton = Button(self.master, text="New Game", width='10', command = self.newGame)
        self.ngButton.pack()
        self.scoreButton = Button(self.master, text="Top 10", width='10', command = self.displayScore)
        self.scoreButton.pack()
        self.quitButton = Button(self.master, text="Quit!", width='10', command = self.quitGame)   
        self.quitButton.pack()
        
    def newGame(self):
        self.newNameWindow = Toplevel(self.master)
        self.app = NameWindow(self.newNameWindow)
        self.master.withdraw()

    def displayScore(self):
        None

    def quitGame(self):
        self.master.destroy()

class ScoreWindow:

    def __init__(self, master):
        self.master = master
        self.master.geometry("100x200")
        self.master.title("Scores")
        self.master.configure(bg="grey")        

        self.introText = Label(self.master, text = "Top 10!", bg="grey", fg="black", font=("Arial", 20, "bold"))
        self.introText.pack()

        self.scoreText = Text(self.master)
        self.scoreText.pack()

        self.returnButton = Button(root, text="Return", command = self.returnToMenu)
        self.returnButton.pack()

    def returnToMenu(self):

        self.newMenuWindow = Toplevel(self.master)
        self.app = MenuWindow(self.newMenuWindow)
        self.master.withdraw()

class NameWindow:

    def __init__(self, master):
        self.master = master
        self.master.geometry("300x100")
        self.master.title("Player Name")
        self.master.configure(bg="grey")

        self.introText = Label(self.master, text = "Enter you name below!", bg="grey", fg="black", font=("Arial", 20, "bold"))
        self.introText.pack()

        self.nameInput = StringVar()

        self.name = Entry(self.master, width=10, textvariable = self.nameInput)
        self.name.pack()

        self.done2 = Button(self.master, text="Enter", command = self.returnName)
        self.done2.pack()

    def returnName(self):
        gameInfo.name = self.nameInput.get()
        self.newDifficultyWindow = Toplevel(self.master)
        self.app = DifficultyWindow(self.newDifficultyWindow)
        self.master.withdraw()

class DifficultyWindow:

    def __init__(self, master):
        self.master = master
        self.master.geometry("300x200")
        self.master.title("Difficulty")
        self.master.configure(bg="grey")
        
        self.introText = Label(self.master, text = "Choose difficulty!", bg="grey", fg="black", font=("Arial", 20, "bold"))
        self.heightBox = Spinbox(self.master, from_=9, to=24, increment=1)
        self.widthBox = Spinbox(self.master, from_=9, to=30, increment=1)
        self.mineBox = Spinbox(self.master, from_=10, to=667, increment=1)

        self.difficultyInput = StringVar() 
        self.difficultyInput.set("Beginner")

        self.difficultyOption = OptionMenu(self.master, self.difficultyInput, "Beginner", "Intermediate", "Expert", "Custom") 
        self.done3 = Button(self.master, text="Enter", width='10', command = self.determineDifficulty)
        self.done4 = Button(self.master, text="Enter", width='10', command = self.checkCustom)
        self.returnBtn = Button(self.master, text="Return", width='10', command = self.returnChoice)

        self.introText.pack()
        self.difficultyOption.pack()
        self.done3.pack()

    def determineDifficulty(self):
        self.difficulty = self.difficultyInput.get()

        if self.difficulty == "Beginner":
            gameInfo.height = 9
            gameInfo.width = 9
            gameInfo.numberOfMines = 10
            self.forwardDifficulty()

        if self.difficulty == "Intermediate":
            gameInfo.height = 16
            gameInfo.width = 16
            gameInfo.numberOfMines = 40
            self.forwardDifficulty()            

        if self.difficulty == "Expert":
            gameInfo.height = 16
            gameInfo.width = 30
            gameInfo.numberOfMines = 99
            self.forwardDifficulty()

        if self.difficulty == "Custom":
            self.customDifficulty() 

    def customDifficulty(self):
        self.difficultyOption.pack_forget()
        self.done3.pack_forget()
        self.widthBox.pack()
        self.heightBox.pack()
        self.mineBox.pack()
        self.done4.pack()
        self.returnBtn.pack()

        self.errorText1 = StringVar()
        self.errorText2 = StringVar()

        Label(self.master, textvariable=self.errorText1, bg="grey", fg="black", font=("Arial", 12, "italic")).pack()
        Label(self.master, textvariable=self.errorText2, bg="grey", fg="black", font=("Arial", 12, "italic")).pack()

    def returnChoice(self):
        self.widthBox.pack_forget()
        self.heightBox.pack_forget()
        self.mineBox.pack_forget()
        self.done4.pack_forget()
        self.returnBtn.pack_forget()
        self.difficultyOption.pack()
        self.done3.pack()

    def checkCustom(self):

        if int(self.mineBox.get())>((int(self.heightBox.get())-1)*(int(self.widthBox.get())-1)):
            self.maxMines = (int(self.heightBox.get())-1)*(int(self.widthBox.get())-1)
            self.errorText1.set("Too many mines!")
            self.errorText2.set("Maximum " + str(self.maxMines) + " with current height and width.")
            
        else:
            gameInfo.height = int(self.heightBox.get())
            gameInfo.width = int(self.widthBox.get())
            gameInfo.numberOfMines = int(self.mineBox.get())
            self.forwardDifficulty()
    
    def forwardDifficulty(self):

        global gameEngine
        gameEngine = Engine()
        self.newGameWindow = Toplevel(self.master)
        self.app = GameWindow(self.newGameWindow)
        self.master.withdraw()

class GameWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("Mine Sweeper")
        self.master.configure(bg="grey")

        self.timeToggle = True
        self.trueFlagCount = 0
        self.score = 0
        self.leftClicks = 0

        self.lossText1 = Label(self.master, text= "Oh no, you stepped on a mine! Game over!")
        self.lossText2 = Label(self.master, text= "You correctly flagged " + str(self.trueFlagCount) + " mines of " + str(gameInfo.getNOM()) + ", so close!")
        self.lossText3 = Label(self.master, text= "Do you want to return to main menu or quit?")
        self.winText1 = Label(self.master, text= "Congratulations, you found all mines!")
        self.scoreText1 = Label(self.master, text= "You scored " + str(self.score) + "!")
        self.scoreText2 = Label(self.master, text= "Your score of " + str(self.score) + " managed you a spot on the leaderboar!")
        self.highScoreText = Label(self.master, text= "Your score of " + str(self.score) + " got you the High Score!!!")
        self.mainMenuBtn = Button(self.master, text="Main menu", width='10', command=self.returnMainMenu)
        self.leaderBoardBtn = Button(self.master, text="Leaderboard", width='10', command=self.returnLeaderBoard)
        self.quitBtn = Button(self.master, text= "Quit game", width='10', command=self.quitGame)

        self.tileImg = PhotoImage(file= "tile_plain.gif")
        self.clickedImg = PhotoImage(file= "tile_clicked.gif")
        self.mineImg = PhotoImage(file= "tile_mine.gif")
        self.flagImg = PhotoImage(file= "tile_flag.gif")
        self.toggleImg = PhotoImage(file= "flag.gif")
        self.vicinityImg = [PhotoImage(file= "tile_" + str(i+1) + ".gif") for i in range(8)]
        
        gameEngine.placeMines()
        gameEngine.applyVicinity()

        self.tileBtn = [[None for x in range(gameInfo.getWidth())] for y in range(gameInfo.getHeight())]
        
        for y in range(gameInfo.getHeight()):
            for x in range(gameInfo.getWidth()):
                
                self.tileBtn[y][x] = Button(self.master, image=self.tileImg, command= lambda y=y, x=x: self.examineButton(y,x))
                self.tileBtn[y][x].grid(column=x, row=y+3)

        self.toggleBtn = Button(self.master, image= self.toggleImg, command= self.flagToggleBtn)
        self.toggleBtn.grid(column=int(gameInfo.getWidth()/2), row=0, columnspan=2, rowspan=2)

        self.timeLabel = Label(self.master)
        self.timeLabel.grid(column=0, row=0)
        self.startTimer()

    def startTimer(self): #startar tidtagarur
        self.start = time.time()
        self.updateTimer()

    def updateTimer(self):
        now = time.time()-self.start
        self.timeLabel.configure(text=str(int(now)))
        if self.timeToggle == True:
            self.master.after(1000, self.updateTimer)
        
    def examineButton(self, y, x):

        status = gameEngine.examineTile(y,x)
        
        if status == "open":
            self.tileBtn[y][x].config(image = self.clickedImg)
            self.openVicinity(y,x)

        elif status == "mine":
            self.tileBtn[y][x].config(image = self.mineImg, bg='crimson')
            self.gameOver()

        elif status == None: None 
            
        else: self.vicinityImage(y,x)

        self.tileBtn[y][x].config(relief="sunken")
        self.leftClicks += 1
        self.checkWin()

    def flagTile(self, y, x):
        if gameEngine.tile[y][x].clicked == False:
            if gameEngine.tile[y][x].flagged == False:
                gameEngine.tile[y][x].flagged = True
                self.tileBtn[y][x].config(image = self.flagImg)
            else:
                gameEngine.tile[y][x].flagged = False
                self.tileBtn[y][x].config(image = self.tileImg)

        self.checkFlagWin()

    def flagToggleBtn(self):

        if self.toggleBtn.config('relief')[-1] == 'sunken':
            for y in range(gameInfo.getHeight()):
                for x in range(gameInfo.getWidth()):
                    self.tileBtn[y][x].config(command= lambda y=y, x=x: self.examineButton(y,x))
            self.toggleBtn.config(relief="raised")

        else:
            for y in range(gameInfo.getHeight()):
                for x in range(gameInfo.getWidth()):
                    self.tileBtn[y][x].config(command= lambda y=y, x=x: self.flagTile(y,x))
            self.toggleBtn.config(relief="sunken")

    def openVicinity(self, y, x):
        
        if y==0 and x==0:                                                   #opens vicinity of top left tile
            self.examineButton(y,x+1)
            self.examineButton(y+1,x+1)
            self.examineButton(y+1,x)

        elif y==0 and x==gameInfo.getWidth()-1:                             #opens vicinity of top right tile
            self.examineButton(y,x-1)
            self.examineButton(y+1,x-1)
            self.examineButton(y+1,x)

        elif y==gameInfo.getHeight()-1 and x==0:                            #opens vicinity of bottom left tile
            self.examineButton(y-1,x)
            self.examineButton(y-1,x+1)
            self.examineButton(y,x+1)

        elif y==gameInfo.getHeight()-1 and x==gameInfo.getWidth()-1:        #opens vicinity of bottom right tile
            self.examineButton(y,x-1)
            self.examineButton(y-1,x-1)
            self.examineButton(y-1,x)
        
        elif y==0 and x in range(1, gameInfo.getWidth()-1):                 #opens vicinity of a tile in the top row
            self.examineButton(y,x-1)
            self.examineButton(y+1,x-1)
            self.examineButton(y+1,x)
            self.examineButton(y+1,x+1)
            self.examineButton(y,x+1)

        elif y==gameInfo.getHeight()-1 and x in range(1,gameInfo.getWidth()-1):    #opens vicinity of a tile in the bottom row
            self.examineButton(y,x-1)
            self.examineButton(y-1,x-1)
            self.examineButton(y-1,x)
            self.examineButton(y-1,x+1)
            self.examineButton(y,x+1)

        elif y in range(1, gameInfo.getHeight()-1) and x==0:                #opens vici4nity of a tile in the left column
            self.examineButton(y-1,x)
            self.examineButton(y-1,x+1)
            self.examineButton(y,x+1)
            self.examineButton(y+1,x+1)
            self.examineButton(y+1,x)

        elif y in range (1,gameInfo.getHeight()-1) and x==gameInfo.getWidth()-1:    #opens vicinity of a tile in the right column
            self.examineButton(y-1,x)
            self.examineButton(y-1,x-1)
            self.examineButton(y,x-1)
            self.examineButton(y+1,x-1)
            self.examineButton(y+1,x)

        else:                                                               #opens vicinity of a tile enclosed by eight tiles
            self.examineButton(y-1,x-1)
            self.examineButton(y-1,x)
            self.examineButton(y-1,x+1)
            self.examineButton(y,x-1)
            self.examineButton(y,x+1)
            self.examineButton(y+1,x-1)
            self.examineButton(y+1,x)
            self.examineButton(y+1,x+1)

    def vicinityImage(self, y, x):
        if gameEngine.tile[y][x].vicinity == 1:
            self.tileBtn[y][x].config(image = self.vicinityImg[0])
        elif gameEngine.tile[y][x].vicinity == 2:
            self.tileBtn[y][x].config(image = self.vicinityImg[1])
        elif gameEngine.tile[y][x].vicinity == 3:
            self.tileBtn[y][x].config(image = self.vicinityImg[2])
        elif gameEngine.tile[y][x].vicinity == 4:
            self.tileBtn[y][x].config(image = self.vicinityImg[3])
        elif gameEngine.tile[y][x].vicinity == 5:
            self.tileBtn[y][x].config(image = self.vicinityImg[4])
        elif gameEngine.tile[y][x].vicinity == 6:
            self.tileBtn[y][x].config(image = self.vicinityImg[5])
        elif gameEngine.tile[y][x].vicinity == 7:
            self.tileBtn[y][x].config(image = self.vicinityImg[6])
        else: self.tileBtn[y][x].config(image = self.vicinityImg[7])

    def checkWin(self):
        
        openedTiles = 0
        for y in range(gameInfo.getHeight()):
            for x in range(gameInfo.getWidth()):
                if gameEngine.tile[y][x].mine != True:
                    if gameEngine.tile[y][x].clicked == True:
                        openedTiles += 1
        if openedTiles == (gameInfo.getHeight()*gameInfo.getWidth()-gameInfo.getNOM()):
            self.gameWin()

    def checkFlagWin(self):

        flaggedMines = 0
        for y in range(gameInfo.getHeight()):
            for x in range(gameInfo.getWidth()):
                if gameEngine.tile[y][x].mine == True:
                    if gameEngine.tile[y][x].flagged == True:
                        flaggedMines += 1
        if flaggedMines == (gameInfo.getNOM()):
            self.gameWin()
                        
    def gameOver(self): #hanterar spelförlust vid sprängd mina
        self.stopTimer()
        
        for y in range(gameInfo.getHeight()):
            for x in range(gameInfo.getWidth()):
                if gameEngine.tileMatrix[y][x] == 10:
                    if gameEngine.tile[y][x].flagged == True:
                        self.trueFlagCount += 1
                    self.tileBtn[y][x].config(image = self.mineImg)
                elif gameEngine.tile[y][x].vicinity == 1:
                    self.tileBtn[y][x].config(image = self.vicinityImg[0])
                elif gameEngine.tile[y][x].vicinity == 2:
                    self.tileBtn[y][x].config(image = self.vicinityImg[1])
                elif gameEngine.tile[y][x].vicinity == 3:
                    self.tileBtn[y][x].config(image = self.vicinityImg[2])
                elif gameEngine.tile[y][x].vicinity == 4:
                    self.tileBtn[y][x].config(image = self.vicinityImg[3])
                elif gameEngine.tile[y][x].vicinity == 5:
                    self.tileBtn[y][x].config(image = self.vicinityImg[4])
                elif gameEngine.tile[y][x].vicinity == 6:
                    self.tileBtn[y][x].config(image = self.vicinityImg[5])
                elif gameEngine.tile[y][x].vicinity == 7:
                    self.tileBtn[y][x].config(image = self.vicinityImg[6])
                elif gameEngine.tile[y][x].vicinity == 8:
                    self.tileBtn[y][x].config(image = self.vicinityImg[7])
                else: self.tileBtn[y][x].config(image = self.clickedImg)

                self.tileBtn[y][x].config(relief="sunken")
                self.tileBtn[y][x].config(state="disabled")

        self.gameLossUpdate()
    
    def gameWin(self): #hanterar spelarvinster där alla minor undvikits
        self.stopTimer()

        for y in range(gameInfo.getHeight()):
            for x in range(gameInfo.getWidth()):
                if gameEngine.tileMatrix[y][x] == 10:
                    self.tileBtn[y][x].config(image = self.mineImg, bg='green')
                elif gameEngine.tile[y][x].vicinity == 1:
                    self.tileBtn[y][x].config(image = self.vicinityImg[0])
                elif gameEngine.tile[y][x].vicinity == 2:
                    self.tileBtn[y][x].config(image = self.vicinityImg[1])
                elif gameEngine.tile[y][x].vicinity == 3:
                    self.tileBtn[y][x].config(image = self.vicinityImg[2])
                elif gameEngine.tile[y][x].vicinity == 4:
                    self.tileBtn[y][x].config(image = self.vicinityImg[3])
                elif gameEngine.tile[y][x].vicinity == 5:
                    self.tileBtn[y][x].config(image = self.vicinityImg[4])
                elif gameEngine.tile[y][x].vicinity == 6:
                    self.tileBtn[y][x].config(image = self.vicinityImg[5])
                elif gameEngine.tile[y][x].vicinity == 7:
                    self.tileBtn[y][x].config(image = self.vicinityImg[6])
                elif gameEngine.tile[y][x].vicinity == 8:
                    self.tileBtn[y][x].config(image = self.vicinityImg[7])
                else: self.tileBtn[y][x].config(image = self.clickedImg)

                self.tileBtn[y][x].config(relief="sunken")
                self.tileBtn[y][x].config(state="disabled")
                
        self.calcScore()
        self.gameWinUpdate()
    
    def stopTimer(self): #stoppar tidtagarur
        self.end = time.time()
        self.timeToggle = False
     
    def calcScore(self): #räknar ut nytt resultat
        self.score = int(((self.leftClicks*(self.end-self.start))/(gameInfo.getHeight()*gameInfo.getWidth()))*1000)
        print(self.score)

    def gameLossUpdate(self):
        """self.lossText1.grid( = Label(self.master, text= "Oh no, you stepped on a mine! Game over!")
        self.lossText2 = Label(self.master, text= "Do you want to return to main menu or quit?")
        self.winText1 = Label(self.master, text= "Congratulations, you found all mines!")
        self.scoreText1 = Label(self.master, text= "You scored " + str(self.score) + "!")
        self.scoreText2 = Label(self.master, text= "Your score of " + str(self.score) + " managed you a spot on the leaderboar!")
        self.highScoreText = Label(self.master, text= "Your score of " + str(self.score) " got you the High Score!!!")
        self.mainMenuBtn = Button(self.master, text="Main menu")
        self.leaderBoardBtn = Button(self.master, text="Leaderboard")
        self.quitBtn = Button(self.master, text= "Quit game")"""
        None
        
    def gameWinUpdate(self):
        None
    
    def returnMainMenu(self): #hanterar omstarter
        self.newMenuWindow = Toplevel(self.master)
        self.app = MenuWindow(self.newMenuWindow)
        self.master.withdraw()

    def returnLeaderBoard(self):
        self.newScoreWindow = Toplevel(self.master)
        self.app = ScoreWindow(self.newScoreWindow)
        self.master.withdraw()

    def quitGame(self):
        quit()

class Tile:

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.vicinity = 0
        self.mine = False
        self.clicked = False
        self.flagged = False 

class Engine:

    def __init__(self):

        self.mineCount = 0
        
        self.tileMatrix = [[0 for x in range(gameInfo.getWidth())] for y in range(gameInfo.getHeight())]

        self.tile = [[None for x in range(gameInfo.getWidth())] for y in range(gameInfo.getHeight())]

        for tileRow in range(gameInfo.getHeight()): 
            for tileColumn in range(gameInfo.getWidth()):
                self.tile[tileRow][tileColumn] = Tile(tileRow, tileColumn)

    def placeMines(self):

        y = random.randint(0, gameInfo.getHeight()-1)
        x = random.randint(0, gameInfo.getWidth()-1)

        if self.tileMatrix[y][x]==10:
            self.placeMines()
        else: self.mineCount += 1
        
        self.tileMatrix[y][x] = 10
        self.tile[y][x].mine = True

        if self.mineCount < gameInfo.getNOM():
            self.placeMines()

    def applyVicinity(self):
        
        for y in range(1, gameInfo.getHeight()-1):       #checks vicinity of tiles with eight surrounding tiles 
            for x in range(1, gameInfo.getWidth()-1):
                self.vicinityCount = 0

                if self.tileMatrix[y][x] != 10:
                    if self.tileMatrix[y-1][x-1] == 10:
                        self.vicinityCount += 1
                    if self.tileMatrix[y-1][x] == 10:
                        self.vicinityCount += 1
                    if self.tileMatrix[y-1][x+1] == 10:
                        self.vicinityCount += 1
                    if self.tileMatrix[y][x-1] == 10:
                        self.vicinityCount += 1
                    if self.tileMatrix[y][x+1] == 10:
                        self.vicinityCount += 1
                    if self.tileMatrix[y+1][x-1] == 10:
                        self.vicinityCount += 1
                    if self.tileMatrix[y+1][x] == 10:
                        self.vicinityCount += 1
                    if self.tileMatrix[y+1][x+1] == 10:
                        self.vicinityCount += 1

                    self.tileMatrix[y][x] = self.vicinityCount 
                    self.tile[y][x].vicinity = self.vicinityCount
                    
                else: None

        for x in range(1, gameInfo.getWidth()-1):       #checks vicinity of first row 
            self.vicinityCount = 0
            y = 0

            if self.tileMatrix[y][x] != 10:
                if self.tileMatrix[y][x-1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y+1][x-1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y+1][x] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y+1][x+1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y][x+1] == 10:
                    self.vicinityCount += 1

                self.tileMatrix[y][x] = self.vicinityCount 
                self.tile[y][x].vicinity = self.vicinityCount
                    
            else: None

        for x in range(1, gameInfo.getWidth()-1):       #checks vicinity of last row
            self.vicinityCount = 0
            y = gameInfo.getHeight()-1

            if self.tileMatrix[y][x] != 10:
                if self.tileMatrix[y][x-1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y-1][x-1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y-1][x] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y-1][x+1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y][x+1] == 10:
                    self.vicinityCount += 1

                self.tileMatrix[y][x] = self.vicinityCount 
                self.tile[y][x].vicinity = self.vicinityCount
                    
            else: None

        for y in range(1, gameInfo.getHeight()-1):      #checks vicinity of first column
            self.vicinityCount = 0
            x = 0

            if self.tileMatrix[y][x] != 10:
                if self.tileMatrix[y-1][x] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y-1][x+1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y][x+1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y+1][x+1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y+1][x] == 10:
                    self.vicinityCount += 1

                self.tileMatrix[y][x] = self.vicinityCount 
                self.tile[y][x].vicinity = self.vicinityCount
                    
            else: None

        for y in range(1, gameInfo.getHeight()-1):      #checks vicinity of last column
            self.vicinityCount = 0
            x = gameInfo.getWidth()-1

            if self.tileMatrix[y][x] != 10:
                if self.tileMatrix[y-1][x] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y-1][x-1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y][x-1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y+1][x-1] == 10:
                    self.vicinityCount += 1
                if self.tileMatrix[y+1][x] == 10:
                    self.vicinityCount += 1

                self.tileMatrix[y][x] = self.vicinityCount 
                self.tile[y][x].vicinity = self.vicinityCount
                    
            else: None

        if self.tileMatrix[0][0] != 10:     #checks vicinity of top left tile
            self.vicinityCount = 0

            if self.tileMatrix[0][1] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[1][1] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[1][0] == 10:
                self.vicinityCount += 1

            self.tileMatrix[0][0] = self.vicinityCount 
            self.tile[0][0].vicinity = self.vicinityCount

        else: None

        if self.tileMatrix[0][gameInfo.getWidth()-1] != 10:    #checks vicinity of top right tile
            self.vicinityCount = 0

            if self.tileMatrix[0][gameInfo.getWidth()-2] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[1][gameInfo.getWidth()-2] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[1][gameInfo.getWidth()-1] == 10:
                self.vicinityCount += 1

            self.tileMatrix[0][gameInfo.getWidth()-1] = self.vicinityCount 
            self.tile[0][gameInfo.getWidth()-1].vicinity = self.vicinityCount

        else: None

        if self.tileMatrix[gameInfo.getHeight()-1][0] != 10:    #checks vicinity of bottom left tile
            self.vicinityCount = 0

            if self.tileMatrix[gameInfo.getHeight()-2][0] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[gameInfo.getHeight()-2][1] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[gameInfo.getHeight()-1][1] == 10:
                self.vicinityCount += 1

            self.tileMatrix[gameInfo.getHeight()-1][0] = self.vicinityCount 
            self.tile[gameInfo.getHeight()-1][0].vicinity = self.vicinityCount

        else: None

        if self.tileMatrix[gameInfo.getHeight()-1][gameInfo.getWidth()-1] != 10:    #checks vicinity of bottom right tile
            self.vicinityCount = 0

            if self.tileMatrix[gameInfo.getHeight()-1][gameInfo.getWidth()-2] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[gameInfo.getHeight()-2][gameInfo.getWidth()-2] == 10:
                self.vicinityCount += 1
            if self.tileMatrix[gameInfo.getHeight()-2][gameInfo.getWidth()-1] == 10:
                self.vicinityCount += 1

            self.tileMatrix[gameInfo.getHeight()-1][gameInfo.getWidth()-1] = self.vicinityCount 
            self.tile[gameInfo.getHeight()-1][gameInfo.getWidth()-1].vicinity = self.vicinityCount

        else: None

        for tileList in self.tileMatrix:
                for tile in tileList:
                    print(str(tile).rjust(3), end="")
                print()
        print()

    def checkClicked (self, y, x):
        return self.tile[y][x].clicked
    
    def examineTile(self, y, x): #hanterar undersökning av specifik ruta

        if self.checkClicked(y,x) == False:
            self.tile[y][x].clicked = True 
        
            if self.tileMatrix[y][x] != 10:
                if self.tile[y][x].vicinity != 0:
                    return self.tile[y][x].vicinity
                
                else: return "open"
            else: return "mine"
        else: None

class GameInfo:

    def __init__(self):
        self.height = None
        self.width = None
        self.numberOfMines = None
        self.name = None

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getNOM(self):
        return self.numberOfMines

    def getName(self):
        return self.name

def readResult(): #läser tidigare resultat från fil
    None
    
def playerName(): #läser användarens inmatning
    name = input("What is your name?")
    return name 
    
def writeResult(result): #skriver nya resultat till fil
    None
    
def main(): #huvudprogrammet som står för alla menyval

    global gameInfo 
    gameInfo = GameInfo()
    
    root = Tk()
    app = MenuWindow(root)
    root.mainloop()    

main()
