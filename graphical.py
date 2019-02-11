from tkinter import *       
from deck import *
from tools import *



def createGUI(deck):
	def createWildcard():
		def addToWildcard():
			selected = cards.get('active')
			wildcard.insert(END, selected)
			wildcard.grid(row=1,column=1)
		def removeFromWildcard():
			selected = wildcard.get('active')
			wildcard.delete('active')
		def submitWildCard():
			temp = name.get()
			print(temp)
			mylistLeft.insert(END, temp) 
			mylistLeft.grid(row=1,column=0)

		popOut = Tk()
		tempText = StringVar()
		tempText.set("Sample Name")
		
		popOut.title("Add Wildcard")
		cards = Listbox(popOut)
		cards.grid(row=1, column = 0)
		wildcard = Listbox(popOut)
		wildcard.grid(row=1, column = 1)

		for card in deck.getCardNames(): 
			cards.insert(END, card) 
		mylistLeft.grid(row=1,column=0)
		add = Button(popOut, text='Add', width=25, command=addToWildcard) 
		add.grid(row=2, column = 0)
		remove = Button(popOut, text='Remove', width=25, command=removeFromWildcard) 
		remove.grid(row=2, column = 1)
		wildcardName = Label(popOut, text="Wildcard Name:").grid(row=3)
		name = Entry(popOut, textvariable=tempText)
		name.grid(row=3, column=1)
		submit = Button(popOut, text='Submit', width=25, command=submitWildCard ) 
		submit.grid(row=4)
	def populateOptions():
		deck = importDeck()
		#mylistLeft = Listbox()
		#mylistRight = Listbox()
		mylistLeft.delete(0,END)
		mylistRight.delete(0,END)
		loadedDeck.importFile(deck)
		for card in loadedDeck.getCardNames(): 
			mylistLeft.insert(END, card) 
			mylistLeft.grid(row=1,column=0)	
	def addToRight():
		selected = mylistLeft.get('active')
		mylistRight.insert(END, selected)
		mylistRight.grid(row=1,column=1)
	def removeFromRight():
		selected = mylistRight.get('active')
		mylistRight.delete('active')
	def calculate():
		total = 0
		failures = loadedDeck.cardsInDeck()
		successes = []
		current = []
		iterations = 1
		for card in mylistRight.get(0,END):
				temp = loadedDeck.numberOfCardInDeck(card)
				iterations = iterations * temp
				failures = failures - temp
				successes.append(temp)
				current.append(1)
		print(iterations)
		for c in range(iterations):
			runningTotal = 0
			top = 1
			for x in range(len(current)):
				runningTotal = runningTotal + current[x]
				top = top * binomialCoefficient(successes[x],current[x])
			top = top * binomialCoefficient(failures,int(w.get())-runningTotal)
			print("---------")
			bottom = binomialCoefficient(loadedDeck.cardsInDeck(),int(w.get()))
			temp = (top/bottom)
			print(temp)
			if(runningTotal>=0):
				total = total + temp 
			y = 0
			print(c)
			inc = False
			if(c+1<iterations):
				while(not inc):
					if(current[y]+1<5):
						current[y]=current[y]+1
						print("N")
						inc = True
					else:
						current[y]=1
						y = y + 1
						print("Y")
		print(total)
	
	root = Tk()
	menu = Menu(root) 
	root.config(menu=menu)
	filemenu = Menu(menu)
	loadedDeck = MyDeck()

	root.title("Deck-U-Lator")
	menu.add_cascade(label="Options", menu= filemenu)
	filemenu.add_command(label="Import Deck",command=populateOptions)
	filemenu.add_command(label="New Wild Card", command=createWildcard)

	mylistLeft = Listbox()
	mylistLeft.grid(row=1, column = 0)
	mylistRight = Listbox()
	mylistRight.grid(row=1, column = 1)

	add = Button( text='Add', width=25, command=addToRight) 
	add.grid(row=2, column = 0)
	remove = Button( text='Remove', width=25, command=removeFromRight) 
	remove.grid(row=2, column = 1)

	Label(root,text = "Card to Draw").grid(row=3)
	w = Spinbox( from_ = 0, to = deck.cardsInDeck())
	w.grid(row=3, column =1)

	calculate = Button(text="Calculate",width=25, command=calculate)
	calculate.grid(row=4)

	mainloop() 


	

