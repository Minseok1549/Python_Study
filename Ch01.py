import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
# namedtuple ( '객체이름', ['attributes'] )

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

card = Card('7', 'diamonds')
print(card)

# index 와 attribute 로 접근이 가능
print(card[0], card[1], card.rank, card.suit)

deck = FrenchDeck()
print(len(deck))

# getitem 에서 제공하는 index 로 인해 호출 가능
for i in range(5):
    print(deck[i])

from random import choice
print(choice(deck))

# __contains__() 메서드의 존재로 in 연산자로 검색이 가능
print(Card('Q', 'bearts') in deck)

suit_values = dict(
    spades=3,
    hearts=2,
    diamonds=1,
    clubs=0
)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

print(spades_high(card))

for card in sorted(deck, key=spades_high):
    print(f"The rank of {card} is {spades_high(card)}.")

from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)