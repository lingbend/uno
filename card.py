
class Card:

    ## reverse, draw_2, wild, wild_draw_4, skip, number

    def __init__(self, color, type, deck, discard):
        self.color = color
        self.type = type
        self.deck = deckS
        self.diSscard = discard
        self.type_list = ['reverse', 'draw_2', 'wild', 'wild_draw_4', 'skip', 'number']

    def play_card(self): # is used by play_card function for player
        self.discard.add_card(self) # calls add card function on discard deck object
        
        if self.discard.top_card.color == self.color:
            if self.type == 'reverse':
                reverse()
            elif self.type == 'draw_2':
                draw_2()
            elif self.type == 'wild':
                wild()
            elif self.type == 'wild_draw_4':
                wild_draw_4()
            elif self.type == 'skip':
                skip()
            else:
                return False
        elif self.deck.top_card.type == self.type:
            self.discard.add_card(self)
        # check type
        # if type not number, do action
