

import Card



from OOP.game.cards.Card import Card

class Peach(Card):


    def __init__(self, number):
        self.name = 'peach'
        self.number = number
        self.target = None



    def choiceTarget(self, player):
        self.target = player

    def action(self):
        print 'Use peach to cure players '
        player = self.target
        if player.HP < player.maxHP:
            player.HP = player.HP+1
            print 'now current player with HP: '+ str(player.HP)
            return True
        else:
            print 'current player has full HP'
            return False


