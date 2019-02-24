import random
import os
import pygame
import backend

class Card:
	#KONSTRUKTOR
	def __init__(self, number, symbol, location=(300,500)):
		self.number = number
		self.symbol = symbol
		self.location = location

	#GETTER
	def getLocationX(self):
		return self.location[0]
	def getLocationY(self):
		return self.location[1]
	def getLocation(self):
		return self.location
	def getNumber(self):
		return self.number
	def getSymbol(self) :
		return self.symbol

	#SETTER
	def setLocation(self, x, y):
		self.location = (x,y)

	def setLocationInit(self):
		self.location = (300,500)

	#FUNCTION
	def showLocation(self):
		print("({},{})".format(self.location[0],self.location[1]))

class Deck:
	#KONSTRUKTOR
	def __init__(self):
		self.deck = []
		for number in range(1,14):
			for symbol in range(1,5):
				card = Card(number, symbol)
				self.deck.append(card)

		random.shuffle(self.deck)

	def addCard(self, card):
		self.deck.append(card)

	def throwCard(self, i):
		self.deck.pop(i)

	def getCardNumber(self, i):
		return self.deck[i].getNumber()

	def getCardSymbol(self, i):
		return self.deck[i].getSymbol()

	def getCardLocation(self, i):
		return self.deck[i].getLocation()

	def setLocationInit(self):
		for card in self.deck:
			card.setLocationInit()

	def showDeck(self):
		for card in self.deck: 
			if card.getSymbol() == 1:
				print("{} {}".format("Heart", card.getNumber()))
			elif card.getSymbol() == 2:
				print("{} {}".format("Club", card.getNumber()))
			elif card.getSymbol() == 3:
				print("{} {}".format("Spade", card.getNumber()))
			elif card.getSymbol() == 4:
				print("{} {}".format("Diamond", card.getNumber()))

#INIT GAME
pygame.init() #inisialisasi modul pygame

#GAME LIBRARY
green = (0, 204, 0)
white = (255,255,255) #(R,G,B)
black = (0,0,0)
tosca = (0, 255, 153)
red = (255,0,0)
display_width = 800
display_height = 600

#GRAPHIC LIBRARY
font = pygame.font.SysFont("raleway", 25, True)
fontBig = pygame.font.SysFont("raleway", 40, True)
cardImage = pygame.image.load(os.path.join("img","card.png"))
bg = pygame.image.load(os.path.join("img","table.jpg"))
bgStart = pygame.image.load(os.path.join("img","bgStart.jpg"))
buttonNext = pygame.image.load(os.path.join("img", "button_next.png"))
buttonExit = pygame.image.load(os.path.join("img", "button_exit.png"))
fotoTim = pygame.image.load(os.path.join("img", "Ashiaaap.jpg"))
hati = []
for i in range(13):
	hati.append(pygame.image.load(os.path.join("img/Hati",str(i+1) + "H.png")))
keriting = []
for i in range(13):
	keriting.append(pygame.image.load(os.path.join("img/Keriting", str(i+1) + "K.png")))
sekop = []
for i in range(13):
	sekop.append(pygame.image.load(os.path.join("img/Sekop", str(i+1) + "S.png")))
wajik = []
for i in range(13):
	wajik.append(pygame.image.load(os.path.join("img/Wajik", str(i+1) + "W.png")))

#USEFUL FUNCTION
def animateDrawCard(Deck, final_location):
	if (len(Deck.deck) <= 9):
		n = len(Deck.deck)-1
	else:
		n = 9

	same = True
	while (n >=0 and same):
		if Deck.deck[n].getLocationX() < final_location[n][0]:
			Deck.deck[n].setLocation(Deck.deck[n].getLocationX()+10, Deck.deck[n].getLocationY())
		elif Deck.deck[n].getLocationX() > final_location[n][0]:
			Deck.deck[n].setLocation(Deck.deck[n].getLocationX()-10, Deck.deck[n].getLocationY())

		if Deck.deck[n].getLocationY() < final_location[n][1]:
			Deck.deck[n].setLocation(Deck.deck[n].getLocationX(), Deck.deck[n].getLocationY()+10)
		elif Deck.deck[n].getLocationY() > final_location[n][1]:
			Deck.deck[n].setLocation(Deck.deck[n].getLocationX(), Deck.deck[n].getLocationY()-10)

		if (Deck.deck[n].getLocation()==final_location[n]):
			n-=1
		else:
			same = False

def AreaValid(mouseLocation,i):
	return mouseLocation[0] >= i[0] and mouseLocation[0] <= i[0]+100 and mouseLocation[1] >= i[1] and mouseLocation[1] <= i[1] + 150

