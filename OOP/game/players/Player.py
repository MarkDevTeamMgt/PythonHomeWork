


from OOP.game.cards import Card


class Player:

    def __init__(self,HP,name,status):
        self.HP = HP
        self.maxHP = HP
        self.name = name
        self.status = status
        self.weapon = None
        self.handCard = []
        self.exeAttack = False


    def pick(self, cardQueue):
        print self.name+' pick two cards from card queue HP: '+str(self.HP)
        self.handCard.append(cardQueue.pop())
        self.handCard.append(cardQueue.pop())


    def waive(self, WaiveCardQueue):
        self.exeAttack = False
        while len(self.handCard) > self.HP:
            print 'please waive handcard until equal to rest HP'
            for i in range(0,len(self.handCard)):
                print str(i+1)+'. '+self.handCard[i].name
            index = int(raw_input())
            WaiveCardQueue.append(self.handCard[index-1])
            del self.handCard[index-1]



    def play(self, WaiveCardQueue):
        print 'your turn, please choice card:'
        option = 0
        while option != -1:
            for i in range(0,len(self.handCard)):
                print str(i+1),'. '+self.handCard[i].name
            print '-1. stop play phase'
            option = int(raw_input())
            if option != -1:
                if self.handCard[i].name is 'flash':
                    print 'not able use flash on your turn'
                else:
                    self.handCard[option-1].choiceTarget(self)
                    if self.handCard[option-1].action() is True:
                        WaiveCardQueue.append(self.handCard[option - 1])
                        del self.handCard[option-1]



    def defense(self):
        num = -1
        for i in range(0,len(self.handCard)):
            if self.handCard[i].name is 'flash':
                self.handCard[i].action()
                num = i
                break

        if num != -1:
           del self.handCard[num]
        else:
            self.HP = self.HP -1
            print self.name,' under attack rest HP: ',str(self.HP)

        # if self.HP == 0:
        #    if  PlayGround.askPeach() is True:
        #        self.HP +1


        # if save == False:
        #     print 'player: '+self.name+' died'
        #     PlayGround.getCurrentPlayer().remove(self)


    def hasPeach(self):
        num = -1
        for i in range(0,len(self.handCard)):
            if self.handCard[i].name is 'peach':
                print self.name,' want to save your?'
                print  '1. Yes'
                print  '2. No'
                option = int(raw_input())
                if option == 1:
                    num = i
                break
        if num != -1:
            del self.handCard[num]
            return True
        return False










