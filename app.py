from flask import Flask, render_template, redirect, request
app = Flask(__name__)

from cardstack import carddeck
from dealer import *
from helpers import check_winner, check_winner_after_deal, chips_calculate
from player import *


# global variables
bet = 0

# player's chip count, set at index.html 
chips = 5

# name placeholder (if someone accesses /game directly)
name = "Tiger Woods" 
winner = ""

# possible actions for player as dict
actions = {
    "card":False,
    "hold":False,
    "double":False,
}

# list of chips to be displayed
chips_display = []

user = player()
dealer = dealer()
deck = carddeck()

@app.route("/", methods = ["GET", "POST"])
    # starting application / opening page
def index():
    # start game and get name & chips amount
    if request.method == "POST":
        # modifiy global variables and redirect to the game
        global name, chips
        name = request.form.get("name")
        chips = float(request.form.get("chips"))
        return redirect("/game")
    else:
        return render_template("index.html")

@app.route("/game", methods=["GET", "POST"])
def game():
    #get access to global actions-dict
    global actions, user, dealer, deck, bet, winner, chips_display
    # render game and ask for bet
    if request.method == "GET":
        # create deck and update properties incl. deleting cards in hand, game options
        global name, chips
        user.name = name
        user.chips = chips
        chips_display = []
        user.paramReset()
        dealer.paramReset()
        actions["card"] = False
        actions["hold"] = False
        actions["double"] = False
        return render_template("game.html", chips=chips_display, user=user, actions=actions, dealer=dealer)
    
    else: #request.method == "POST"
        # if bet has been posted, meaning game starts, then bet is an integer, else (except) it is "None"
        try:
            # set user's bet
            bet = int(request.form.get("bet"))
            user.set_bet(bet)
            # calculate chips to be displayed
            chips_calculate(chips_display, bet)
            # draw first two cards for user and dealer
            for x in range(2):
                user.drawcard(deck[-1])
                deck.pop()
                dealer.drawcard(deck[-1])
                deck.pop()

            # check if any of players has won
            winner = check_winner_after_deal(user, dealer)
            if winner != "no":
                return redirect("/endofgame")

            # choose which actions are available for player
            actions["card"] = True
            actions["hold"] = True
            actions["double"] = True
            
            return render_template("game.html", chips=chips_display, user=user, actions=actions, dealer=dealer)
        
        # if bet has not been posted, instead user has requested another card
        except:
            user.drawcard(deck[-1])
            deck.pop()
            actions["double"] = False
            if user.handvalue > 21:
                winner = "toomuchuser"
                return redirect("/endofgame")
            else:
                return render_template("game.html", chips=chips_display, user=user, actions=actions, dealer=dealer)


@app.route("/hold", methods=["GET", "POST"])
def hold():
    global user, dealer, winner
    # blackjack rules - dealer draws when < 17
    while dealer.handvalue < 17:
        dealer.drawcard(deck[-1])
        deck.pop()
    # when dealer > 18, check winner
    winner = check_winner(user, dealer)
    return redirect("/endofgame")
    

@app.route("/double", methods=["GET", "POST"])
def double():
    global user, bet, winner
    user.drawcard(deck[-1])
    deck.pop()
    #double bet amount
    user.set_bet(bet, True)
    if user.handvalue > 21:
        winner = "toomuchuser"
        return redirect("/endofgame")
    # if user is < 21 then dealer needs to draw his cards
    else:
        return redirect("/hold")

@app.route("/endofgame")
def endofgame():
    global user, dealer, bet, chips, winner, chips_display
    # update user chips to chips after game has ended
    chips = user.chips
    return render_template("endofgame.html", chips=chips_display, winner=winner, bet=bet, user=user, dealer=dealer)