exempt = ["Plains","Island","Swamp","Mountain","Forest"] #Cards not restricted to 4 of
class MyDeck:
    def __init__(self):
        self.cards = []
    def __str__(self):
        deck = ""
        temp = []
        temp.extend(self.cards)
        while(len(temp)>0):
            card = temp.pop() 
            #print(card)
            deck = deck + str(card) +" : " + str(card.number) + "\n"
        return deck
    def cardsInDeck(self):
        count = 0
        for card in self.cards:
            count = count + card.number
        #print(count)
        return count
    def numberOfCardInDeck(self,search):
        temp = []
        temp.extend(self.cards)
        while(len(temp)>0):
            card = temp.pop() 
            if(card.name==search):
                return card.number
        return 0
    def addCard(self,card):
        if (self.cards.count(card)==0):
            card.number=1
            self.cards.append(card)
            #print(card)
            print("Added "+str(card))
        else:
            holding =self.cards.pop(self.cards.index(card))
            if (holding.number <4 or holding.name in exempt):
                holding.number+=1
                print("Added "+str(card))
            else:
                print("Attempting to add fifth copy of "+str(card))
            self.cards.append(holding)
    def importFile(self,deckList):
        if deckList is not None:
            #print("Not None")
            for uniqueCard in deckList:
                print(uniqueCard.number)
                for x in range(uniqueCard.number):
                    self.addCard(uniqueCard)
    def getCardNames(self):
        cardNames =[]
        temp = []
        temp.extend(self.cards)
        while(len(temp)>0):
            card = temp.pop()
            cardNames.append(str(card))
        return cardNames 
class MyCard:
    def __init__(self,n):
        self.name = n
        self.number = 0
    def __str__(self):
        return self.name
class MyHand:
    def __init__(self,deck):
        self.source=deck