def PickValid(choosenCard, idx):
	i = 0
	while(i < len(choosenCard)):
		if choosenCard[i] == idx:
			return False
		else:
			i+=1

	return True

def credits():
	gameDisplay.fill(black)
	text1 = font.render("Ashiaaap Team", True, white)
	text2 = font.render("Mgs. Muhammad Riandi Ramadhan 13517080", True, white)
	text3 = font.render("Muhamamad Fikri Hizbullah 13517104", True, white)
	text4 = font.render("M.Algah Fattah Illahi 13517122", True, white)

	gameDisplay.blit(fotoTim, (200,50))
	gameDisplay.blit(text1, (250, 300))
	gameDisplay.blit(text2, (150, 350))
	gameDisplay.blit(text3, (150, 400))
	gameDisplay.blit(text4, (150, 450))

	pygame.display.update()
	pygame.time.delay(5000)

#SETTING SURFACE
gameDisplay = pygame.display.set_mode((display_width,display_height)) #surface
pygame.display.set_caption('24 Game') #judul

#MAIN LOOP
def gameLoop():
	gameExit = False
	deck = Deck()
	choosenCard = []

	final_location = [(50,300),(200,300),(350,300),(500,300),(650,300),
						(50,100),(200,100),(350,100),(500,100),(650,100)]

	while not gameExit:
		mouseLocation = (0,0)
		#EVENT GETTER
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouseLocation = event.pos

		#DRAWING SECTION
		gameDisplay.blit(bg, (0,0)) #background
		text = font.render("PICK 4 CARDS", True, white)
		gameDisplay.blit(text, (300,50))
		numberCardDeck = font.render("Cards in Deck : " + str(len(deck.deck)), True, white)
		gameDisplay.blit(numberCardDeck, (300, 550))

		#CHOOSING CARD HANDLER
		idx = 0
		for card in deck.deck:
			if (idx <= 9):
				gameDisplay.blit(cardImage, card.getLocation())
				if len(choosenCard) < 4:
					if AreaValid(mouseLocation, card.getLocation()): #kalau ada daerah yang kepencet
						if PickValid(choosenCard, idx): #memastika kartu yang dipilih kartu yang belum dibuka
							choosenCard.append(idx)	
				idx+=1				
				

		#FLIPPING CARD
		if (len(choosenCard) >= 1 and len(choosenCard) <= 4):
			for i in choosenCard:
				if deck.getCardSymbol(i) == 1:
					gameDisplay.blit(hati[deck.getCardNumber(i)-1], deck.getCardLocation(i))
				elif deck.getCardSymbol(i) == 2:
					gameDisplay.blit(keriting[deck.getCardNumber(i)-1], deck.getCardLocation(i))
				elif deck.getCardSymbol(i) == 3:
					gameDisplay.blit(sekop[deck.getCardNumber(i)-1], deck.getCardLocation(i))
				elif deck.getCardSymbol(i) == 4:
					gameDisplay.blit(wajik[deck.getCardNumber(i)-1], deck.getCardLocation(i))

		#SOLVER
		if (len(choosenCard) == 4):
			number = []
			for i in choosenCard:
				number.append(str(deck.getCardNumber(i)))

			for i in choosenCard:
				deck.throwCard(i)

			solve = backend.solving(number)
			textSolve = fontBig.render(solve, True, white)
			gameDisplay.blit(textSolve, (250,500))
			#NEXT CARD? EXIT?
			Clicked = False
			while not Clicked:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						gameExit = True
						Clicked = True
					if event.type == pygame.MOUSEBUTTONDOWN:
						mouseLocation = event.pos

				gameDisplay.blit(buttonNext, (570,500))
				gameDisplay.blit(buttonExit, (50,500))
				pygame.display.update()

				if mouseLocation[0] >= 550 and mouseLocation[0] <= 725 and mouseLocation[1] >= 500 and mouseLocation[1] <= 565:
					#NEXT
					choosenCard = []
					deck.setLocationInit()
					Clicked = True
				elif mouseLocation[0] >= 50 and mouseLocation[0] <= 225 and mouseLocation[1] >= 500 and mouseLocation[1] <= 565:
					#EXIT
					gameExit = True
					Clicked = True

				if len(deck.deck) == 0:
					gameExit = True
					Clicked = True


		animateDrawCard(deck, final_location)

		#UPDATE FRAME
		pygame.display.update()

	#CREDITS/END GAME
	credits()
	pygame.quit()

def gameStart():
	Start = False
	Quit = False
	while not Start:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				Start = True
				Quit = False
			if event.type == pygame.QUIT:
				Start = True
				Quit = True

		gameDisplay.blit(bgStart, (0,0))
		pygame.display.update()

	if not Quit:
		gameLoop()
	else:
		pygame.quit()


gameStart()