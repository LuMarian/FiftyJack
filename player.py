from dealer import dealer

class player(dealer):
    def __init__(self, name = "no_name", chips = 10):
        dealer.__init__(self)
        self.name = name
        self.chips = float(chips)

    def set_bet(self, bet, double = False):
        if double is False:
            self.bet = bet
            self.chips -= bet
        if double is True:
            self.bet *= 2
            self.chips -= bet

    def wins(self, blackjack = False, tie = False): #blackjack parameter for chips calculation
        if blackjack is True:
            self.chips += self.bet * 2.5
        elif tie is True:
            self.chips += self.bet
        else:
            self.chips += self.bet * 2
        # if blackjack = True, player gets 2,5 times his bet
