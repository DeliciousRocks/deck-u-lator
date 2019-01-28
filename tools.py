from tkinter import Tk
from tkinter.filedialog import askopenfilename
from deck import *

supported = [".dck",".dec"]

def importDeck():
    #print("Import Deck")
    #Tk().withdraw()
    fileName = "C:/Users/walte/Downloads/Heartless Retrival 3-12.dec"#askopenfilename()
    print(fileName)
    file = open(fileName, "r")
    extention = fileName[len(fileName)-4:len(fileName)]
    print(fileName) 
    if extention in supported:
        if(extention==".dck"):
            return parseDck(file)
        elif(extention==".dec"):
            return parseDec(file)
    else:
        print("Unsupported File Type --- Accepted types are:")
        for fileType in supported:
            print(fileType)
def parseDck(file):
    line = file.readline() #Get deck name out of the way
    deck = []
    while(line):
        line = file.readline()
        if(line[0]!="L"):
            number = line[0:line.find("[")-1]
            cardName = line[line.find("]")+2:len(line)-1]
            card = MyCard(cardName)
            card.number = int(number)
            #print(card)
            deck.append(card)    
            return deck
def parseDec(file):
    print("Parse Dec")
    line = file.readline()   
    deck = []
    while(line):
        line = file.readline()
        if(line[0]!="/"):
            if(line[0]=="S"):
                line = None
            else:
                number = line[0:line.find(" ")]
                cardName = line[line.find(" ")+1:len(line)-1]
                card = MyCard(cardName)
                card.number = int(number)
                #print(card)
                deck.append(card)
    #print(deck)
    print("Exiting") 
    return deck
def factorial(number):
    if(number ==0):
        return 1
    else:
        return number * factorial(number-1)
def binomialCoefficient(N,n):
    return (factorial(N)/((factorial(n)*factorial(N-n))))
