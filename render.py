import pygame

MARGIN = 10

def render(window, game):
    # Get background resource
    background = pygame.image.load("res/table/wooden_table.png").convert()
    background = pygame.transform.scale(background, 
                                    (pygame.display.Info().current_w, 
                                     pygame.display.Info().current_h))
    # Start with a Clear screen
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))

    top_x = MARGIN
    top_y = MARGIN

    clickable_cards = []
    for player in game.players:
        # Display all player stats
        offset = display_player_stats(window, player, (top_x, top_y))
        top_x += offset[0] + MARGIN
        # display Current player's hand
        if player.get_id() == game.current_turn:
            # Diplay Hand: 
            clickable_cards = display_player_hand(window, player)
            display_player_name(window, player)

    # draw the deck
    deck_img = pygame.image.load("res/card_back.png").convert()
    deck_rect = deck_img.get_rect()
    deck_rect.topright = (pygame.display.Info().current_w - 10, 10)
    window.blit(deck_img, deck_rect)
    #Draw the discard
    discard_img = pygame.image.load(game.discard.top_card.resource).convert() # TODO: make this the top discard
    discard_rect = discard_img.get_rect()
    discard_rect.topright = (pygame.display.Info().current_w - 20 - discard_rect.size[0], 10)
    window.blit(discard_img, discard_rect)
    # Display color_picker
    red_rect, yellow_rect, green_rect, blue_rect, confirm = None, None, None, None, None
    # Display color pickers if the player needs to pick the color
    if game.action == "pick_color":
        red_rect, yellow_rect, green_rect, blue_rect = display_color_pickers(window)
    elif game.action == "win":
        display_win(window, game)
    elif game.action != "":
        confirm = display_confirmation(window, game.action)
    # return all the clickable objects on the screen
    return clickable_cards, deck_rect, red_rect, yellow_rect, green_rect, blue_rect, confirm


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

def display_card(window, card, top_left_coords, card_size):
    """displays a card on the screen"""
    # get card image resource
    card_image = pygame.image.load(card.resource).convert()
    # Load the rect object
    card_image_rect = card_image.get_rect()
    # Set the location
    card_image_rect.topleft = top_left_coords
    # set the size of the card
    card_image_rect.size = card_size
    # render the card
    window.blit(card_image, card_image_rect)
    return card, card_image_rect

def display_player_name(window, player):
    text = f"{player.name}'s turn"
    font = pygame.font.Font(None, 80)
    font = font.render(text, True, (255, 255, 255))
    text_rect = font.get_rect()
    text_rect.center = ((pygame.display.Info().current_w // 2),
                        (pygame.display.Info().current_h // 6.5))
    window.blit(font, text_rect)


def display_player_hand(window, player):
    """Displays a players hand"""
    # get a card's Size
    card_size = get_card_size()
    # Get row amounts
    number_of_cards_per_row = int(pygame.display.Info().current_w / card_size[0]) - 1
    number_of_rows = len(player.hand) / number_of_cards_per_row
    if number_of_rows > int(number_of_rows):
        number_of_rows = int(number_of_rows) + 1
    # Set start position to render cards.
    left = MARGIN
    top = ((pygame.display.Info().current_h) -
           (card_size[1] * number_of_rows) -  # Multiple rows
           (MARGIN * number_of_rows))  # Card Margins

    # loop through all cards and display them.
    card_count_in_row = 0
    remaining_rows = number_of_rows
    clickable_cards = []
    for card in player.hand:
        clickable_cards.append(display_card(window, card, (left, top), card_size))
        # reset x position to newcard position
        left += card_size[0] + MARGIN
        card_count_in_row += 1
        # If end of row reached: then reset cord position to beginning of new row.
        if card_count_in_row >= number_of_cards_per_row:
            card_count_in_row = 0 
            remaining_rows -= 1
            left = MARGIN
            top = ((pygame.display.Info().current_h) -
                    (card_size[1] * remaining_rows) -
                    (MARGIN * remaining_rows))
    return clickable_cards

def get_card_size():
    """gets the card display size"""
    temp_img = pygame.image.load("res/blue_0.png").convert()
    return temp_img.get_rect().size

def display_color_pickers(window):
    """displays the 4 color choices"""
    # Red
    red = pygame.image.load("res/RedButton.png").convert()
    red_rect = red.get_rect()
    red_rect.center = ((pygame.display.Info().current_w // 2) - red_rect.size[0],
                       (pygame.display.Info().current_h // 2) - red_rect.size[1])
    window.blit(red, red_rect)
    # Yellow 
    yellow = pygame.image.load("res/YellowButton.png").convert()
    yellow_rect = yellow.get_rect()
    yellow_rect.center = ((pygame.display.Info().current_w // 2) + yellow_rect.size[0],
                          (pygame.display.Info().current_h // 2) - yellow_rect.size[1])
    window.blit(yellow, yellow_rect)
    # Green
    green = pygame.image.load("res/GreenButton.png").convert()
    green_rect = green.get_rect()
    green_rect.center = ((pygame.display.Info().current_w // 2) - green_rect.size[0],
                         (pygame.display.Info().current_h // 2) + green_rect.size[1])
    window.blit(green, green_rect)
    # Blue
    blue = pygame.image.load("res/BlueButton.png").convert()
    blue_rect = blue.get_rect()
    blue_rect.center = ((pygame.display.Info().current_w // 2) + blue_rect.size[0],
                        (pygame.display.Info().current_h // 2) + blue_rect.size[1])
    window.blit(blue, blue_rect)
    return red_rect, yellow_rect, green_rect, blue_rect

def display_confirmation(window, action):
    """displayes the action and a confrimation button"""
    # confirmation button
    confirm = pygame.image.load("res/ConfirmButton.png").convert()
    confirm_rect = confirm.get_rect()
    confirm_rect.center = ((pygame.display.Info().current_w // 2),
                           (pygame.display.Info().current_h // 2))
    window.blit(confirm, confirm_rect)

    # Message
    if action == "skip":
        text = "Skipped!!"
    elif action == "draw_2":
        text = "Draw 2 Cards!!"
    elif action == "draw_4":
        text = "Draw 4 Cards!!"
    else:
        text = action
    font = pygame.font.Font(None, 32)
    font = font.render(text, True, (255, 255, 255))
    text_rect = font.get_rect()
    text_rect.center = ((pygame.display.Info().current_w // 2),
                        (pygame.display.Info().current_h // 2 )- confirm_rect.size[1] - MARGIN)
    window.blit(font, text_rect)
    return confirm_rect

def display_win(window, game):
    current_player = game.get_current_player()
    text = f"{current_player.name} wins!!"
    font = pygame.font.Font(None, 80)
    font = font.render(text, True, (255, 255, 255))
    text_rect = font.get_rect()
    text_rect.center = ((pygame.display.Info().current_w // 2),
                        (pygame.display.Info().current_h // 2 ))
    window.blit(font, text_rect)


