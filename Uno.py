#import and initialize pygame
import pygame
import sys
import game
import player
pygame.init()
g = game.Game()
g.players.append(player.Player("Steve", 0))
g.players.append(player.Player("Chris", 1))
g.players.append(player.Player("John", 2))
g.deal_inital_cards_to_players()

base_font = pygame.font.Font(None, 32)
#create the screen
w = pygame.display.set_mode((0,0),pygame.FULLSCREEN)


# Set backgorund to screen
background = pygame.image.load("res/table/wooden_table.png").convert()
background = pygame.transform.scale(background, 
                                    (pygame.display.Info().current_w, 
                                     pygame.display.Info().current_h))
w.blit(background, (0, 0))




def render():
    top_x = 10
    top_y = 10
    for player in g.players:
        if player.get_id() != g.current_turn:
            # display other players card count
            player_description = f"{player.name}: {player.get_number_of_cards()}"
            font = pygame.font.Font(None, 32)
            font = font.render(player_description, True, (255, 255, 255))
            text_rect = font.get_rect()
            text_rect.center = (((text_rect.size[0] // 2) + top_x), 
                                ((text_rect.size[1] // 2) + top_y))
            top_x += text_rect.size[0] + 10
            w.blit(font, text_rect)
        else:
            #display current Players cards
            left = 10
            temp_img = pygame.image.load("res/blue_0.png").convert()
            temp_rect = temp_img.get_rect()
            bottom = (pygame.display.Info().current_h - 10) - (temp_rect.size[1] * (len(player.hand) // 11)) - (10 * (len(player.hand) // 11))
            card_count = 0
            for card in player.hand:
                card_image = pygame.image.load(card.resource).convert()
                card_image_rect = card_image.get_rect()
                card_image_rect.bottomleft = (left, bottom)
                left += card_image_rect.size[0] + 10
                card_count += 1
                if card_count > 10:
                    card_count = 0 
                    left = 10
                    bottom += (temp_rect.size[1] * (len(player.hand) // 11)) + (10 * (len(player.hand) // 11))
                w.blit(card_image, card_image_rect)
    # draw the deck
    deck_img = pygame.image.load("res/card_back.png").convert()
    deck_rect = temp_img.get_rect()
    deck_rect.topright = (pygame.display.Info().current_w - 10, 10)
    w.blit(deck_img, deck_rect)
    #Draw the discard
    discard_img = pygame.image.load(g.discard.top_card.resource).convert() # TODO: mak ehtis the top f discard
    discard_rect = discard_img.get_rect()
    discard_rect.topright = (pygame.display.Info().current_w - 20 - discard_rect.size[0], 10)
    w.blit(discard_img, discard_rect)



def update():
    pass






rect = pygame.Rect(200, 200, 140, 32) 
user_text = ''

color_active = pygame.Color('lightskyblue3') 
  
# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 
#title
pygame.display.set_caption("A Simple Game Uno")



x=False
active=False
while True:
    render()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if rect.collidepoint(event.pos): 
                active = True
            else: 
                active = False
  
        #ways to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                x = True 
  
            # Unicode standard is used for string 
            # formation 
            else: 
                user_text += event.unicode
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                x = False
                user_text -= event.unicode

    if x == True:
        user_text = user_text[:-1]
    

    if active: 
        color = color_active 
    else: 
        color = color_passive 

    pygame.draw.rect(w, color, rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    w.blit(text_surface, (rect.x+5, rect.y+5)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    rect.w = max(100, text_surface.get_width()+10) 
      
      


    pygame.display.flip()