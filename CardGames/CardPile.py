class Card:
    SUITS = [
        "Hearts",
        "Spades",
        "Diamonds",
        "Clubs"
    ]

    RANKS = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    SUITS_COUNT = 4
    RANKS_COUNT = 13

    def __init__(self, rank: int, suit: int):
        self.__suit__ = suit
        self.__rank__ = rank

    def get_suit(self) -> int:
        return self.__suit__

    def get_rank(self) -> int:
        return self.__rank__

    def __str__(self):
        return f"{self.RANKS[self.get_rank()]} of {self.SUITS[self.get_suit()]}"

    def __repr__(self):
        return self.__str__()



class CardPile:
    def __init__(self):
        self.__pile__ = []
        for rank in range(1, Card.RANKS_COUNT):
            for suit in range(Card.SUITS_COUNT):
                self.__pile__.append(Card(rank, suit))
        self.__size__ = len(self.__pile__)

    def is_not_empty(self) -> bool:
        return self.__size__ > 0

    def get_pile(self) -> list:
        """
        :return: List of cards in pile
        """
        return self.__pile__.copy()

    def get_size(self) -> int:
        """
        :return: Current quantity of cards in pile.
        """
        return self.__size__

    def shuffle(self):
        """
        Shuffles current pile
        :return: None
        """
        from random import randint
        new_pile = []
        while len(self.__pile__) > 0:
            new_pile.append(self.__pile__.pop(randint(0, len(self.__pile__) - 1)))
        self.__pile__ = new_pile
        print("Riffle shuffle!")

    def draw(self) -> Card:
        """
        Takes out the top card from pile. Used in pair with Hand.take()
        :return: The taken card
        """
        if self.__size__ < 1:
            raise ValueError("Could not draw from clear pile!")
        self.__size__ -= 1
        return self.__pile__.pop(0)

    def reset(self):
        """
        Resets current pile to default. Needs to be reshuffled after.
        :return:
        """
        self.__pile__ = []
        for rank in range(1, Card.RANKS_COUNT):
            for suit in range(Card.SUITS_COUNT):
                self.__pile__.append(Card(rank, suit))
        self.__size__ = len(self.__pile__)
        print("Deck reset!")

    def __str__(self):
        return ', '.join([str(card) for card in self.__pile__])


class Hand:
    def __init__(self):
        self.__hand__ = []

    def get_hand(self) -> list:
        """
        :return: List of cards in hand
        """
        return self.__hand__.copy()

    def take(self, card: Card) -> Card:
        """
        Adds given card to hand. Used in pair with CardPile.draw()
        :param card: Given card
        :return: The same card
        """
        self.__hand__.append(card)
        return card

    def clear(self):
        """
        Removes all cards from hand
        :return:
        """
        self.__hand__.clear()
    def get_size(self):
        """
        :return: Quantity of cards in hand
        """
        return len(self.__hand__)

    def retract(self):
        """
        :return: Last card, also removing it form hand
        """
        return self.__hand__.pop(-1)

    def __str__(self):
        return ', '.join([str(card) for card in self.__hand__])