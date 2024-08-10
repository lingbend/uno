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
        elif len(discard.card_list) <= 1:
            print('failed to shuffle')
            print(len(discard.card_list))
            return False
        else:
            card_list = discard.card_list[:-1]
            discard.card_list = [discard.card_list.pop()]
            discard.top_card = discard.card_list[0]
            for card in card_list:
                if card.type == 'wild' or card.type == 'draw_4':
                    card.color == 'wild'
        random.shuffle(card_list)
        self.card_list += card_list
        self.top_card = card_list[-1]
        return True

    def add_card(self, new_card):
        self.card_list.append(new_card)
        self.top_card = new_card


    def initialize_cards(self):
        cards = []
        for color in ['red', 'blue', 'green', 'yellow']:
            for type in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'reverse', 'draw_2', 'skip']:
                cards.append(Card(color, type))
                cards.append(Card(color, type))
            for type in ['0']:
                cards.append(Card(color, type))
        for i in range(4):
            cards.append(Card('wild', 'wild'))
            cards.append(Card('wild', 'draw_4'))
        return cards
            

    def draw_card(self, discard):
        if len(self.card_list) <= 1:
            if not self.shuffle_cards(discard):
                return False
        card = self.card_list.pop()
        self.top_card = self.card_list[-1]
        return card