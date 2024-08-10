
def update(game, event, clickable_cards, deck_rect, red_rect, yellow_rect, green_rect, blue_rect, confirm=None):
    """Update loop. will update the game according to what needs to occur. The event should be
    a mousedown event"""
    current_player = game.get_current_player()
    # If a player is to pick a color
    if game.action == "pick_color":
        # Set up color pickers
        color_pickers = [(red_rect, "red"),
                         (yellow_rect, "yellow"),
                         (green_rect, "green"),
                         (blue_rect, "blue")]
        # check if color is chosen
        for color_picker, color in color_pickers:
            if color_picker.collidepoint(event.pos):
                game.discard.top_card.color = color
                # Check if played card is a draw 4
                if game.discard.top_card.type == "draw_4":
                    game.action = "draw_4"
                else:
                    game.action = ""
                game.set_next_players_turn()
    # Handle Skips
    elif game.action == "skip":
        if confirm.collidepoint(event.pos):
            game.action = ""
            game.set_next_players_turn()
    # Handle Draw 2s
    elif game.action == "draw_2":
        if confirm.collidepoint(event.pos):
            for _ in range(2):
                drawn_card = game.deck.draw_card(game.discard)
                current_player.draw_card(drawn_card)
            game.action = ""
            game.set_next_players_turn()
    # Handle Draw 4s
    elif game.action == "draw_4":
        if confirm.collidepoint(event.pos):
            for _ in range(4):
                drawn_card = game.deck.draw_card(game.discard)
                current_player.draw_card(drawn_card)
            game.action = ""
            game.set_next_players_turn()
    # Handle Normal Play
    else:
        # Draw from Deck if chosen
        if deck_rect.collidepoint(event.pos):
            drawn_card = game.deck.draw_card(game.discard)
            if not drawn_card:
                game.game_state = 'play'
                return
            else:
                current_player.draw_card(drawn_card)
                game.set_next_players_turn()
                game.game_state = ''
                return  # stop update function after drawing a card.
        # Play a card
        for card, rect in clickable_cards:
            if rect.collidepoint(event.pos): 
                if game.is_card_playable(card):
                    game.game_state = ''
                    game.play_card(card)
                    check_win(game)
                    if card.color != "wild" and game.action != "win":
                        game.set_next_players_turn()
        

def check_win(game):
    current_player = game.get_current_player()
    if len(current_player.hand) == 0:
        game.action = "win"