from tkinter import *       
from deck import *


def populateOptions(deck):
	root = Tk() 
	leftFrame = Frame(root) 
	middleFrame = Frame(root) 
	rightFrame = Frame(root)
	leftFrame.pack(side=LEFT)
	middleFrame.pack(side=BOTTOM)
	rightFrame.pack(side=RIGHT)

	root.title("Deck-U-Lator")
	scrollbarLeft = Scrollbar(leftFrame) 
	scrollbarLeft.pack( side = LEFT, fill = Y ) 
	mylistLeft = Listbox(root, yscrollcommand = scrollbarLeft.set ) 
	scrollbarRight = Scrollbar(rightFrame)
	scrollbarRight.pack( side = RIGHT, fill = Y )
	mylistRight = Listbox(root, yscrollcommand = scrollbarLeft.set )
	scrollbarRight.config( command = mylistRight.yview )

	for card in deck.getCardNames(): 
		mylistLeft.insert(END, card) 
		mylistLeft.pack( side = LEFT, fill = BOTH ) 
		scrollbarLeft.config( command = mylistLeft.yview )
	def addToRight():
		selected = mylistLeft.get('active')
		mylistRight.insert(END, selected) 
		mylistRight.pack( side = LEFT, fill = BOTH ) 
		scrollbarLeft.config( command = mylistLeft.yview )
	def removeFromRight():
		selected = mylistRight.get('active')
		mylistRight.delete('active')

	add = Button(middleFrame, text='Add', width=25, command=addToRight) 
	add.pack(side=LEFT)
	remove = Button(middleFrame, text='Remove', width=25, command=removeFromRight) 
	remove.pack(side=LEFT)


	w = Spinbox(middleFrame, from_ = 0, to = deck.cardsInDeck())
	w.pack()


	mainloop() 