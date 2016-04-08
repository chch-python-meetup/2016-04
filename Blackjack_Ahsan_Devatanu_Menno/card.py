__author__ = 'CodeClub'

import random

SUITES = ['\u2660', '\u2665', '\u2666', '\u2663']
VALUES = range(1, 14)


class Card(object):

    def __init__(self, suite, value):
        self.suite = suite
        self._value = value

    def __str__(self):
        return self.value_str()+self.suite

    @property
    def value(self):
        return min(10, self._value)

    def value_str(self):
        if self.value == 1:
            return 'A'
        elif self.value < 11:
            return str(self.value)
        elif self.value == 11:
            return 'J'
        elif self.value == 12:
            return 'Q'
        elif self.value == 13:
            return 'K'
        else:
            raise ValueError('Unknown Value %d' % self.value)


    @classmethod
    def generate(cls):
        return cls(random.choice(SUITES), random.choice(VALUES))


if __name__ == '__main__':
    for i in range(50):
        print(Card.generate())