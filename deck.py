from card import Card
import random

class Deck:

    def __init__(self):
        self.top_card = None
        self.card_list = []

    
    def shuffle_cards(self, card_list):
        pass


    def add_card(self, new_card):
        self.card_list.append(new_card)
        self.top_card = new_card






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