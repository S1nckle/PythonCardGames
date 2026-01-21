class Dice:
    def __init__(self, sides: int):
        self.__sides__ = sides

    def get_sides(self) -> int:
        return self.__sides__

    def throw(self) -> int:
        from random import randint
        return randint(1, self.__sides__)

class Hand:
    """
    Carries given array of dice and last throw.
    """
    def __init__(self, dice: list):
        """
        :param dice: List of dices
        """

        self.__hand__ = dice
        self.__last_throw = [None for i in range(len(dice))]

    def get_hand(self):
        return self.__hand__.copy()

    def throw(self, which:list):
        throw = []
        for i in range(len(self.__hand__)):
            if i in which:
                throw.append(self.__hand__[i].throw())
            else:
                throw.append(self.__last_throw[i])
        self.__last_throw = throw
        return throw

    def throw_all(self) -> list:
        self.__last_throw = [dice.throw() for dice in self.get_hand()]
        return self.__last_throw

    def get_last_throw(self):
        return self.__last_throw

    def clear(self):
        """
        Nullifies stats.
        """
        self.__last_throw = [None for i in range(len(self.get_hand()))]



