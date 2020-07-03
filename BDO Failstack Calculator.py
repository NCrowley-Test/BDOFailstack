#Calculator to try and determine how useful a failstack is for a certain level of enhancement
#Includes estimated number of attempts when cronning an item
#Todo includes Dead God, and RNG calculator for attempts in app
import random
from enum import IntEnum

class enhanceType(IntEnum):
    Weapon = 1
    Armor = 2
    Accessory = 3
    Horse = 4
    BlackstarWeapon = 5

class enhanceLevel(IntEnum):
    Pri = 1
    Duo = 2
    Tri = 3
    Tet = 4
    Pen = 5
def get_Item_Type():
    item_Type = 0
    while item_Type not in(1,2,3,4,5):
        try:
            item_Type = int(input("Enter 1 for Weapon, 2 for Armor, 3 for Accessory, 4 for Horse or 5 for Blackstar Weapons: "))
        except:
            print("Please pick a valid number")
    return item_Type

def get_Level_attempted():
    level_Attempted = 0


    while level_Attempted not in(1,2,3,4,5):
        try:
            level_Attempted = int(input("Enter what level you're trying to enhance to in number form(eg: pri = 1) "))
        except:
            print("Please pick a valid number")
    return level_Attempted

def get_Failstack():
    failstack = -1
    while failstack == -1:
        try:
            failstack = abs(int(input("Enter your Failstack: ")))
        except:
            print("Please pick a number")
    return failstack

def get_Info():
    item_Type = get_Item_Type()
    #Horses don't need level attempted, can only go from t8 to dream
    if item_Type != enhanceType.Horse:
        level_Attempted = get_Level_attempted()
    else:
        level_Attempted = 0
    failstack = get_Failstack()
    return [item_Type, level_Attempted, failstack]


def odds_Success(attempt):
    item_Type = int(attempt[0])
    level_Attempted = int(attempt[1])
    failstack = int(attempt[2])
    if item_Type == enhanceType.Weapon:
        if level_Attempted == enhanceLevel.Pri:
            # Pri Weapon stack
            if failstack < 50:
                odds_Success = round(11.77 + 1.176 * failstack, 2)
            else:
                odds_Success = round(70.56 + (failstack - 50) * .235, 2)
            print("Softcap FS is 50")

        # Duo Weapon Stack
        elif level_Attempted == enhanceLevel.Duo:
            if failstack < 82:
                odds_Success = round(7.69 + 0.769 * failstack, 2)
            else:
                odds_Success = round(70.75 + (failstack - 82) * .15, 2)
            print("Softcap FS is 82")
        # Tri Weapon Stack
        elif level_Attempted == enhanceLevel.Tri:
            if failstack < 102:
                odds_Success = round(6.25 + .625 * failstack, 2)
            else:
                odds_Success = round(70 + (failstack - 102) * .125, 2)
            print("Softcap FS is 102")
        # Tet Weapon Stack
        elif level_Attempted == enhanceLevel.Tet:
            odds_Success = round(2 + .2 * failstack, 2)
            print("Softcap Unknown")
        # Pen Weapon Stack
        elif level_Attempted == enhanceLevel.Pen:
            odds_Success = round(.3 + .03 * failstack, 2)
            print("Softcap unknown")



    elif item_Type == enhanceType.Armor:
        # Pri Armor stack
        if level_Attempted == enhanceLevel.Pri:
            if failstack < 50:
                odds_Success = round(11.77 + 1.176 * failstack, 2)
            else:
                odds_Success = round(70.56 + (failstack - 50) * .235, 2)
            print("Softcap FS is 50")
        # Duo Armor Stack
        elif level_Attempted == enhanceLevel.Duo:
            if failstack < 82:
                odds_Success = round(7.69 + 0.769 * failstack, 2)
            else:
                odds_Success = round(70.75 + (failstack - 82) * .15, 2)
            print("Softcap FS is 82")
        # Tri Armor Stack
        elif level_Attempted == enhanceLevel.Tri:
            if failstack < 102:
                odds_Success = round(6.25 + .625 * failstack, 2)
            else:
                odds_Success = round(70 + (failstack - 102) * .125, 2)
            print("Softcap FS is 102")
        # Tet Armor Stack
        elif level_Attempted == enhanceLevel.Tet:
            odds_Success = round(2 + .2 * failstack, 2)
            print("Softcap Unknown")
        # Pen Armor Stack
        elif level_Attempted == enhanceLevel.Pen:
            odds_Success = round(.3 + .03 * failstack, 2)
            print("Softcap Unknown")


    elif item_Type == enhanceType.Accessory:

        # Pri Accessory Stack
        if level_Attempted == enhanceLevel.Pri:
            if failstack < 18:
                odds_Success = round(25 + 2.5 * failstack)
            else:
                odds_Success = round(70 + (failstack - 18) * .5)
            print("Softcap is 18")
        # Duo Accessory Stack
        elif level_Attempted == enhanceLevel.Duo:
            if failstack < 40:
                odds_Success = round(10 + 1 * failstack, 2)
            else:
                odds_Success = round(50 + (failstack - 40) * .2, 2)
            print("Softcap is 40")
        # Tri Accessory Stack
        elif level_Attempted == enhanceLevel.Tri:
            if failstack < 44:
                odds_Success = round(7.5 + .75 * failstack, 2)
            else:
                odds_Success = round(40.5 + (failstack - 44) * .15, 2)
            print("Softcap is 44")
        elif level_Attempted == enhanceLevel.Tet:
            if failstack < 110:
                odds_Success = round(2.5 + .25 * failstack, 2)
            else:
                odds_Success = round(30 + (failstack - 110) * 0.05, 2)
            print("Softcap is 110")
        elif level_Attempted == enhanceLevel.Pen:
            odds_Success = round(.5 + failstack * .05, 2)
            print("Softcap unknown")

    # Horse Attempts, softcap and levels don't exist so math is pretty simple
    elif item_Type == enhanceType.Horse:
        odds_Success = round(1 + .2 * failstack, 2)

    # Blackstar Weapon, there is no softcap so math is simple. I don't have a tet to test for pen attempts, so that might be incorrect.
    elif item_Type == enhanceType.BlackstarWeapon:
        if level_Attempted == enhanceLevel.Pri:
            odds_Success = round(13.08 + failstack * 1.308, 2)
        elif level_Attempted == enhanceLevel.Duo:
            odds_Success = round(10.63 + 1.063 * failstack, 2)
        elif level_Attempted == enhanceLevel.Tri:
            odds_Success = round(3.4 + .34 * failstack, 2)
        elif level_Attempted == enhanceLevel.Tet:
            odds_Success = round(0.51 + .051 * failstack, 2)
        elif level_Attempted == enhanceLevel.Pen:
            odds_Success = round(.2 + .02 * failstack, 2)
            print("Uncertain of actual odds")

    # Max odds can be is 100%
    if odds_Success > 100:
        odds_Success = 100
    print("Odds of Success:", odds_Success)
    return odds_Success

