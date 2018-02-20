from random import shuffle
import time

class NaivePlayer():
    def __init__(self):
        self.hand = []
        self.name = "Naive Player"
        self.wins = 0

    def draw(self):
        card = self.hand[0]
        self.hand.remove(card)
        return card

    def replace(self, l):
        for card in l:
            self.hand.append(card)


class OrderPlayer():
    def __init__(self):
        self.hand = []
        self.name = "Smart Player"
        self.wins = 0

    def draw(self):
        card = self.hand[0]
        self.hand.remove(card)
        return card

    def replace(self, l):
        for card in sorted(l):
            self.hand.append(card)


class War():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        self.player1.hand = []
        self.player2.hand = []
        deck = range(2,15)*4
        shuffle(deck)

        for i in range(26):
            self.player1.hand.append(deck.pop())
            self.player2.hand.append(deck.pop())

        #print len(self.player1.hand), len(self.player2.hand)

        def _draw(player1, player2, inPlay, card1 = 2, card2 = 2):
            if len(self.player1.hand) > 0:
                card1 = player1.draw()
                inPlay.append(card1)
            if len(self.player2.hand) > 0:
                card2 = player2.draw()
                inPlay.append(card2)


            if card1 > card2:
                player1.replace(inPlay)
            elif card2 > card1:
                player2.replace(inPlay)
            else:
                for i in range(3):
                    if len(self.player1.hand) > 1:
                        inPlay.append(player1.draw())
                for i in range(3):
                    if len(self.player2.hand) > 1:
                        inPlay.append(player2.draw())

                _draw(player1, player2, inPlay, card1, card2)

        start = time.time()
        finished = True
        while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            inPlay = []
            _draw(self.player1, self.player2, inPlay)
            if time.time() - start > 1:
                finished = False
                break
            #print len(self.player1.hand), len(self.player2.hand)

        #print len(self.player1.hand), len(self.player2.hand)
        if finished:
            if len(self.player2.hand) > 0:
                self.player1.wins += 1
            else:
                self.player2.wins += 1

if __name__ == "__main__":
    player = NaivePlayer()
    player2 = NaivePlayer()
    smartPlayer = OrderPlayer()

    game = War(player, player2)

    for i in range(1000):
        game.play()

    print player.name, ": ", player.wins, " wins; ", player2.name, ": ", player2.wins, " wins."
