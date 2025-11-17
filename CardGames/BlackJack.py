import CardPile

class Dealer(CardPile.Hand):
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
    LEAVE = 'L'

    def __init__(self):
        self.deck = CardPile.CardPile()
        self.player = [CardPile.Hand()]
        self.dealer = Dealer()

    @staticmethod
    def count_total(hand: CardPile.Hand):
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

    def print_drawn_state(self, current: CardPile.Hand):
        """
        :return: Pseudographic UI of the game
        """
        print('|====================Black Jack====================|')
        print("  Dealer: ", self.dealer.show_drawn(), end='\n\n')
        for i in range(len(self.player)):
            if current == self.player[i]:
                print(" > ", end='' )
            print("Player: ", self.player[i], end='\n')
        print('|============(Dealer must take until 17)===========|', end='\n\n')

    def print_state(self):
        """
        :return: Pseudographic UI of the game
        """
        print('|====================Black Jack====================|')
        print("  Dealer: ", self.dealer, end='\n\n')
        for i in range(len(self.player)):
            print("Player: ", self.player[i], end='\n')
        print('|============(Dealer must take until 17)===========|', end='\n\n')

    def play(self):
        win = 0
        if RESHUFFLE_EVERY_ROUND:
            self.deck.reset()
            self.deck.shuffle()

        # Draw cards
        for i in range(2):
            for hand in self.player:
                hand.take(self.deck.draw())
            self.dealer.take(self.deck.draw())

        # Check for 21s
        d_count = BlackJack.count_total(self.dealer)
        p_count = BlackJack.count_total(self.player[0])
        if d_count == 21:
            self.print_state()
            if p_count == 21:
                print("Stay!".center(52, ' '))
                return
            else:
                print("Dealer won!".center(52, ' '))
                return
        else:
            if p_count == 21:
                self.print_state()
                print("You won!".center(52, ' '))
                return

        #Player moves
        for hand in self.player:
            self.print_drawn_state(hand)
            move = input(f"Type {BlackJack.HIT} to HIT, {BlackJack.DOUBLE} to DOUBLE, {BlackJack.SPLIT} to SPLIT or ANY to Stay!\n")
            while move == BlackJack.HIT or move == BlackJack.DOUBLE or move == BlackJack.SPLIT:
                if move == BlackJack.HIT:
                    hand.take(self.deck.draw())
                    self.print_drawn_state(hand)
                    if BlackJack.count_total(hand) > 21:
                        print("Busted!".center(52, ' '))
                        break
                    move = input(f"Type {BlackJack.HIT} to HIT, {BlackJack.DOUBLE} to DOUBLE, {BlackJack.SPLIT} to SPLIT or ANY to Stay!\n")

                if move == BlackJack.DOUBLE:
                    if hand.get_size() > 2:
                        print("You can only double after first draw!")
                        move = input(f"Type {BlackJack.HIT} to HIT, {BlackJack.DOUBLE} to DOUBLE, {BlackJack.SPLIT} to SPLIT or ANY to Stay!\n")
                    else:
                        hand.take(self.deck.draw())
                        self.print_drawn_state(hand)
                        if BlackJack.count_total(hand) > 21:
                            print("Busted!".center(52, ' '))
                        break

                if move == BlackJack.SPLIT:
                    if hand.get_size() > 2:
                        print("You can only split after first draw!")
                        move = input(f"Type {BlackJack.HIT} to HIT, {BlackJack.DOUBLE} to DOUBLE, {BlackJack.SPLIT} to SPLIT or ANY to Stay!\n")
                    else:
                        if (hand.get_hand()[0].get_rank() != hand.get_hand()[1].get_rank()) and not (hand.get_hand()[0].get_rank() >= 10 and hand.get_hand()[1].get_rank() >= 10):
                            print("You can only split two cards of same rank!")
                            move = input(f"Type {BlackJack.HIT} to HIT, {BlackJack.DOUBLE} to DOUBLE, {BlackJack.SPLIT} to SPLIT or ANY to Stay!\n")
                        else:
                            self.player.append(CardPile.Hand())
                            self.player[-1].take(self.player[-2].retract())
                            self.player[-2].take(self.deck.draw())
                            self.player[-1].take(self.deck.draw())
                            self.print_drawn_state(hand)
                            move = input(f"Type {BlackJack.HIT} to HIT, {BlackJack.DOUBLE} to DOUBLE, {BlackJack.SPLIT} to SPLIT or ANY to Stay!\n")


        # Dealer moves
        while BlackJack.count_total(self.dealer) < 17:
            self.dealer.take(self.deck.draw())
        self.print_state()

        # Results
        d_count = BlackJack.count_total(self.dealer)
        p_count = [BlackJack.count_total(hand) for hand in self.player]

        if len(p_count) == 1:
            if p_count[0] > 21:
                print("You busted!".center(52, ' '))
            else:
                if p_count[0] > d_count:
                    print("You won!".center(52, ' '))
                elif p_count[0] == d_count:
                    print("Stay!".center(52, ' '))
                else:
                    print("Dealer won!".center(52, ' '))
        else:
            for i in range(len(p_count)):
                if p_count[i] > 21:
                    print(f"Hand {i + 1}: busted!".center(52, ' '))
                if p_count[i] > d_count:
                    print(f"Hand {i + 1}: you won!".center(52, ' '))
                elif p_count[i] == d_count:
                    print(f"Hand {i + 1}: stay!".center(52, ' '))
                else:
                    print(f"Hand {i + 1}: dealer won!".center(52, ' '))



RESHUFFLE_EVERY_ROUND = True
bj = BlackJack()
while True:
    bj.play()
    bj.dealer.clear()
    for i in range(len(bj.player)):
        if i == 0:
            bj.player[i].clear()
        else:
            bj.player.pop(i)
    if input(f"Type {BlackJack.LEAVE} to leave") == BlackJack.LEAVE:
        break