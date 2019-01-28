from deck import *
from tools import *
from graphical import *
def main():
	print("Make empty Deck")
	deck = MyDeck()
	print("Read list")
	temp = importDeck()
	print("Load list") 
	deck.importFile(temp)
	print("Here is the deck")
	print(str(deck))
	print("Here is the deck")
	print(str(deck))
	populateOptions(deck)
main()