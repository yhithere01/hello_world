import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
         "Ten", "Jack", "Queen", "King", "Ace")

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}


class Card():
    def __init__(self, suit="Diamonds", rank="Queen"):
        #  suit and rank are strings
        self.suit = suit
        self.rank = rank
        #  value is an integer
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit} with value {self.value}"


class Deck():
    def __init__(self):
        self.card_stack = []
        #  Loops through ranks & suits tuples to fill deck list 52 cards
        for rank in ranks:
            for suit in suits:
                i = Card(suit, rank)
                self.card_stack.append(i)


class Player():
    def __init__(self, card1, card2):
        self.hand_cards = [card1, card2]
        self.total = 0

    def get_total(self):
        self.total = 0
        for card in self.hand_cards:
            self.total += card.value
        return self.total

    def hit(self, new_card):
        self.hand_cards.append(new_card)
        self.total = self.total + new_card.value

    def ace_in_hand(self):
        for card in self.hand_cards:
            if card.rank == "Ace":
                return True
        else:
            return False


#  Finds the ace in hand worth 11 and changes value to 1
def handle_aces(player_hand):
    for card in player_hand.hand_cards:
        if(card.value == 11):
            card.value = 1


#  Uses random int between 0 and 51 to pop card in that position from deck
def deal_card(deck):
    return deck.card_stack.pop(random.randint(0, len(deck.card_stack) - 1))


# Runs the game with the specific player in the argument
def play_hand(player, deck):
    # player represents an instance of the Player class
    while True:
        # EARLY CHECK in case there are two aces before printing scores
        # If equal or greater than 21 and ace is in hand, handles ace
        if player.get_total() > 21 and player.ace_in_hand():
            handle_aces(player)

        # Print relevant information
        print(f"Score: {str(player.get_total())}\n")
        for card in player.hand_cards:
            print(card)

        # If equal to or greater than 21, prints and breaks
        if player.get_total() > 21:
            # Print relevant information
            print("BUST\n")
            player.total = 0
            break

        command = input("hit or pass: ")

        # If person chooses to hit, call "Player" function hit
        if(command == "hit"):
            player.hit(deal_card(deck))
        else:
            break


# Compares the values of the hands of each player and returns the winner
def compare_scores(players):
    # The highest hand
    highscore = 0
    # Which player we are on
    player_counter = 1
    # Which player with the highest player
    winner = 0

    # Compares player totals except dealer and finds the highest hand
#   for player in range(size(players) - 1):
        if player.total > highscore:
            highscore = player.total
            winner = player_counter
        player_counter += 1

    if 
    # If player before the last wins, print player, else dealer
    return f"The best hand is player {winner} with a {highscore} points."


def dealer_turn(player, deck):
    print(f"Revealed card: {player.hand_cards[0]}\n")
    # Logic on deciding whether to hit
    if player.hand_cards[0].value <= 6:
        print("Dealer hits")
        player.hit(blackjack.deal_card(deck))
    else:
        print("Dealer stays")

    # Handles aces before reveal
    if player.get_total() > 21 and player.ace_in_hand():
        blackjack.handle_aces(player)

    # Dealer shows face down card
    print("\nDealer reveals cards:")
    for card in player.hand_cards:
        print(card)

    # Determines if busted
    if player.get_total() > 21:
        # Print relevant information
        print("BUST\n")
    print(player.get_total())
