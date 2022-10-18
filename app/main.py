import os
import sys
import random
from bee import QueenBee, WorkerBee, DroneBee

def main() -> int:

    beeArray = [QueenBee(),WorkerBee(),WorkerBee(),WorkerBee(),WorkerBee(),WorkerBee(), DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee()]
    while len(beeArray) > 0 :
        attack = input("attack?")
        if (attack == ("y")):
            rand = random.randint(0,len(beeArray)-1)
            beeArray[rand].hp -= beeArray[rand].hit
            print ("You've hit the " + beeArray[rand].name + " bee for " + str(beeArray[rand].hit) + "hp")
            if beeArray[rand].hp <= 0 :
                if rand == 0 : ## if queen dies kill all bees
                    print ("You've killed the Queen, all other bees die alongside her")
                    beeArray.clear()
                else :
                    print("You've killed a " + beeArray[rand].name + " bee")
                    beeArray.pop(rand)
            else :
                print(str(beeArray[rand].hp) + " HP left" )
                 
    print ("You've killed all the bees :( ")
    playAgain = input("Play again ? (y/n)") 
    if playAgain == "y" :
        os.execl(sys.executable, sys.executable, *sys.argv)
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit