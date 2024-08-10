#import and initialize pygame
import pygame
import sys
import game
import player
import render
import update
pygame.init()
g = game.Game()
g.players.append(player.Player("Steve", 0))
g.players.append(player.Player("Chris", 1))
g.players.append(player.Player("John", 2))
g.deal_inital_cards_to_players()

base_font = pygame.font.Font(None, 32)
#create the screen
w = pygame.display.set_mode((0,0),pygame.FULLSCREEN)


rect = pygame.Rect(200, 200, 140, 32) 
user_text = ''

color_active = pygame.Color('lightskyblue3') 
  
# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 
#title
pygame.display.set_caption("A Simple Game of Uno")


while True:
    clickable_cards, deck_rect = render.render(w, g)
    # Input (with update inside)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            update.update(g, event, clickable_cards, deck_rect)
        #ways to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()