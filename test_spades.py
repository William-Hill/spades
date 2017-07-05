import unittest
from collections import namedtuple
import spades

class test_SPADES(unittest.TestCase):
    TEST_HAND = [spades.Card('3', 'spades', 4), spades.Card('5', 'spades', 6), spades.Card('ace', 'spades', 15),spades.Card('3', 'hearts', 3), spades.Card('3', 'clubs', 1)]
    def setUp(self):
        spades.initialize_game()

    def test_generate_deck(self):
        deck = spades.generate_deck()
        print "deck: ", deck
        self.assertIsNotNone(deck)
        self.assertEqual(len(deck), 52)

    def test_sort_hand(self):
        sorted_hand = spades.sort_hand(self.TEST_HAND)
        print "sorted_hand: ", sorted_hand
        self.assertTrue(sorted_hand[0].value, 1)

    def test_players_hand(self):
        self.assertTrue(len(spades.players_hand), 5)

    def test_AI_hand(self):
        self.assertTrue(len(spades.AI_hand), 5)

    def test_AI_choose_card(self):
        print "spades.AI_hand:", spades.AI_hand
        player_card = spades.Card('7', 'diamonds', 6)
        sorted_hand = spades.sort_hand(self.TEST_HAND)
        chosen_card = spades.AI_choose_card(sorted_hand, player_card)

        self.assertEqual(chosen_card.value, 1)
        print "remaining hand: ", sorted_hand

        player_card = spades.Card('2', 'spades', 3)
        chosen_card = spades.AI_choose_card(sorted_hand, player_card)
        self.assertEqual(chosen_card.value, 4)
        print "remaining hand: ", sorted_hand

        #lowest card by the time this test comes
        chosen_card = spades.AI_choose_card(sorted_hand)
        self.assertEqual(chosen_card.value, 3)

    # def test_calculate_card_value(self):
    #     Card = namedtuple('Card', ['rank', 'suit'])
    #     test_card = Card('3', 'diamonds')
    #     self.assertTrue(spades.calculate_card_value(test_card), 2)

    def test_compare_cards(self):
        card_1 = spades.Card('3', 'spades')
        card_2 = spades.Card('3', 'hearts')
        spades.compare_cards(card_1, card_2)
        self.assertTrue(spades.players_books, 1)

    def test_find_cards_of_suit(self):
        output = spades.find_cards_of_suit("spades", self.TEST_HAND)
        self.assertTrue(len(output), 3)



if __name__ == '__main__':
    unittest.main()
