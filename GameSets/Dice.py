class Dice:
    def __init__(self, sides: int):
        self.__sides__ = sides

    def get_sides(self) -> int:
        return self.__sides__

    def throw(self) -> int:
        from random import randint
        return randint(1, self.__sides__)

class Hand:
    def __init__(self, dice: list):
        """
        :param dice: List of dices
        """

        self.__hand__ = dice
        self.__last_throw = [0 for i in range(dice)]
        self.__score = 0

    def get_hand(self):
        return self.__hand__.copy()

    def throw(self) -> list:
        '''
        Throw all dice in hand
        :return:
        '''
        self.__last_throw = [dice.throw() for dice in self.get_hand()]
        return self.__last_throw

    def get_last_throw(self):
        return self.__last_throw

    def get_score(self):
        return self.__score

    def add_score(self, value: int):
        self.__score += value
        return self.__score

    def clear(self):
        self.__score = 0
        self.__last_throw = [0 for i in range(len(self.get_hand()))]



