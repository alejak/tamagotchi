"""
Author: Alexander Jakobsen
P-project 181 Teknologtamagotchin
2017-01-17
This programme lets the user control a tamagotchi. Depending on the user input, the tamagotchis size may change.
"""

from tkinter.ttk import *
from tkinter import *

class TamagotchiWindow: #the window containing the tamagotchi
    
    def __init__(self, master):#sets up the contents of the window
        self.master = master
        self.master.title("TeknologTamagotchi")
        
        self.tamagotchi = TamagotchiState()
        self.__currentSize = 0
        
        self.studyButton = Button(self.master, text = "Study", width = "6", command = self.studyCommand)
        self.sleepButton = Button(self.master, text = "Sleep", width = "6", command = self.sleepCommand)
        self.examButton = Button(self.master, text = "Exam", width = "6", command = self.examCommand)
        self.partyButton = Button(self.master, text = "Party", width = "6", command = self.partyCommand)

        self.infoBox = Label(self.master, font=("Palatino Linotype", 9), text = "Welcome to your very own Teknologtamagotchi!")
        
        self.tamagotchiBox = Canvas(self.master,width=500, height=500)
        self.pet = self.tamagotchiBox.create_oval(0, 0, 0, 0, fill="red")
        
        self.studyButton.grid(row=1, column=0)
        self.sleepButton.grid(row=1, column=1)
        self.examButton.grid(row=2, column=0)
        self.partyButton.grid(row=2, column=1)
        self.infoBox.grid(row=3, column=0, columnspan=2)
        self.tamagotchiBox.grid(row=0, column=0, columnspan=2)     


    def studyCommand(self): #makes your tamagotchi study
        self.__currentSize = self.tamagotchi.getSize()
        self.tamagotchi.updateSequenceList(0)
        self.updateInfo()
        
    def sleepCommand(self):#makes your tamagotchi sleep
        self.__currentSize = self.tamagotchi.getSize()
        self.tamagotchi.updateSequenceList(1)
        self.updateInfo()
        
    def examCommand(self):#makes your tamagotchi exam
        self.__currentSize = self.tamagotchi.getSize()
        self.tamagotchi.updateSequenceList(2)
        self.updateInfo()
        
    def partyCommand(self):#makes your tamagotchi party
        self.__currentSize = self.tamagotchi.getSize()
        self.tamagotchi.updateSequenceList(3)
        self.updateInfo()
     
    def updateInfo(self): #updates the infobox and resizes your tamagotchi
        if self.tamagotchi.getSize() > self.__currentSize:
            self.infoBox.config(text= "Yaay! Your Tamagotchi grew to " + str(self.tamagotchi.getSize()) + "!")
            self.__currentSize = self.tamagotchi.getSize()
        elif self.tamagotchi.getSize() < self.__currentSize:
            self.infoBox.config(text= "Naaw! Your Tamagotchi shrunk to " + str(self.tamagotchi.getSize()) + "!")
            self.__currentSize = self.tamagotchi.getSize()
        elif self.tamagotchi.getSize() == self.__currentSize/2:
            self.infoBox.config(text= "Noo! Your Tamagotchi got bored and halved it's size to " + str(self.tamagotchi.getSize()) + "!")
            self.__currentSize = self.tamagotchi.getSize()
        elif self.tamagotchi.getSize() < 1:
            self.infoBox.config(text= "Noo! Your Tamagotchi is almost gone. Try something else!")
            self.__currentSize = self.tamagotchi.getSize()

        self.tamagotchiBox.coords(self.pet,200-self.__currentSize, 200-self.__currentSize, 300+self.__currentSize, 300+self.__currentSize )

    
class TamagotchiState(): #a class where your tamagotchi's size is calculated
     
    def __init__(self):
        self.__size = 100
        self.__currentSequence = [5,5,5]
        self.__posSeq = [[1,2,3],[0,1,2],[0,2,1]]
        self.__negSeq = [[3,1,2],[0,3,2],[3,1,1]]


    def updateSequenceList(self, action):#adds your tamagotchis last action to a list
        self.__currentSequence.append(action)
        self.checkSequence()

    def checkSequence(self):#controls the last 3 entries of the list changes the size of your tamagotchi accordingly 
        seqList = self.__currentSequence
        print(seqList[-3:])

        try:
            if seqList[-3:] in self.__posSeq:
                self.__size += 25
                
            elif seqList[-3:] in self.__negSeq:
                print (seqList[-3:])
                self.__size -= 25
                """
            elif seqList[-3] == 0 and seqList[-2] == 1 and seqList[-1] == 2:
                self.__size += 25
                
            elif seqList[-3] == 0 and seqList[-2] == 2 and seqList[-1] == 1:
                self.__size += 25
                
            elif seqList[-3] == 0 and seqList[-2] == 3 and seqList[-1] == 2:
                self.__size -= 25
                
            elif seqList[-3] == 3 and seqList[-2] == 1 and seqList[-1] == 3:
                self.__size -= 25"""
                
            elif seqList[-3] == seqList[-1] and seqList[-1] == seqList[-2]:
                self.__size = self.__size/2
                
            else: None
            
        except IndexError: None

    def getSize(self):
        return self.__size
    
def main():
    root = Tk()
    app = TamagotchiWindow(root)
    root.mainloop()

main()
