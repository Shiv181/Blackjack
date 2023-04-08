import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return F"{self.rank['rank']}  of {self.suit}"


class Deck:
    def __init__(self):
        self.deck_cards = []
        suits = ["spades", "hearts", "diamonds", "clubs"]
        ranks = [{"rank": "A", "value": 11},
                 {"rank": "2", "value": 2},
                 {"rank": "3", "value": 3},
                 {"rank": "4", "value": 4},
                 {"rank": "5", "value": 5},
                 {"rank": "6", "value": 6},
                 {"rank": "7", "value": 7},
                 {"rank": "8", "value": 8},
                 {"rank": "9", "value": 9},
                 {"rank": "10", "value": 10},
                 {"rank": "J", "value": 10},
                 {"rank": "Q", "value": 10},
                 {"rank": "K", "value": 10},
                 {"rank": "A", "value": 11}]

        for suit in suits:
            for rank in ranks:
                self.deck_cards.append(Card(suit, rank))

    def shuffle(self):
        if len(self.deck_cards) > 1:
            random.shuffle(self.deck_cards)

    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.deck_cards) > 0:
                card = self.deck_cards.pop()
                cards_dealt.append(card)
        return cards_dealt


class Hand:
    def __init__(self, dealer=False):
        self.deck_cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.deck_cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        self.hand_has_ace = False
        for card in self.deck_cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                self.hand_has_ace = True

        if self.hand_has_ace and self.value > 21:
            self.value -= 10  # Same thing as setting the Ace to one (for ex 21-10 = 1)

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        if self.get_value() == 21:
            return True
        else:
            return False

    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's Hand" if self.dealer else "Your"} Hand:''')
        for index, card in enumerate(self.deck_cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)

        if not self.dealer:
            print("Value", self.get_value())
        print()
