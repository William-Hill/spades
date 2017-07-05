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

def generate_deck():
    cards = [Card(rank, suit, calculate_card_value(rank,suit)) for rank in RANKS for suit in SUITS]
    return cards

def deal_hand(hand_list, deck):
    for _ in range(5):
        item = deck.pop()
        print "item:", item
        hand_list.append(item)

def calculate_card_value(rank, suit):
    #TODO: Add multiplier for spades suit
    # print "card:", card
    # rank = RANKS.index(card.rank)
    rank_value = RANKS.index(rank)
    # print "rank:", rank
    # print "{rank} rank_value: {rank_value}".format(rank=rank, rank_value=rank_value)
    # suit = SUITS.index(card.suit)
    suit_value = SUITS.index(suit)
    # print "suit:", suit
    # print "{suit} suit_value: {suit_value}".format(suit=suit, suit_value=suit_value)
    # return rank + suit
    print "{rank} of {suit} = {value}".format(rank=rank, suit=suit, value=rank_value + suit_value)
    return rank_value + suit_value

def getKey(hand):
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
    if card_1_value > card_2_value:
        print "player won book"
        players_books +=1
    else:
        print "AI won book"
        AI_books +=1

def initialize_game():
    global AI_hand
    deck_of_cards = generate_deck()
    print "deck_of_cards type: ", type(deck_of_cards)
    print "number of cards:", len(deck_of_cards)
    print "cards:", deck_of_cards
    random.shuffle(deck_of_cards)
    print "shuffled deck:", deck_of_cards

    deal_hand(AI_hand, deck_of_cards)
    AI_hand = sort_hand(AI_hand)
    deal_hand(players_hand, deck_of_cards)


def find_cards_of_suit(suit, hand):
    cards_of_suit = [card for card in hand if card.suit == suit]
    return cards_of_suit


def AI_choose_card(hand, players_card = None):
    # sorted_AI_hand = sort_hand(AI_hand)
    # print "sorted_AI_hand: ", sorted_AI_hand
    if players_card:
        # players_card_value = calculate_card_value(players_card.rank, players_card.value)
        print "players_card_value: ", players_card.value
        # temp_card = None
        temp_card = hand[0]
        # same_suit_cards = find_cards_of_suit(players_card.suit, AI_hand)
        #loop through list looking for card of same suit
        for index, card in enumerate(hand):
        #if card is found of same suit, set as temp card
            if card.suit == players_card.suit:
                temp_card = card
                if card.value > players_card.value:
                    break
                else:
                    continue
        #if card of same suit is not found, set temp card to card with a higher value than player card
            if not temp_card and card.value > players_card.value:
                temp_card = card
                continue
        #if no card is higher than player card, set temp card to lower card in hand
        chosen_card_index = hand.index(temp_card)
        print "chosen_card_index: ", chosen_card_index
        chosen_card = hand.pop(chosen_card_index)
        print "chosen_card:", chosen_card
        return chosen_card
    else:
        chosen_card = hand.pop(0)
        return chosen_card



    # card_values = []
    # for card in AI_hand:
    #     value = calculate_card_value(card)
    #     card_values.append(value)
    # if not spades_cut:
    #     playable

initialize_game()
#TODO: log AI_hand to a file with timestamp and unique gameID and/or timestamp
print "AI_hand:", AI_hand
print "players_hand: ", players_hand
# print "number of cards:", len(deck_of_cards)

# print "card_value:", calculate_card_value(players_hand[0])
