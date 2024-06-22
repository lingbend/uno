import random
import termcolor

wild_color = None
skip = False
reverse = 'clockwise'
draw = 0
discards = []
deck = []
name_options = ['Egbert', 'Frodo', 'Victoria', 'Francis Bacon', 'George', 'Maria', 'Lea', 'Grover', 'Errol',
                'Madeline', 'Helen', 'Marcus', 'Harry', 'Eugene', 'Titus', 'Gaspar', 'Eve', 'Lindsey',
                'Britton', 'Lars', 'Horace', 'Stuart', 'Julius Caesar', 'Monica', 'Alistair', 'Stanislas',
                'Rizzo', 'Adele', 'Fabio', 'Amy', 'Damian', 'Shaggy', 'Rolf', 'Cedric', 'Voldemort', 'Robert',
                'Mercury', 'Loki', 'Ares', 'Seth', 'James', 'Rebekah', 'Mr. Cockroach', 'Mr. Potato Head',
                'Aragorn', 'Sauron', 'Legolas', 'John Doe', 'Roald Dahl', 'Harley Davidson',
                'Dwayne "The Rock" Johnson', 'Stick', 'Mr. Toad', 'Tony Stark', 'Galloran', 'Gonzo',
                'Scoobidus Moobidus, the Great Old One', 'Golum', 'Smeagol', 'Spencer']

def reset_variables():

    global skip
    global reverse
    global draw
    global discards
    global deck

    skip = False
    reverse = 'clockwise'
    draw = 0
    discards = []
    deck = []


def main():
    play_again = True
    while play_again:
        reset_variables()
        if not check_options():
            break
        generate_deck()    # list of tuples
        num_players = get_num_players()
        hands = deal_hands(num_players)
        winner = play_game(num_players, hands)
        print(f'The winner is {winner}!')


def generate_deck():

    global deck

    # Generates each card as a tuple
    for color in ['Red', 'Blue', 'Yellow', 'Green']:

        for i in range(10):    # Creates numbers 0 to 9
            deck.append((color, i))
            if i != 0:    # Adds a second card for all numbers except 0
                deck.append((color, i))

        for k in ['Skip', 'Draw Two', 'Reverse']:    # Generates all special, colored cards here
            deck.append((color, k))
            deck.append((color, k))

    for j in range(4):    # Generates each type of Wild card 4 times
        deck.append(('Wild', 'Normal'))
        deck.append(('Wild', 'Draw Four'))
    random.shuffle(deck)


def get_num_players():
    while True:
        number = input('How many players are there? (2-10) ')
        try:
            number = int(number)
        except ValueError:
            print("Try again, that's not a number.")
        else:
            if number <= 1 or number > 10:
                print('Enter a whole number between 2 and 10.')
            else:
                return number


def deal_hands(num_players):

    hands = {}

    for i in range(num_players):
        hand = []
        for j in range(7):
            draw_card(hand)
        hands['Player' + str(i + 1)] = hand
    return hands


def play_game(num_players, hands):

    global deck
    global discards
    global skip
    turn_num = random.randint(1, num_players)
    end = False
    discards = [deck.pop(0)]

    while not end:
        for i in range(1, num_players + 1):
            top_card = discards[-1]
            print('Top card:', end=' ')
            print_cards([top_card])
            if skip:
                skip = False
                continue
            elif i == turn_num:
                if player_turn(hands, turn_num, top_card):
                    return 'you'
            else:
                computer_turn(i)


def player_turn(hands, turn_num, top_card):

    global draw
    hand = hands['Player' + str(turn_num)]

    print('Your hand:', end=' ')
    print_cards(hand)

    if draw != 0:
        print(f"You draw {str(draw)} cards.")
        for i in range(draw):
            draw_card(hand)
        draw = 0
    else:
        selection = get_card_select(hand, top_card)
        if play_cards(selection, hand, top_card):
            return True


def play_cards(selection, hand, top_card):

    global discards
    global wild_color
    global skip
    global reverse
    global draw

    if selection != 'Draw a card':
        discards.append(selection)
        hand.remove(selection)
        if check_winner(hand):
            return True
        if "Wild" in selection:
            while True:
                wild_color = input("Choose a color (Red, Blue, Yellow, or Green): ").capitalize()
                if wild_color in ['Red', 'Blue', 'Yellow', 'Green']:
                    break
                else:
                    print('Try again.')
        elif "Skip" in selection:
            skip = True
        elif "Reverse" in selection:
            if reverse == 'clockwise':
                reverse = 'counterclockwise'
            else:
                reverse = 'clockwise'
        if "Draw Two" in selection:
            draw += 2
        elif "Draw Four" in selection:
            draw += 4
    else:
        new_card = draw_card(hand)
        if get_valid_cards([new_card], top_card):
            print_cards([new_card])
            while True:
                choice = input('Do you want to play this card? (y/n) ')
                if not choice.isalpha():
                    print('Invalid response, try again.')
                elif choice.lower() == 'y':
                    print('Card played.')
                    play_cards(new_card, hand, new_card)
                    break
                elif choice.lower() == 'n':
                    print('Card not played.')
                    break
                else:
                    print('Invalid response, try again.')


def draw_card(hand):

    global deck
    global discards

    if len(deck) == 0:
        top_card = discards.pop(-1)
        random.shuffle(discards)
        deck = discards
        discards.clear()
        discards.append(top_card)
    else:
        new_card = deck.pop(0)
        hand.append(new_card)
        return new_card


def get_card_select(hand, top_card):
    choices = get_valid_cards(hand, top_card)
    print('Options:', end=' ')
    print_cards(choices, False)
    print('Draw a card')
    while True:
        selection = input(f'Choose an option (1-{len(choices)+1}): ')
        try:
            selection = int(selection)
            if not 0 < selection <= len(choices) + 1:
                print(f'Choose an option between 1 and {len(choices) + 1}')
                continue
        except ValueError:
            print("Invalid selection, try again.")
        else:
            if selection == len(choices) + 1:
                return 'Draw a card'
            else:
                return choices[selection - 1]


def get_valid_cards(hand, top_card):
    valid_cards = []
    top_color, top_type = top_card
    for card in hand:
        color, ctype = card
        if color == "Wild":
            valid_cards.append(card)
        elif top_color == "Wild" and color == wild_color:
            valid_cards.append(card)
        elif color == top_color or ctype == top_type:
            valid_cards.append(card)
    return valid_cards


def check_winner(hand):
    if not hand:
        return True
    return False


def print_cards(cards, new_line=True):
    for color, ctype in cards:
        card = color + ' ' + str(ctype)
        if color == 'Wild':
            termcolor.cprint(card, 'cyan', end=', ')
        else:
            termcolor.cprint(card, color.lower(), end=', ')
    if new_line:
        print()


def computer_turn(num):
    pass


def check_options():
    choice = input('Select an option (Play, Quit): ')
    if not choice.isalpha():
        print('Choose a valid option.')
    elif choice.lower() == 'play':
        print('Starting game.')
        return True
    elif choice.lower() == 'quit':
        return False
    else:
        print('Choose a valid option.')


if __name__ == '__main__':
    main()
