
class NaivePlayer():
    def __init__(self):
        self.Hand = []
        self.name = "Naive Player"
        self.wins = 0

    def draw(self):
        card = self.Hand[0]
        A.remove(card)
        return card

    def replace(l):
        for card in l:
            self.Hand.append(card)


class OrderPlayer():
    def __init__(self):
        self.Hand = []
        self.name = "Smart Player"
        self.wins = 0

    def draw(self):
        card = self.Hand[0]
        A.remove(card)
        return card

    def replace(l):
        for card in sorted(l)[::-1]:
            self.Hand.append(card)
