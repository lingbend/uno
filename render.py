import pygame

def render(window, game):
    # Get background resource
    background = pygame.image.load("res/table/wooden_table.png").convert()
    background = pygame.transform.scale(background, 
                                    (pygame.display.Info().current_w, 
                                     pygame.display.Info().current_h))
    # Start with a Clear screen
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))

    top_x = 10
    top_y = 10
    # Display player stats
    for player in game.players:
        offset = display_player_stats(window, player, (top_x, top_y))
        top_x += offset[0] + 10
        if player.get_id() == game.current_turn:
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
                window.blit(card_image, card_image_rect)
    # draw the deck
    deck_img = pygame.image.load("res/card_back.png").convert()
    deck_rect = temp_img.get_rect()
    deck_rect.topright = (pygame.display.Info().current_w - 10, 10)
    window.blit(deck_img, deck_rect)
    #Draw the discard
    discard_img = pygame.image.load(game.discard.top_card.resource).convert() # TODO: mak ehtis the top f discard
    discard_rect = discard_img.get_rect()
    discard_rect.topright = (pygame.display.Info().current_w - 20 - discard_rect.size[0], 10)
    window.blit(discard_img, discard_rect)


def display_player_stats(window, player, top_left_coords):
    """Displays one player's stats in the location specified in the coords. Returns the size of
    the text."""
    # Get text to display
    player_description = f"{player.name}: {player.get_number_of_cards()}"
    # Create a font pygame object for displaying
    font = pygame.font.Font(None, 32)
    # Add text to font object
    font = font.render(player_description, True, (255, 255, 255))
    # set the location of the font object
    text_rect = font.get_rect()
    text_rect.center = (((text_rect.size[0] // 2) + top_left_coords[0]), 
                        ((text_rect.size[1] // 2) + top_left_coords[1]))
    # render the font object
    window.blit(font, text_rect)
    return text_rect.size