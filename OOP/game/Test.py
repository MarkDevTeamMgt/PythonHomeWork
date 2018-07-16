
from OOP.game.util.PlayGround import PlayGround

from OOP.game.cards.CardGenerator import CardGenerator
from OOP.game.players.Player import Player

def initGame():

    cardQueue = []
    players = []

    players.append(Player(3, 'Palyer1', 'zhugong'))
    print 'Palyer 1 join game with 3 HP'
    players.append(Player(3, 'Palyer2', 'zhongchen'))
    print 'Palyer 2 join game with 3 HP'
    players.append(Player(3, 'Palyer3', 'neijian'))
    print 'Palyer 3 join game with 3 HP'
    players.append(Player(3, 'Palyer4', 'fanzei'))
    print 'Palyer 4 join game with 3 HP'

    generator = CardGenerator(players)


    for i in range(0, 52):
        newCard = generator.CardGenerate(i)
        print 'add new card with: '+newCard.name
        cardQueue.append(newCard)

    for player in players:
        for i in range(0, 4):
            player.handCard.append(cardQueue.pop())
            print player.name,' get ',len(player.handCard),' cards'


    return players,cardQueue



if __name__ == '__main__':
    playerList, cards = initGame()
    playGround = PlayGround(playerList,cards)
    playGround.onGoingGame()



