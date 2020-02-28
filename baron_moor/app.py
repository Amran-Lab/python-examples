#!/usr/bin/env python3

import random
from CalculatePosition import *
from Dial import Dial 
from GameBoard import * 
from HiddenTreasures import *
from Movement import *
from Navigation import * 
from PlayerPosition import *
from Trap import *
from TreasurePosition import *
import sys

def main():

    viewing = None
    option = None
    toGo = None
    toGoCondition = True
    playerXPosition = None
    playerYPosition = None
    treasureXPosition = None
    treasureYPosition = None
    hiddenXPosition = None
    hiddenYPosition = None
    trapX = None
    trapY = None
    con = True
    positionMatching = True

    while con:
        print("You awaken to find yourself in a barren moor. Try \"look\"")
        viewing = input().lower()

        if viewing == "look":
            print("Grey foggy clouds float oppressively close to you,\n" +
                        "reflected in the murky grey water which reaches up your\n" +
                        "shins.\n" +
                        "Some black plants barely poke out of the shallow water.")
            con = False
        else:
            print("You have entered an incorrect statement, \n" +
                        "do you wish to exit the viewing?, \n" +
                        "Please enter either \"Yes\" or \"No\"")

            option = input().lower()

            if option == "yes":
                con = False
            elif option =='no':
                sys.exit('You have chosen not to play')
            else:
                print('You have put something invalid')
                pass

    playerPosition = PlayerPosition()
    treasurePosition = TreasurePosition()
    hiddenTreasures = HiddenTreasures()
    trap = Trap()

    playerXPosition = playerPosition.calculateXPosition()
    playerYPosition = playerPosition.calculateYPosition()
    treasureXPosition = treasurePosition.calculateXPosition()
    treasureYPosition = treasurePosition.calculateYPosition()
    hiddenTXPosition = hiddenTreasures.calculateXPosition()
    hiddenTYPosition = hiddenTreasures.calculateYPosition()
    trapX = trap.calculateXPosition()
    trapY = trap.calculateYPosition()


    while positionMatching:
        
        if (playerXPosition == treasureXPosition or playerYPosition == treasureYPosition 
        or hiddenTXPosition == playerXPosition or hiddenTYPosition == playerYPosition 
        or hiddenTXPosition == treasureXPosition or hiddenTYPosition == treasureYPosition 
        or trapX == playerXPosition or trapY == playerYPosition):
            
            playerXPosition = playerPosition.calculateXPosition()
            playerYPosition = playerPosition.calculateYPosition()
            treasureXPosition = treasurePosition.calculateXPosition()
            treasureYPosition = treasurePosition.calculateYPosition()
            hiddenTXPosition = hiddenTreasures.calculateXPosition()
            hiddenTYPosition = hiddenTreasures.calculateYPosition()
            trapX = trap.calculateXPosition()
            trapY = trap.calculateYPosition()

        else:
            positionMatching = False

    navigation = Navigation(playerXPosition, playerYPosition, treasureXPosition, treasureYPosition)

    dial = Dial()

    print("The dial reads " + str(navigation.calculateResultant()) + "m")



    print("Try \"North\", \"South\", \"East\" or \"West\" \n" +
                "You notice a small watch-like device in your left hand.\n" +
                "It has hands like a watch, but the hands don’t seem to tell\n" +
                "time.")

    def displayboard(playerXPosition,playerYPosition):
        
        row = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        col = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        lst = []
        board =[]
        for i in row:
            for j in col:
                board.append((j,i)) 
        

        for el in board:
        
            if el == (playerXPosition,playerYPosition):
                lst.append('|X|')
            
            
            else:
                lst.append('|_|')
        row1 = ' '.join(lst[:20])
        row2 = ' '.join(lst[20:40])
        row3 = ' '.join(lst[40:60])
        row4 = ' '.join(lst[60:80])
        row5 = ' '.join(lst[80:100])   
        row6 = ' '.join(lst[100:120])
        row7 = ' '.join(lst[120:140]) 
        row8 = ' '.join(lst[140:160]) 
        row9 = ' '.join(lst[160:180])    
        row10 = ' '.join(lst[180:200]) 
        row11 = ' '.join(lst[200:220]) 
        row12 = ' '.join(lst[220:240]) 
        row13 = ' '.join(lst[240:260]) 
        row14 = ' '.join(lst[260:280]) 
        row15 = ' '.join(lst[280:300]) 
        row16 = ' '.join(lst[300:320]) 
        row17 = ' '.join(lst[320:340]) 
        row18 = ' '.join(lst[340:360]) 
        row19 = ' '.join(lst[360:380]) 
        row20 = ' '.join(lst[380:400])
        
        
        string = ("{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}\n{11}\n{12}\n{13}\n{14}\n{15}\n{16}\n{17}\n{18}\n{19}").format(row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15,row16,row17,row18,row19,row20)
        print(string)
        return lst
    
    while toGoCondition:

        if playerXPosition == hiddenTXPosition and playerYPosition == hiddenTYPosition:
            print("You have discovered the legendary EI sword to aid you in your quest")
        
        if trapX == playerXPosition and trapY == playerYPosition:
            print("You fell into a trap, you're dead now")
            toGoCondition = False

        if playerXPosition == treasureXPosition and playerYPosition == treasureYPosition:
            print("You found the treasure, now go save the world. THE END")
            toGoCondition = False
        
        else:
            displayboard(playerXPosition,playerYPosition)
            toGo = input("Please enter directions to go: ").lower()

            if toGo == "south" or toGo == "s":
                playerYPosition = dial.north(playerYPosition)
                navigation.setpY(playerYPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            elif toGo == "east" or toGo == "e":
                playerXPosition = dial.east(playerXPosition)
                navigation.setpX(playerXPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            elif toGo == "north" or toGo == "n":
                playerYPosition = dial.south(playerYPosition)
                navigation.setpY(playerYPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            elif toGo == "west" or toGo == "w":
                playerXPosition = dial.west(playerXPosition)
                navigation.setpX(playerXPosition)
                print("The dial reads " + str(navigation.calculateResultant()) + "m")
            else:
                print("You havent chosen a direction to go")
                print(navigation.calculateResultant())
            
if __name__ == "__main__":
    main()









