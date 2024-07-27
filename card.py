


class Card:

    ## reverse, draw_2, wild, wild_draw_4, skip, number

    def __init__(self, color, type, deck, discard, id):
        self.color = color
        self.type = type
        self.deck = deckS
        self.discard = discard
        self.id = id

    def play_card(self): # is used by play_card function for player
        
        if self.discard.top_card.color == self.color:
            self.discard.add_card(self) # calls add card function on discard deck object
            return self.type

        elif self.discard.top_card.type == self.type:
            self.discard.add_card(self)
            return self.type

        else:
            return False
