import random

BLACKJACK = 21
DEALER_MUST_STAY = 17

DECK_FULL = [
    2, 2, 2, 2,
    3, 3, 3, 3, 
    4, 4, 4, 4, 
    5, 5, 5, 5, 
    6, 6, 6, 6, 
    7, 7, 7, 7, 
    8, 8, 8, 8, 
    9, 9, 9, 9, 
    10, 10, 10, 10,
    "Jack", "Jack", "Jack", "Jack",
    "Queen", "Queen", "Queen", "Queen",
    "King", "King", "King", "King",
    "Ace", "Ace", "Ace", "Ace", "Ace"
]

class Hand:

    cards = []
    bust = False
    twentyone = False

    def __init__(self, cards, name):
        if isinstance(cards, list):
            for card in cards:
                if card in DECK_FULL:
                    self.cards = cards  
        else:
            if cards in DECK_FULL:
                self.cards = [cards]

        self.name = name

    def hit(self,deck):
        card = random.choice(deck)
        self.cards.append(card)
        deck.remove(card)

    def total(self):
        numAces = 0
        total = 0
        for card in self.cards:
            try:
                total = total + card
            except:
                if card == "Ace":
                    total = total + 11
                    numAces = numAces + 1
                else:
                    total = total + 10
            
        while(total > 21 and numAces > 0):
            total = total - 10
            numAces = numAces - 1

        return total
    
    def result(self):
        if self.total() > BLACKJACK:
            self.bust = True
            return "Bust!"
        elif self.total() == BLACKJACK:
            self.twentyone = True
            return "Blackjack!"
        else:
             return f"Your final hand is worth {self.total()}"

    def show(self):
        if len(self.cards) == 0:
            print(f"{self.name}, you do not have a hand")
        else:
            print(f"{self.name}, your current hand is:")
            for card in self.cards:
                print(f"[{card}]", end=" ")
            print()

class Dealer(Hand):
    def get_shown(self):
        try:
            return self.cards[1]
        except:
            pass
    
    def play(self, deck):
        self.show()
        while self.total() < DEALER_MUST_STAY:
            self.hit(deck)
            self.show()


def first_deal_players(deck, num_players):
    hands = []
    for i in range(1, num_players + 1):
        card1 = random.choice(deck)
        deck.remove(card1)
        card2 = random.choice(deck)
        deck.remove(card2)
        name = input(f"Player {i}'s name? ")
        hands.append(Hand([card1, card2], name))
    return hands

def first_deal_dealer(deck):
    card1 = random.choice(deck)
    deck.remove(card1)
    card2 = random.choice(deck)
    deck.remove(card2)
    return Dealer([card1, card2], "Dealer")



game = input("Do you want to play a game of BlackJack? [Y/N]: ")
while (game.upper() != "Y" and game.upper() !="N"):
    game = input("I don't understand. Do you want to play a game of BlackJack? [Y/N]: ")

while(game.upper() == "Y"):
    WINNERS = []
    DECK = DECK_FULL

    num_players = 0
    while(num_players <= 0):
        try:
            num_players = int(input("How many players? " ))
        except:
            print("I don't understand.")
        if num_players <= 0:
            print("Please type a positive number.")

    PLAYERS_HANDS = first_deal_players(DECK, num_players)
    DEALER_HAND = first_deal_dealer(DECK)

    print(f"Dealer is showing [{DEALER_HAND.get_shown()}]")

    for player in PLAYERS_HANDS:
        player.show()
        while player.total() < 21:
            hit = input("Hit or pass? [H/P]: ")
            if hit.upper() == "H":
                player.hit(DECK)
                player.show()
            elif hit.upper() == "P":
                break
            else:
                print("I don't understand.")

        if player.twentyone:
            print("Blackjack!")
            WINNERS.append(player.name)

        print(player.result())

    DEALER_HAND.play(DECK)
    print(DEALER_HAND.result())

    for player in PLAYERS_HANDS:
        if player not in WINNERS and not player.bust:
            if DEALER_HAND.total() > 21:
                WINNERS.append(player)
            elif player.total() > DEALER_HAND.total():
                WINNERS.append(player)
    if len(WINNERS) == 0:
        print("No one wins!")
    else:
        print("Winners: ")
        for winner in WINNERS:
            print(f"{winner.name}!")

    game = input("Play again? [Y/N]: ")
    while (game.upper() != "Y" and game.upper() !="N"):
        game = input("I don't understand. Do you want to play another game of BlackJack? [Y/N]: ")


print("Goodbye!")

'''
test = Hand(["Ace", "Ace", "Ace", "Ace"], "test")
print(test.total())
'''