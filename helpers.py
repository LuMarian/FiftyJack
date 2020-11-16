from cardstack import card


# checking if any player has won, returns "no" if no winner yet, otherwise it returns "user", "blackjack", "dealer" or "tied"
def check_winner_after_deal(user, dealer):
    # if user has blackjack with two cards
    if user.handvalue == 21:
        # player ties blackjacks with dealer
        if dealer.handvalue == 21:
            user.wins(False, True)
            return "tied"
        # player wins with a blackjack
        else:
            user.wins(True)
            return "blackjack"
    elif dealer.handvalue == 21:
        return "dealerblackjack"
    else:
        return "no"

def check_winner(user, dealer):
    if dealer.handvalue > 21:
        user.wins()
        return "toomuchdealer"
    elif dealer.handvalue == user.handvalue:
        user.wins(False, True)
        return "tied"
    elif dealer.handvalue < user.handvalue:
        user.wins()
        return "user"
    elif dealer.handvalue > user.handvalue:
        return "dealer"

# calculate chips to be displayed
def chips_calculate(chips, bet):
    while bet > 0:
        for x in [10, 5, 1]:
            if x <= bet:
                chips.append(x)
                bet -= x
                break
    return
    
