import pygame


def update(game, event, clickable_cards, deck_rect):
    """Update loop. will update the game according to what needs to occur. The event should be
    a mousedown event"""
    current_player = game.get_current_player()

    for card, rect in clickable_cards:
        if rect.collidepoint(event.pos): 
            print(card.type, card.color)
            if game.is_card_playable(card):
                game.play_card(card)
                game.set_next_players_turn()
        else: 
            pass
    # deck draw feature
    if deck_rect.collidepoint(event.pos):
        drawn_card = game.deck.draw_card(game.discard)
        current_player.draw_card(drawn_card)
        game.set_next_players_turn()
