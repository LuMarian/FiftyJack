import random

class card:
    def __init__(self, value, color, cardset): #cardset as to which of the 4 decks it belongs to
        self.value = value
        self.color = color
        self.cardset = cardset
        if value == 1:
            self.truevalue = 11 #aces count as 11, can be deducted in dealer function "drawcard"
        elif value > 10: # J/Q/K each count as 10
            self.truevalue = 10
        else:
            self.truevalue = value

def carddeck(): # creating playing deck of cards
    colors = ["D", "H", "C", "S"] # diamonds, hearts, clubs, spades
    carddeck = []
    for sets in range(4): #4 cardsets
        for col in colors:
            for val in range(13):
                createdcard = card((val+1), col, (sets+1)) # values starting at 1, 1 = ace, 11 = J, 12 = Q, 13 = K
                carddeck.append(createdcard)
    random.shuffle(carddeck)
    return carddeck
# 208 cards, each card posseses value, color and number of cardset
