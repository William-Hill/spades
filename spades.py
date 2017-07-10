#!/usr/bin/env python2
from collections import namedtuple
import random

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
AI_hand = []
AI_books = 0
players_hand = []
players_books = 0
players_turn = False
Card = namedtuple('Card', ['rank', 'suit', 'value'])

def generate_deck():
    ''' gives a list of 53 card tuples with rank and suit'''
    cards = [Card(rank, suit, calculate_card_value(rank,suit)) for rank in RANKS for suit in SUITS]
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

def print_players_hand(players_hand):
    '''print the player's hand of cards as a menu style that allows cards to be
    selected.'''
    for index, card in enumerate(players_hand):
        print "{index}) {rank} of {suit} (value: {value})".format(index=index+1, rank=card.rank, suit=card.suit, value=card.value)

def print_AI_card(AI_card):
    print "AI_card: {rank} of {suit} (value: {value})".format(rank=AI_card.rank, suit=AI_card.suit, value=AI_card.value)

def print_player_card(player_card):
    print "player_card: {rank} of {suit} (value: {value})".format(rank=player_card.rank, suit=player_card.suit, value=player_card.value)

def deal_hand(hand_list, deck):
    random.shuffle(deck)

    for _ in range(5):
        item = deck.pop()
        hand_list.append(item)

def calculate_card_value(rank, suit):
    '''Calculates the value by the index in the list'''
    rank_value = RANKS.index(rank) + 1
    suit_value = SUITS.index(suit) + 1
    if suit == "spades":
        return rank_value * 15
    return rank_value + suit_value

def choose_AI_card(hand, players_card = None):
    if players_card:
        '''set to weakest card in deck'''
        temp_card = hand[0]
        #loop through list looking for card of same suit
        for card in hand:
        #if card is found of same suit, set as temp card
            if card.suit == players_card.suit:
                temp_card = card
                if temp_card.value > players_card.value:
                    break
                else:
                    continue
        #if card of same suit is not found, set temp card to card with a higher value than player card
            if  card.value > players_card.value:
                temp_card = card
                continue
        #if no card is higher than player card, set temp card to lower card in hand
        chosen_card_index = hand.index(temp_card)
        chosen_card = hand.pop(chosen_card_index)
        return chosen_card
    else:
        '''If it is the AI's turn, it plays its weakest card'''
        chosen_card = hand.pop(0)
        return chosen_card

def choose_player_card():
    while True:
        card_index = int(raw_input("Choose a card to play \n"))
        try:
            card = players_hand.pop(card_index-1)
            break
        except IndexError, error:
            print "There is no card that matches index {}".format(card_index)
            continue
    return card

def compare_cards(card_1, card_2):
    global players_books
    global AI_books
    global players_turn
    if card_1.value > card_2.value:
        print ("player won book")
        players_books +=1
        players_turn = True
    elif card_1.value == card_2.value:
        if SUITS.index(card_1.suit) > SUITS.index(card_2.suit):
            print "player won book"
            players_books +=1
            players_turn = True
        else:
            print "AI won book"
            AI_books +=1
            players_turn = False
    else:
        print ("AI won book")
        AI_books +=1
        players_turn = False

def main():
    global players_turn
    print "Welcome to the CyberCamp 2017 Game of Spades!!"
    print "You will be playing against an AI-controlled opponent."
    initialize_game()

    while len(players_hand) > 0:
        print_players_hand(players_hand)
        if not players_turn:
            AI_card = choose_AI_card(AI_hand)
            players_card = choose_player_card()
            print_player_card(players_card)
            print_AI_card(AI_card)
        else:
            players_card = choose_player_card()
            AI_card = choose_AI_card(AI_hand, players_card)
            print_AI_card(AI_card)
            print_player_card(players_card)

        compare_cards(players_card, AI_card)
        print "player's books:", players_books
        print "AI's books: ", AI_books, "\n"

if __name__ == '__main__':
    main()
