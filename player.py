class Player:
    def __init__(self, name, id) -> None:
        self.hand = []
        self.turn = False
        self.id = id
        self.name = name

    def get_hand(self):
        return self.hand
    
    def is_turn(self):
        return self.turn
    
    def become_turn(self):
        self.turn = True
    
    def end_turn(self):
        self.turn = False
    
    def play_card(self, card, top_discard_card):
        if card in self.get_playable_cards(top_discard_card):
            card.play_card()
            self.hand.remove(card)
            return True
        return False
    
    def draw_card_from_deck(self, deck):
        card = deck.draw_card()
        self.hand.append(card)

    def get_playable_cards(self, top_discard_card):
        playable = []
        for card in self.hand:
            if card.color == top_discard_card.color:
                playable.append(card)
            elif card.type == top_discard_card.type:
                playable.append(card)
        return playable


    # hand
    # is players turn
    # play card
    # add a card
    # end turn
