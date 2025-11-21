from CardGames.GameSets import Dice

class DicePoker:
    GOAL = 100
    def __init__(self):
        self.player = Dice.Hand([Dice.Dice(6) for i in range(5)])
        self.bot = Dice.Hand([Dice.Dice(6) for i in range(5)])
        self.player_score = 0
        self.bot_score = 0

    def print_stage(self):
        print("|======Dice Game======|")
        print(' '.join(self.bot.get_last_throw()).center(23, ' '))
        print()
        print(' '.join(self.player.get_last_throw()).center(23, ' '))
        print("|=====================|")

    def play(self):

