__author__ = 'CodeClub'
from player import Player
from hand import Hand
from card import Card

def play(player):
    hand = Hand()
    hand.add_card(Card.generate())
    hand.add_card(Card.generate())

    player.turn(hand)
    return hand

def main():
    house = Player('house',18)
    house_hand = play(house)

    players = [Player('Ahsan', 11), Player('Deva', 20), Player('Menno', 19)]
    for player in players:
        hand = play(player)
        wins = ""
        if house_hand.is_bust and not hand.is_bust:
            wins = player.name + ' wins'
        elif not house_hand.is_bust and hand.is_bust:
            wins = "house wins"
        elif house_hand.is_bust and hand.is_bust:
            wins = "both lose"
        elif house_hand.total <= hand.total:
            wins = player.name + " wins"
        else:
            wins = "house wins"


        print("%s:%d %s - %s" %(player.name, hand.total, hand, wins))

    print("%s:%d %s" %(house.name, house_hand.total, house_hand))






if __name__ == "__main__":
    for i in range(5):
        main()
        print("="*20)