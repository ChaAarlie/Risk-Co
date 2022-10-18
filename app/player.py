# Our player class
from bee import Bee
class Player(object):
    # can only attack for now -> future : addPlayer HP and bee.attack
    winNumber = 0
    def attack(self, Bee):
        Bee.hp -= Bee.hit
        print ("You've hit the " + Bee.name + " bee for " + str(Bee.hit) + "hp")
