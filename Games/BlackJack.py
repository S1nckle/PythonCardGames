from CardGames.GameSets import Cards

class Dealer(Cards.Hand):
    def __init__(self):
        super().__init__()

    def show_drawn(self):
        """
        Show cards when given with one closed
        :return:
        """
        return f"{self.get_hand()[0]}, ?"

class BlackJack:
    HIT = 'H'
    SPLIT = 'S'
    DOUBLE = 'D'

    def __init__(self):
        self.deck = Cards.CardPile()
        self.player = Cards.Hand()
        self.dealer = Dealer()

    @staticmethod
    def count_total(hand: Cards.Hand):
        """
        :param hand: Hand to count
        :return: Total score of given hand via rules of Black Jack
        """
        total = 0
        aces = 0

        for card in hand.get_hand():
            if card.get_rank() > 1:
                total += min(10, card.get_rank())
            else:
                aces += 1
        if aces > 0:
            total += aces - 1
            total += 11 if total <= 10 else 1

        return total

    def print_drawn_state(self):
        """
        :return: Pseudographic UI of the game
        """
        print('|====================Black Jack====================|')
        print("Dealer: ", self.dealer.show_drawn(), end='\n\n')
        print("Player: ", self.player, end='\n')
        print('|============(Dealer must take until 17)===========|', end='\n\n')

    def print_state(self):
        """
        :return: Pseudographic UI of the game
        """
        print('|====================Black Jack====================|')
        print("Dealer: ", self.dealer, end='\n\n')
        print("Player: ", self.player, end='\n')
        print('|============(Dealer must take until 17)===========|', end='\n\n')

    def play(self, bet=0):
        doubled = False
        for i in range(2):
            self.dealer.take(self.deck.draw())
            self.player.take(self.deck.draw())
        self.print_drawn_state()

        drawn_player = BlackJack.count_total(self.player)
        drawn_dealer = BlackJack.count_total(self.dealer)

        if drawn_player == 21:
            self.print_state()
            if drawn_dealer == 21:
                print("Stay!".center(52, ' '))
                return
            else:
                print("You won!".center(52, ' '))
                return
        elif drawn_dealer == 21:
            self.print_state()
            print("Dealer won!".center(52, ' '))
            return


        move = input('Type H to HIT, D to DOUBLE, S to SPLIT and ANY to STAY: \n')

        while move == BlackJack.HIT or move == BlackJack.DOUBLE or move == BlackJack.SPLIT:
            if move == BlackJack.HIT:
                self.player.take(self.deck.draw())
                self.print_drawn_state()
                if BlackJack.count_total(self.player) <= 21:
                    move = input('Type H to HIT, D to DOUBLE, S to SPLIT and ANY to STAY: \n')
                else:
                    self.print_state()
                    print("Dealer won!".center(52, ' '))
                    return
            if move == BlackJack.DOUBLE:
                self.player.take(self.deck.draw())
                doubled = True
                break
            if move == BlackJack.SPLIT:
                print("We don't split.\n")
                move = input('Type H to HIT, D to DOUBLE, S to SPLIT and ANY to STAY: \n')


        while BlackJack.count_total(self.dealer) < 17:
            self.dealer.take(self.deck.draw())
        self.print_state()

        dealer_total = BlackJack.count_total(self.dealer)
        if dealer_total > 21:
            print("You won!".center(52, ' '))
            return

        player_total = BlackJack.count_total(self.player)
        if player_total > dealer_total:
            print("You won!".center(52, ' '))
        elif player_total < dealer_total:
            print("Dealer won!".center(52, ' '))
        else:
            print("Stay!".center(52, ' '))
        return



def main(money: int):
    """
    :param money: Start money
    """
    from random import randint
    bj.deck.shuffle()
    if not RESHUFFLE_EVERY_ROUND:
        cut = randint(bj.deck.get_size() // 4, bj.deck.get_size() // 2)

    while True:
        bet = 0
        if BETS:
            bet = int(input("Place your bet: "))
        if not RESHUFFLE_EVERY_ROUND:
            if bj.deck.get_size() < cut:
                bj.deck.reset()
                bj.deck.shuffle()
                cut = randint(bj.deck.get_size() // 4, bj.deck.get_size() // 2)
        else:
            bj.deck.reset()
            bj.deck.shuffle()

        bj.play(bet)
        bj.player.clear()
        bj.dealer.clear()
        if input("L to Leave, ANY to continue\n\n") == 'L':
            print("Thanks for game.")
            break


bj = BlackJack()
BETS = False
RESHUFFLE_EVERY_ROUND = False
main(1000)