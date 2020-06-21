#Ferhat Ali Tokuc 20180702071 (FATACADEMY)
from random import shuffle

# Deck class, which has an initially empty
# deck and methods to manipulate the deck.
class UnoDeck():
    def __init__(self):
        self.deck = []

    def addCard(self, c):   # Adds a card to top of the deck.
        self.deck.append(c)

    def shuffleDeck(self):   # Shuffles the deck.
        shuffle(self.deck)

    def getNumCards(self):   # How many cards in the deck?
        return len(self.deck)

    def getTopCard(self):           # Only returns the top card in the deck.
        if (len(self.deck) > 0):    # Useless here but it was given in the assigment pdf( ı just followed the Sezer Hoca's rules)
            return self.deck[-1]

    def canPlay(self, c):               # Returns true if a playable card exists in the deck.
        c_color, c_num = c.split(',')   # Returns false if not exists.

        for card in self.deck:
            color, num = card.split(',')
            if (color == c_color or num == c_num):
                return True
        return False

    def getCard(self, index):   # Removes and returns the card in the given index. 
        return self.deck.pop(index)

    def findCard(self, c):   # Returns the index of the given card. (Assuming it exists in the deck.)
        c_color, c_num = c.split(',')

        for i, card in enumerate(self.deck):   # enumerate() indexes and iterates through a list.
            color, num = card.split(',')
            if (color == c_color or num == c_num):
                return i

deck = UnoDeck()
hand1 = UnoDeck()
hand2 = UnoDeck()

lastPlayedCard = ""

colors = ["Yellow", "Red", "Green", "Blue"]

for color in colors:   # Putting all the cards in the deck.
    for i in range(1,10):
        card = color + "," + str(i)
        deck.addCard(card)
        deck.addCard(card)

deck.shuffleDeck()

for i in range(7):   # Distributing 7 cards to players.
    card = deck.getCard(0)
    hand1.addCard(card)
    card = deck.getCard(0)
    hand2.addCard(card)

# The game begins.
lastPlayedCard = hand1.getCard(0)
print("Player 1's turn: ", lastPlayedCard)

while(True):
    if(hand2.getNumCards() > 0):
        if(hand2.canPlay(lastPlayedCard)):   # If the player 2 has any suitable card.
            cardIndex = hand2.findCard(lastPlayedCard)   # Find the index of the suitable card.
            lastPlayedCard = hand2.getCard(cardIndex)   # Return the suitable card and remove it from the hand of player 2.
            print("Player 2's turn: ", lastPlayedCard)
        else:
            if(deck.getNumCards() > 0):   # If there are any cards to draw.
                topOfDeck = deck.getCard(-1) # Remove the card from top of the deck.
                hand2.addCard(topOfDeck) # Add the card to player 2.
                print("Player 2 draws a card from the deck!")
            else:
                print("Game is a tie! #FATACADEMY")
                break
    else:
        print("Player 2 won! #FATACADEMY")
        break

    if(hand1.getNumCards() > 0):
        if(hand1.canPlay(lastPlayedCard)):    # If there are any cards in player 2's deck.
            cardIndex = hand1.findCard(lastPlayedCard)   # Find the index of the suitable card.
            lastPlayedCard = hand1.getCard(cardIndex)   # Return the suitable card and remove it from the hand of player 2.
            print("Player 1's turn: ", lastPlayedCard)
        else:
            if(deck.getNumCards() > 0):   # If there are any cards to draw.
                topOfDeck = deck.getCard(-1)   # Remove the card from top of the deck.
                hand1.addCard(topOfDeck)   # Add the card to player 2.
                print("Player 1 draws a card from the deck!")
            else:
                print("Game is a tie! #FATACADEMY")
                break
    else:
        print("Player 1 won! #FATACADEMY")
        break
#Thanks to Sezer Hoca , stackoverflow, forums, youtube and indian people