from player import Player
from variants import Variants

bot = Player()

alex = Player(Variants.PAPER, 'Alex')

print(bot.whoWins(bot, alex))
