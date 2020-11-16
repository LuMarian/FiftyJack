class dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.handvalue = 0
        self.chips = 0

    def drawcard(self, card): #adds card to the player
        self.hand.append(card)
        acecount = 0
        self.handvalue = 0
        for x in range(len(self.hand)): #calculates handvalue - Ace = 11 or 1 and J/Q/K (11/12/13) = 10
            cardvalue = self.hand[x].truevalue
            if cardvalue == 11:
                acecount += 1
            self.handvalue += cardvalue
            if self.handvalue > 21 and acecount > 0: #minus 10 hand value if ace counts as 1
                while acecount > 0:
                    self.handvalue -= 10
                    acecount -=1

    def paramReset(self):
        self.hand = []
        self.handvalue = 0
        self.bet = 0
