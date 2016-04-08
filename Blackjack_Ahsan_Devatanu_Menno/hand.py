__author__ = 'CodeClub'

class Hand(object):

    def __init__(self):
        self.cards = []

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

    def add_card(self, card):
        self.cards.append(card)

    @property
    def total(self):
        totals = _calc_totals(0, self.cards)
        viable_totals = [total for total in totals if total <= 21]
        if not viable_totals:
            return min(totals)
        return max(viable_totals)

    @property
    def is_bust(self):
        return self.total > 21


def _calc_totals(total, cards):
    totals = []
    cards = list(cards)
    while cards:
        card = cards.pop()
        if card.value == 1:
            total += 1
            totals.extend(_calc_totals(total+11, cards))
        else:
            total += card.value
    totals.append(total)
    return totals

if __name__ == "__main__":
    from card import Card

    for _ in range(4):
        h = Hand()
        for i in range(3):
            h.add_card(Card.generate())

        print(h)
        print(h.total)
        print(h.is_bust)