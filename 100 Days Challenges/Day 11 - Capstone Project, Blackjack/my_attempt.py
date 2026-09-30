# the challenge is to create a very simple version of black jack with only pass and hit functions
# no double down option or a score or bet tracker. if I can implement that it would be a nice bonus

import random as rng

# since the idea is a simple game of blackjack, the instructor gives the list of cards below:
# also, we will be assuming that the deck is infinite, so cards are not removed when used.

# functions for the game

def player_first_hand(player_hand: list, cards: list):
    player_hand.append(rng.choice(cards))
    player_hand.append(rng.choice(cards))
    return player_hand

def dealer_first_hand(dealer_hand: list, cards: list):
    dealer_hand.append(rng.choice(cards))
    dealer_hand.append(rng.choice(cards))
    return dealer_hand[0]

def check_ace(hand):

    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1

def game_logic(player: list, dealer: list ):

        if sum(player) > 21:
            print(f'you bust! your hand is {player}, totaling {sum(player)}')
            return False
        elif sum(player) == 21:
            print(f'21 ! you win! your hand is {player}, totaling {sum(player)}')
            return False
        elif sum(player) < 21:
            print(f'your hand is {player}, totaling {sum(player)}\n')
            hit_pass = input('hit, or pass? h or p\n')
            if hit_pass == 'h':
                player.append(rng.choice(cards))
                return True # True to continue and recheck after the hit.
            elif hit_pass == 'p':
                while sum(dealer) < 17:
                    dealer.append(rng.choice(cards))
                    if sum(dealer) > 21:
                        print(f'the dealer busts! you win! the dealer\'s hand is {sum(dealer)}')
                        return False
                if sum(player) > sum(dealer):
                    print(f'you win! your hand is {player}, totaling {sum(player)}\nand the dealer\'s hand is {dealer}, totaling {sum(dealer)}\n')
                    return False
                elif sum(player) < sum(dealer):
                    print(f'you lose! your hand is {player}, totaling {sum(player)}\nand the dealer\'s hand is {dealer}, totaling {sum(dealer)}\n')
                    return False
                elif sum(player) == sum(dealer):
                    print(f'a draw! your hand is {player}, totaling {sum(player)}\nand the dealer\'s hand is {dealer}, totaling {sum(dealer)}\n')
                    return False
            return False

status = True

while status == True:
    # variables for the game, if this was more sophistacated, I would have created a class for the game and the player and dealer, but for now, this will do.
    # for now they will be a part of the while loop.
    cards = [11, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 10, 10, 10] # the ace will count as 11 until the user goes over 21
    hands = {
        'player': [],
        'dealer': []
    }

    # the first hand
    player_first = player_first_hand(hands['player'], cards) 
    dealer_first = dealer_first_hand(hands['dealer'], cards)

    # view the first hand
    print(f'the dealer\'s hand: {dealer_first}')
    print(f'your hand: {player_first}\n')

    # the game's loop
    logic_loop = True
    while logic_loop == True:
        check_ace(hands['player'])
        check_ace(hands['dealer'])
        if game_logic(hands['player'], hands['dealer']) == False:
            logic_loop = False

    continue_game = input('continue? y or n\n')
    print('\n' * 100)
    if continue_game == 'n':
        status = False
