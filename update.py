
def update(game, event, clickable_cards, deck_rect, red_rect, yellow_rect, green_rect, blue_rect, confirm=None):
    """Update loop. will update the game according to what needs to occur. The event should be
    a mousedown event"""
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
    else:
        current_player = game.get_current_player()

        for card, rect in clickable_cards:
            if rect.collidepoint(event.pos): 
                if game.is_card_playable(card):
                    game.play_card(card)
                    if card.color != "wild":
                        game.set_next_players_turn()
            else: 
                pass
        # deck draw feature
        if deck_rect.collidepoint(event.pos):
            drawn_card = game.deck.draw_card(game.discard)
            current_player.draw_card(drawn_card)
            game.set_next_players_turn()
