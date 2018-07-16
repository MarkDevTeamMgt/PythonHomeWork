
from OOP.game.cards.Card import Card

class Flash(Card):

    def __init__(self, number):
        self.name = 'flash'
        self.number  = number


    def action(self):
        print 'flash!!'