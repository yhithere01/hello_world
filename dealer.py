import blackjack

deck = blackjack.Deck()

dealer = blackjack.Player(blackjack.deal_card(deck), blackjack.deal_card(deck))


# Dealer, one card hidden; hits under certain cases
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


dealer_turn(dealer, deck)
