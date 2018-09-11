import blackjack

deck = blackjack.Deck()

dealer = blackjack.Player(blackjack.deal_card(deck), blackjack.deal_card(deck))


# Processes a human player; dealer remains hidden
while True:
    # Holds all player instances to be used as arguments for functions
    player_pool = []
    # Gets how many players are playing
    number_of_players = input("How many people are playing? ")

    if int(number_of_players) == 0:
        print("Goodbye")
        break

    # Creates specified number of players and appends them to list
    for number in range(int(number_of_players)):
        player_pool.append(blackjack.Player(blackjack.deal_card(deck),
                                            blackjack.deal_card(deck)))

    # For loop goes through the list of players and plays game for each
    for i in range(len(player_pool)):
        print("\nNow playing player " + str(i + 1))

        blackjack.play_hand(player_pool[i], deck)

    # Add in the dealer and play its turn
    player_pool.append(dealer)
    blackjack.dealer_turn(dealer, deck)

    print(blackjack.compare_scores(player_pool))
    break
    