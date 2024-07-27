import player

NUMBER_OF_PLAYERS = 4


class Game:
    def __init__(self) -> None:
        self.players = []

    def create_a_player(self, player_name):
        p = player.Player(player_name, len(self.players))
        self.players.append(p)
    
    def deal_cards_to_players(self):


    def main():
        # set up players
        # set up deck
        # deal inital cards to players
        # select a player to go first and esablish an order of turns
        # Play a player's turn

        