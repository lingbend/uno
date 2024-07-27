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
        self.action = ''

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
    
    def get_current_player(self) -> player.Player:
        for player in self.players:
            if player.get_id() == self.current_turn:
                return player
        return 0

    def play_turn(self):
        if self.action == "draw 2":
            for _ in range(2):
                card = self.deck.draw_card()
                self.get_current_player().draw_card(card)
        elif self.action == "draw 4":
            for _ in range(4):
                card = self.deck.draw_card()
                self.get_current_player().draw_card(card)
        elif self.action == "skip":
            self.set_next_players_turn()
            return # End the players turn now.
        
        # If no cards avalilable to play, draw a card and end the turn
        if len(self.get_current_player().get_playable_cards()) == 0:
            card = self.deck.draw_card()
            self.get_current_player().draw_card(card)

        
        

    def main():
        # set up players
        # set up deck
        # deal inital cards to players
        # select a player to go first and esablish an order of turns
        # Play a player's turn

        