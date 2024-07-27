#import and initialize pygame
import pygame
import sys
pygame.init()

#create the screen
w = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
w.fill((0,0,255))
rect = pygame.Rect(200, 200, 140, 32) 
base_font = pygame.font.Font(None, 32) 
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