from random import shuffle
import players

class War():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        deck = range(2,15)*4
        shuffle(deck)

        def _draw(player1, player2, inplay):
            card1 = player1.draw()
            card2 = player2.draw()

            inPlay.append(card1)
            inPlay.apennd(card2)

            if card1 > card2:
                player1.replace(inPlay)
            elif card2 > card1:
                player2.replace(inPlay)
            else:
                for i in range(3):
                    inPlay.append(player1.draw())
                for i in range(3):
                    inPlay.append(player2.draw())
                _draw(player1, player2, inPlay)


        while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            inPlay = []
            _draw(player1, player2, inPlay)

        if len(self.player1.hand) > 0:
            self.player1.wins += 1
        else:
            self.player2.wins += 1
