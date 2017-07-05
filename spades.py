from collections import namedtuple
import random
import logging

logging.basicConfig(format = "%(levelname): %(lineno)s %(funcName)s: %(asctime)s", level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
AI_hand = []
AI_books = 0
players_hand = []
players_books = 0
spades_cut = False
Card = namedtuple('Card', ['rank', 'suit', 'value'])
''' value is used to compare which card wins '''

def generate_deck():
    cards = [Card(rank, suit, calculate_card_value(rank,suit)) for rank in RANKS for suit in SUITS]
    return cards
    ''' gives a list of 53 card tuples with rank and suit'''

def deal_hand(hand_list, deck, cards_in_hand = 5):
    #TODO: possibly move shuffle here (add test)
    #TODO: validate cards_in_hand: make sure it is int, set max cards_in_hand as well (10 cards?)
    '''pass in blank list of AI hand or player hand'''
    for _ in range(cards_in_hand):
        item = deck.pop()
        # print "item:", item
        hand_list.append(item)

def calculate_card_value(rank, suit):
    #TODO: Add multiplier for spades suit
    '''Calculates the value by the index in the list'''
    rank_value = RANKS.index(rank)
    suit_value = SUITS.index(suit)
    # print "{rank} of {suit} = {value}".format(rank=rank, suit=suit, value=rank_value + suit_value)
    return rank_value + suit_value

def getKey(hand):
    '''Callback used to sort cards by their value'''
    return hand.value

def sort_hand(hand):
    ''' Sort hand according to suit '''
    sorted_hand = sorted(hand, key=getKey)
    return sorted_hand

def compare_cards(card_1, card_2):
    global players_books
    global AI_books
    card_1_value = calculate_card_value(card_1.rank, card_1.suit)
    card_2_value = calculate_card_value(card_2.rank, card_2.suit)
    #TODO: Add tie breaker for cards with equivalent calculated values
    #TODO: calling value again is repetitive change comparison to card_1.value > card_2.value
    #TODO: in case of tie breaker, do comparison of suits to determine winner
    if card_1_value > card_2_value:
        print "player won book"
        players_books +=1
    else:
        print "AI won book"
        AI_books +=1

def initialize_game():
    '''Sets up initial game by dealing and sorting player and AI hand'''
    global AI_hand
    global players_hand
    deck_of_cards = generate_deck()
    # print "number of cards:", len(deck_of_cards)
    # print "cards:", deck_of_cards
    random.shuffle(deck_of_cards)
    # print "shuffled deck:", deck_of_cards

    deal_hand(AI_hand, deck_of_cards)
    AI_hand = sort_hand(AI_hand)
    deal_hand(players_hand, deck_of_cards)
    players_hand = sort_hand(players_hand)


def find_cards_of_suit(suit, hand):
    #TODO: delete (Deprecated)
    cards_of_suit = [card for card in hand if card.suit == suit]
    return cards_of_suit


def AI_choose_card(hand, players_card = None):

    # sorted_AI_hand = sort_hand(AI_hand)
    # print "sorted_AI_hand: ", sorted_AI_hand
    if players_card:
        print "players_card_value: ", players_card.value
        '''set to weakest card in deck'''
        temp_card = hand[0]
        # same_suit_cards = find_cards_of_suit(players_card.suit, AI_hand)
        #loop through list looking for card of same suit
        #TODO: remove enumerate and index
        for index, card in enumerate(hand):
        #if card is found of same suit, set as temp card
            if card.suit == players_card.suit:
                temp_card = card
                if temp_card.value > players_card.value:
                    break
                else:
                    continue
        #if card of same suit is not found, set temp card to card with a higher value than player card
            if not temp_card and card.value > players_card.value:
            #TODO: will never not be temp card since temp card is automatically set to first in hand
                temp_card = card
                continue
        #if no card is higher than player card, set temp card to lower card in hand
        chosen_card_index = hand.index(temp_card)
        print "chosen_card_index: ", chosen_card_index
        chosen_card = hand.pop(chosen_card_index)
        print "chosen_card:", chosen_card
        return chosen_card
    else:
        '''If it is the AI's turn, it plays its weakest card'''
        chosen_card = hand.pop(0)
        return chosen_card

#TODO: log AI_hand to a file with timestamp and unique gameID and/or timestamp
#print "AI_hand:", AI_hand
#print "players_hand: ", players_hand

def print_players_hand():
    #TODO: loop over players hand and name cards more descriptively
    #"Card.rank of card.suit" as a naming convention
    '''print the player's hand of cards as a menu style that allows cards to be
    selected.
    Example:
    1) 3_Hearts
    2) King_Diamonds
    3) Ace_Spades '''
    pass

def main():
    print "Welcome to the CyberCamp 2017 Game of Spades!!"
    print "You will be playing against an AI-controlled opponent."
    initialize_game()

    # print "Here's the hand you have been dealt: \n"
    while len(players_hand) > 0:
        #TODO: replace this with print_players_hand()
        print players_hand
        players_card_selection = int(raw_input("Choose a card to play \n"))
        #TODO: Add a check for if spades have been cut
        #TODO: If player tries to cut, deny them
            #(if spade is played when card of same suit is available)
        #TODO: Account for index out of range error
        players_card = players_hand.pop(players_card_selection-1)
        #-1 for off by 1 error
        AI_card = AI_choose_card(AI_hand, players_card)
        #TODO: set a second parameter to figure out if AI or player is going first
        compare_cards(players_card, AI_card)
        print "player's books:", players_books
        print "AI's books: ", AI_books



if __name__ == '__main__':
    main()
