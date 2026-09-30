import random as rng

# the structure of the solution relies on functions that return values

def deal_card():
    ''' returns a random card when called '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return rng.choice(cards)

def calc_score(cards: list):
    ''' returns 0 for blackjack, calculates the ace dynamically based on score, returns the some of the rest '''
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user, dealer):
        ''' returns a string of the game\'s conclusion. the order here is more important due to the game\'s rules and logic '''
        if user == dealer:
            return 'draw!'
        elif dealer == 0:
            return 'you lose, the dealer has a blackjack!'
        elif user > 21:
            return 'you lose, it\'s a bust!'
        elif dealer > 21:
            return 'you win, the dealer has bust!'
        elif user > dealer:
            return 'you win, congrat!'
        else:
            return 'you lose!'

while True:
    user_card = []
    dealer_card = []
    game_state = True

    # the first draw
    # the underscore is more memeory effcient and is normally called for simple instructions.
    for _ in range(2):     
        user_card.append(deal_card())
        dealer_card.append(deal_card())

    # game logic and loop
    while game_state:

        user_score = calc_score(user_card)
        dealer_score = calc_score(dealer_card)

        print(f'your cards are: {user_card}, and your score is: {user_score}')
        print(f'the dealer\'s card is: {dealer_card[0]}')

        # the core game logic. using the first else section with a seprate if statement would casue it to execute once if even if the user choose to end those adding one more card without asking
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_state = False
        else:
            hit_pass = input('do you want to hit or pass? h or p\n')
            if hit_pass == 'h':
                user_card.append(deal_card())
            else:
                game_state = False

        while dealer_score < 17 and dealer_score != 0:
            dealer_card.append(deal_card())
            dealer_score = calc_score(dealer_card)

    print(f'your final hand is: {user_card} scoring: {user_score}')
    print(f'the dealer\'s final hand is: {dealer_card} scoring: {dealer_score}')
    print(compare(user_score, dealer_score))

    # keep the playing or exit    
    continue_playing = input('press c to continue playing, e to exit.\n')
    if continue_playing == 'c':
        print('\n' * 20)
        None
    else:
        break
