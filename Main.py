from Bot import Bot
from Game import Game

bot1 = Bot(7,[2,3,4])
bot2 = Bot(7,[2,3,4])

game = Game(bot1, bot2)

game.run()