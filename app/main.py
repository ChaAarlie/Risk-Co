import os
import sys
import random
from player import Player
from bee import QueenBee, WorkerBee, DroneBee

def main() -> int:
    player = Player()
    beeArray = [QueenBee(),WorkerBee(),WorkerBee(),WorkerBee(),WorkerBee(),WorkerBee(), DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee(),DroneBee()]
    # print("Press 'y' to play or 'n' to quit : ")
    while len(beeArray) > 0 :
        action = input("Attack (a) Quit (q) Stats (s) \n")
        if action == "a":
            rand = random.randint(0,len(beeArray)-1)
            player.attack(beeArray[rand])
            if beeArray[rand].hp <= 0 :
                if rand == 0 : ## if queen dies kill all bees
                    print ("You've killed the Queen, all other bees die alongside her")
                    beeArray.clear()
                else :
                    print("You've killed a " + beeArray[rand].name + " bee")
                    print(str(len(beeArray)) + " bees left")
                    beeArray.pop(rand)
            else :
                print(str(beeArray[rand].hp) + " HP left" )
        if action == "q":
            break
        if action == "s":
            print(str(len(beeArray)) + " bees left")
            print("The queen has " + str(beeArray[0].hp) + " HP")
        
    if (len(beeArray) == 0 ):
        print ("You've killed all the bees :( ")
        player.winNumber += 1

    playAgain = input("Play again ? (y/n)") 
    if playAgain == "y" :
        os.execl(sys.executable, sys.executable, *sys.argv)
    else :
        exit
    

if __name__ == '__main__':
    sys.exit(main()) 