

import random



class PlayGround:

    cardQueue = []
    waiveCardQueue = []
    players = []
    currentPlayer = None


    def __init__(self, playerList, cardQueue):
        self.cardQueue = cardQueue
        self.players = playerList


    def onGoingGame(self):
        while len(self.players) > 1:
            for player in self.players:
                self.currentPlayer = player
                if len(self.cardQueue) < 2:
                    self.washCards()
                player.pick(self.cardQueue)
                player.play(self.waiveCardQueue)
                player.waive(self.waiveCardQueue)
                self.checkLive()



    def washCards(self):
        while len(self.waiveCardQueue) !=0:
            num = len(self.waiveCardQueue)
            index = random.randint(0,num)
            self.cardQueue.append(self.waiveCardQueue[index])
            del self.waiveCardQueue[index]


    def GameSummay(self):
        print self.players[0].name,' win and status is ', self.players[0].status



    @classmethod
    def askPeach(cls):
        for palyer in cls.players:
            print 'ask player help: ',palyer.name
            if palyer.hasPeach() is True:
                return True
        return False


    def checkLive(self):
        for palyer in self.players:
            if palyer.HP == 0:
                self.players.remove(palyer)
                print 'player :' ,palyer.name,' died'