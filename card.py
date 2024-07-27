from deck import Deck


class Card:

    ## reverse, draw_2, wild, wild_draw_4, skip, number

    def __init__(self, color, type):
        self.color = color
        self.type = type

    def play_card(self, discard): # is used by play_card function for player
        
        if discard.top_card.color == self.color:
            discard.add_card(self) # calls add card function on discard deck object
            return self.type

        elif discard.top_card.type == self.type:
            discard.add_card(self)
            return self.type

        else:
            return False
