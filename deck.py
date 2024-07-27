from card import Card
import random

class Deck:

    def __init__(self):
        self.top_card = None
        self.card_list = []

    
    def shuffle_cards(self, discard=None):
        if discard is None:
            card_list = self.initialize_cards()
        elif type(discard) != Deck:
            return False
        else:
            card_list = discard.card_list
            discard.card_list = []
            for card in card_list:
                if card.type == 'wild' or card.type == 'draw_4':
                    card.color == 'wild'

        self.card_list = random.shuffle(card_list)

    def add_card(self, new_card):
        self.card_list.append(new_card)
        self.top_card = new_card


    def initialize_cards():
        cards = []
        for color in ['red', 'blue', 'green', 'yellow']:
            for type in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                cards.append(Card(color, type))
                cards.append(Card(color, type))
            for type in ['reverse', 'draw_2', 'skip', '0']:
                cards.append(Card(color, type))
        for i in range(4):
            cards.append(Card('wild', 'wild'))
            cards.append(Card('wild', 'draw_4'))
        return cards
            

    def draw_card(self):
        if len(self.card_list) <= 0:
            pass 
            #shuffle discard
        card = self.card_list.pop()
        if len(self.card_list) <= 0:
                pass
                #shuffle discard
        self.top_card = self.card_list[-1]
        return card
    