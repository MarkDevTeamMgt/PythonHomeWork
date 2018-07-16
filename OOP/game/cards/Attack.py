


from OOP.game.cards.Card import Card

class Attack(Card):

    def __init__(self,number,players):
        self.name = 'attack'
        self.number = number
        self.targetList = players
        self.target = None
        self.source = None


    def choiceTarget(self, player):

        self.source = player
        if self.source.exeAttack is True:
            print 'only attack one time within one turn'
        else:
            print 'please choice target'
            for i in range(0, len(self.targetList)):
                if self.source != self.targetList[i]:
                    print i + 1, '. ', self.targetList[i].name
            index = int(raw_input())
            self.target = self.targetList[index - 1]


    def action(self):
        if self.source.exeAttack == False:
            print self.source.name,' attack ', self.target.name
            print 'attack!! '
            self.source.exeAttack = True
            self.target.defense()
            return True
        else:
            False
