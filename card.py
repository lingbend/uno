import random

class Card:

    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.resource = self.get_resource(color, type)

    def play_card(self, discard): # is used by play_card function for player
        
        if discard.top_card.color == self.color:
            discard.add_card(self) # calls add card function on discard deck object
            return self.type

        elif discard.top_card.type == self.type:
            discard.add_card(self)
            return self.type

        else:
            return False
        
    def get_resource(self, color, type):
        relative_path = 'res/'
        if color != 'wild':
            relative_path += (color + '_')
            if type != 'reverse':
                relative_path += type
            else:
                relative_path = 'res/grandpa_' + color
        else:
            if type == 'draw_4':
                relative_path = 'res/wild_pick_four'
            else:
                relative_path = random.choice(['res/wild_color_changer', 'res/wild_napoleon'])
        relative_path += '.png'
        return relative_path


# print(Card('red', 'reverse').resource)
# print(Card('green', 'draw_2').resource)
# print(Card('yellow', 'skip').resource)
# print(Card('blue', '6').resource)
# print(Card('wild', 'wild').resource)
# print(Card('wild', 'draw_4').resource)


