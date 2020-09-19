from Bot import Bot
from Game import Game

bot1 = Bot(4,[2])
bot2 = Bot(4,[2])

game = Game(bot1, bot2)

game.run()