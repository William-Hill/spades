from collections import namedtuple
import random

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
AI_hand = []
AI_books = 0
players_hand = []
players_books = 0
players_turn = False
Card = namedtuple('Card', ['rank', 'suit', 'value'])

def generate_deck():
    ''' gives a list of 53 card tuples with rank and suit'''
    cards = [Card(rank, suit, calculate_card_value(rank, suit)) for rank in RANKS for suit in SUITS]
    return cards

def getKey(hand):
    '''Callback used to sort cards by their value'''
    return hand.value


def sort_hand(hand):
    ''' Sort hand according to suit '''
    sorted_hand = sorted(hand, key=getKey)
    return sorted_hand


def initialize_game():
    '''Sets up initial game by dealing and sorting player and AI hand'''
    global AI_hand
    global players_hand
    deck_of_cards = generate_deck()
    deal_hand(AI_hand, deck_of_cards)
    AI_hand = sort_hand(AI_hand)
    deal_hand(players_hand, deck_of_cards)
    players_hand = sort_hand(players_hand)

def AI_choose_card(hand, players_card=None):
    '''AI logic for choosing a card to play '''
    global spades_cut
    if players_card:
        #set to weakest card in deck
        temp_card = hand[0]
        # loop through list looking for card of same suit
        for card in hand:
            # if card is found of same suit, set as temp card
            if card.suit == players_card.suit:
                temp_card = card
                if temp_card.value > players_card.value:
                    break
                else:
                    continue
        # if card of same suit is not found, set temp card to card with a higher value than player card
            if card.value > players_card.value:
                temp_card = card
                continue
        # if no card is higher than player card, set temp card to lower card in hand
        chosen_card_index = hand.index(temp_card)
        chosen_card = hand.pop(chosen_card_index)
        if chosen_card.suit == "spades":
            spades_cut = True
        return chosen_card
    else:
        #If it is the AI's turn, it plays its weakest card
        chosen_card = hand.pop(0)
        return chosen_card

def print_players_hand(players_hand):
    '''print the player's hand of cards as a menu style that allows cards to be
    selected.'''
    for index, card in enumerate(players_hand):
        print "{index}) {rank} of {suit} (value: {value})".format(index=index + 1, rank=card.rank, suit=card.suit, value=card.value)


def print_AI_card(AI_card):
    ''' Prints out the card the AI chose in a readable format '''
    print "AI_card: {rank} of {suit} (value: {value})".format(rank=AI_card.rank, suit=AI_card.suit, value=AI_card.value)


def print_player_card(player_card):
    ''' Prints out the card the player chose in a readable format '''
    print "player_card: {rank} of {suit} (value: {value})".format(rank=player_card.rank, suit=player_card.suit, value=player_card.value)

def choose_player_card():
    ''' Lets the player choose a card from their deck '''
    pass

def compare_cards(card_1, card_2):
    ''' Compares the player's card to the AI's card to determine the winner '''
    pass

def deal_hand(hand_list, deck, cards_in_hand=5):
    ''' Deals a hand of cards from the deck '''
    pass

def calculate_card_value(rank, suit):
    ''' Calculates the playing value of a card by its rank and suit '''
    pass

def main():
    ''' Main function '''
    pass

if __name__ == '__main__':
    main()
