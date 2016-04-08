__author__ = 'CodeClub'

from card import Card
from hand import Hand

class Player(object):

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit

    def turn(self, hand):
        while hand.total < self.limit and not hand.is_bust:
            hand.add_card(Card.generate())


