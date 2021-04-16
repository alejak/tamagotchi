# -*- coding: latin-1 -*-
#
#    Ett program som fixar med en kodbok så att man kan 
#    hålla reda på sina koder i en fil. Det är inte
#    krypterat så man kan tjuvläsa, men det skall jag
#    fixa i nästa version.
#

import sys
class CodeBook(object):

   # Skapa en kodbok med samma innehåll som filen
   def __init__(self,filename):
       self.data =[] # Här lagras alla koder (objekt av klassen Code)
       f=open("KodBok.txt","r",encoding="latin1")
       self.accessCode =int(f.readline().strip()) # Här lagras kodbokens hemliga nycken.
       
       while True:
           namn = f.readline().strip()
           if namn =="":
               break
           kod = int(f.readline())
           c = Code(kod, namn)
           self.addCode(c)
      
       f.close()
   

   #Lagra hela kodboken på en fil
   def save(self,filename):
       f=open("KodBok.txt","w")
       f.write(str(self.accessCode))
       for c in self.data:
           f.write("\n")
           f.write(c.getName()+"\n")
           f.write(str(c.getCode()))
       f.close()
   

   # Kolla om koden är rätt.
   def checkCode(self,accessCode):
       return self.accessCode == accessCode
   

   # Lägg till en ny kod.
   def addCode(self,myCode):
      self.data.append(myCode)
   

   # Slå upp en kod. Om koden saknas eller om accesskoden är
   # fel så returneras 0.
   def getCode(self,name,accessCode):
       if self.accessCode == accessCode:
           return self.lookUp(name)
       else:
           return 0
   

   def lookUp(self,name):
      for c in self.data:
         if c.getName()==(name):
            return c.getCode()
        
      return 0


class Code:
    def __init__(self, code,name):
        self.__code = code
        self.__name = name
    
    def getCode(self):
        return self.__code
        
    def getName(self):
        return self.__name




def vaelj_alternativ():
   print( "1: Slå upp en kod")
   print( "2: Lägg till en ny kod")
   print( "3: Avsluta")
   print()

   svar = int(input(">"))
   return svar


def slaaUpp():
    svar = input("Vilken kod söker du?")
    print (c.getCode(svar, huvudKod))

def laeggTill():
    namn=input("Vad gäller kod (textsträng)?")
    kod =int(input("Vad är koden (siffror)?"))
    kaad = Code(kod, namn)
    c.addCode(kaad)


SLAA_UPP = 1
LAEGG_TILL = 2
SLUTA = 3

c = CodeBook("CodeBook.txt")
print ("Välkommen till kodboken 'CodeBook.txt'")
svar=int(input("Ange din hemliga kod:"))
huvudKod = int(svar)
if c.checkCode(huvudKod)==False:
    print ("DET VAR FEL! HÅRDDISKEN RADERAS! HAHAHA!")
    sys.exit(0)

val = 0
while val!=SLUTA:
    val=vaelj_alternativ()
    if val == SLAA_UPP:
        slaaUpp()
    elif val == LAEGG_TILL:
        laeggTill()
c.save("CodeBook.txt")
print ("Ha en bra dag!")


