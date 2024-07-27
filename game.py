import player
import deck

NUMBER_OF_PLAYERS = 4
INITIAL_NUMBER_OF_CARDS = 7


class Game:
    def __init__(self) -> None:
        self.players = []
        self.deck = self.create_deck()
        self.current_turn = 0
        self.direction_of_play = 'right'
        self.actions = []

    def create_a_player(self, player_name):
        p = player.Player(player_name, len(self.players))
        self.players.append(p)
    
    def deal_inital_cards_to_players(self):
        for i in range(INITIAL_NUMBER_OF_CARDS):
            for player in self.players:
                card = self.deck.draw_card()
                player.draw_card(card)


    def create_deck(self):
        self.deck = deck.Deck()
        self.deck.shuffle_cards()

    def reverse(self):
        if self.direction_of_play == 'left':
            self.direction_of_play = 'right'
        else:
            self.direction_of_play = 'left'

    def set_next_players_turn(self):
        if self.direction_of_play == 'right':
            self.current_turn += 1
            if self.current_turn >= len(self.players):
                self.current_turn = 0
        else:
            self.current_turn -= 1
            if self.current_turn < 0:
                self.current_turn = len(self.players) - 1
    
    def get_current_player(self):
        for player in self.players:
            if player.get_id() == self.current_turn:
                return player
        return 0

    def play_turn(self):
        if len(self.actions) == 0:


    def main():
        # set up players
        # set up deck
        # deal inital cards to players
        # select a player to go first and esablish an order of turns
        # Play a player's turn

        