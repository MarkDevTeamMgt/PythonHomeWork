import random

from OOP.game.cards.Attack import Attack
from OOP.game.cards.Flash import Flash
from OOP.game.cards.Peach import Peach


class CardGenerator:

    def __init__(self, players):
        self.players = players



    def CardGenerate(self,num):
        option = random.randint(0,2)
        if option == 0:
            return Attack(num, self.players)
        elif option == 1:
            return Flash(num)
        else:
            return Peach(num)
