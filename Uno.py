#import and initialize pygame
import pygame
import sys
import game
import player
import render
import update

# Initialize The game
pygame.init()
g = game.Game()
g.players.append(player.Player("Steve", 0))
g.players.append(player.Player("Chris", 1))
g.players.append(player.Player("John", 2))
g.deal_inital_cards_to_players()

# create the screen
w = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
# set title
pygame.display.set_caption("A Simple Game of Uno")


while True:
    # Render the cards
    clickable_cards, deck_rect = render.render(w, g)

    # Get Input (with update inside)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            update.update(g, event, clickable_cards, deck_rect)
        # Ways to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Finish Game Loop
    pygame.display.flip()
