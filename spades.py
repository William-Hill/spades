from collections import namedtuple
import random

SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
AI_hand = []
AI_books = 0
players_hand = []
players_books = 0
spades_cut = False

def generate_deck():
    Card = namedtuple('Card', ['rank', 'suit'])
    cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
    return cards

def deal_hand(hand_list, deck):
    for _ in range(5):
        item = deck.pop()
        print "item:", item
        hand_list.append(item)

def calculate_card_value(card):
    print "card:", card
    rank = RANKS.index(card.rank)
    print "rank:", rank
    suit = SUITS.index(card.suit)
    print "suit:", suit
    return rank + suit

def compare_cards(card_1, card_2):
    card_1_value = calculate_card_value(card_1)
    card_2_value = calculate_card_value(card_2)
    if card_1_value > card_2_value:
        print "player won book"
        players_books +=1
    else:
        print "AI won book"
        AI_books +=1

deck_of_cards = generate_deck()
print "deck_of_cards type: ", type(deck_of_cards)
print "number of cards:", len(deck_of_cards)
print "cards:", deck_of_cards
random.shuffle(deck_of_cards)
print "shuffled deck:", deck_of_cards

deal_hand(AI_hand, deck_of_cards)
deal_hand(players_hand, deck_of_cards)

print "AI_hand:", AI_hand
print "players_hand: ", players_hand
print "number of cards:", len(deck_of_cards)

print "card_value:", calculate_card_value(players_hand[0])