def find_Odds_Over_Time(attempt, odds_Success):
    # Function to find expected number of attempts to succeed half the time and 90% of the time
    # Percentages are weird, we have to use exponents to determine how many attempts it will take
    # You have to take into account the times where you succeed twice in a row
    # So it's not as simple as 5% chance means that it takes 20 attempts on average
    # Essentially the odds of at least one success (odds that it won't happen) ^ (number of attempts)
    # We iterate through on number of attempts to find asymptotes at 50% and 90% chance of at least one success
    # Crons checks at .1 because at that point there's a 10% chance you haven't succeeded
    # Therefore a 90% chance you've succeeded at least once
    item_Type = attempt[0]
    if item_Type != enhanceType.Horse:
        crons = 1
        percentOdds = odds_Success * .01
        inverseOdds = 1 - percentOdds
        index = 1
        while crons > 0.5:
            crons = inverseOdds ** index
            index += 1
        # Because of how the loop works, need to subtract one to get the number of iterations before success
        index -= 1
        print("Number of attempts to get a 50% chance of succeeding using crons: ", index)
        # Reset to check 90%
        crons = 1
        index = 1
        while crons > 0.1:
            crons = inverseOdds ** index
            index += 1
        # Because of how the loop works, need to subtract one to get the number of iterations before success
        index -= 1
        print("Number of attempts to get a 90% chance of succeeding using crons: ", index)

    # Horse attempts can't be cronned in the same way, the failstack still goes up.
    # In order to determine odds of success we need to account for this
    # The odds of a horse attempt are 1% + .2% per failed attempt
    # As such, our floating variable needs to go up by .2% per attempts
    else:
        crons = 1
        percentOdds = odds_Success * .01
        inverseOdds = 1 - percentOdds
        index = 1

        while crons > .5:
            crons = (inverseOdds - (.002 * index)) ** index
            index += 1
        # Because of how the loop works, need to subtract one to get the number of iterations before success
        index -= 1
        print("Number of attempts to get a 50% chance of success: ", index)
        # Reset to check 90%
        crons = 1
        index = 1
        while crons > .1:
            crons = (inverseOdds - (.002 * index)) ** index
            index += 1
        # Because of how the loop works, need to subtract one to get the number of iterations before success
        index -= 1
        print("Number of attempts to get a 90% chance of success: ", index)




def RNG_Attempt(odds_Success):

    # Annoyingly random.range returns an int, so random.random() * 100 is required
    exit_Code = ''
    failed_Attempts = 0
    while exit_Code != 'Q':
        chanceSucceeded = random.random() * 100
        if odds_Success > chanceSucceeded:
            print("If you tried to succeed with this stack, you would have successfully enhanced. You failed", failed_Attempts, "times before succeeding.")
            failed_Attempts = 0
        else:
            failed_Attempts += 1
            print("If you tried to succeed with this stack, you would have failed. You have failed", failed_Attempts, "times.")

        exit_Code = str(input("Try again? Enter Q to quit"))
        if exit_Code == "q" or exit_Code == "Q":
            exit()



attempt = get_Info()
odds_Success = odds_Success(attempt)
find_Odds_Over_Time(attempt, odds_Success)
RNG_Attempt(odds_Success)

