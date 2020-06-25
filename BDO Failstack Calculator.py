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

itemType = int(input("Enter 1 for Weapon, 2 for Armor, 3 for Accessory, 4 for Horse or 5 for Blackstar Weapons: "))
while itemType not in(1,2,3,4,5):
    print("Please pick a valid number:")
    itemType = int(input("Enter 1 for Weapon, 2 for Armor, 3 for Accessory, 4 for Horse or 5 for Blackstar Weapons: "))

#Horses don't have different levels you can enhance to, you can only go from tier 8 to tier 9.
if itemType != enhanceType.Horse:
    levelAttempted = int(input("Enter what level you're trying to enhance to in number form(eg: pri = 1) "))
    while levelAttempted not in(1,2,3,4,5):
        print("Please pick a valid number:")
        levelAttempted = int(input("Enter what level you're trying to enhance to in number form(eg: pri = 1) "))

failstack = int(input("Enter your Failstack: "))

if itemType == enhanceType.Weapon:
    if levelAttempted == enhanceLevel.Pri:
#Pri Weapon stack
        if failstack < 50:
            oddsSuccess = round(11.77 + 1.176 * failstack, 2)
        else:
            oddsSuccess = round(70.56 + (failstack - 50) * .235, 2)
        print("Softcap FS is 50")

#Duo Weapon Stack
    elif levelAttempted == enhanceLevel.Duo:
        if failstack < 82:
            oddsSuccess = round(7.69 + 0.769 * failstack, 2)
        else:
            oddsSuccess = round(70.75 + (failstack - 82) * .15, 2)
        print("Softcap FS is 82")
#Tri Weapon Stack
    elif levelAttempted == enhanceLevel.Tri:
        if failstack < 102:
            oddsSuccess = round(6.25 + .625 * failstack, 2)
        else:
            oddsSuccess = round(70 + (failstack - 102) * .125, 2)
        print("Softcap FS is 102")
#Tet Weapon Stack
    elif levelAttempted == enhanceLevel.Tet:
        oddsSuccess = round(2 + .2 * failstack, 2)
        print("Softcap Unknown")
#Pen Weapon Stack
    elif levelAttempted == enhanceLevel.Pen:
        oddsSuccess = round(.3 + .03 * failstack, 2)
        print("Softcap unknown")



elif itemType == enhanceType.Armor:
# Pri Armor stack
    if levelAttempted == enhanceLevel.Pri:
        if failstack < 50:
            oddsSuccess = round(11.77 + 1.176 * failstack, 2)
        else:
            oddsSuccess = round(70.56 + (failstack - 50) * .235, 2)
        print("Softcap FS is 50")
    # Duo Armor Stack
    elif levelAttempted == enhanceLevel.Duo:
        if failstack < 82:
            oddsSuccess = round(7.69 + 0.769 * failstack, 2)
        else:
            oddsSuccess = round(70.75 + (failstack - 82) * .15, 2)
        print("Softcap FS is 82")
# Tri Armor Stack
    elif levelAttempted == enhanceLevel.Tri:
        if failstack < 102:
            oddsSuccess = round(6.25 + .625 * failstack, 2)
        else:
            oddsSuccess = round(70 + (failstack - 102) * .125, 2)
        print("Softcap FS is 102")
# Tet Armor Stack
    elif levelAttempted == enhanceLevel.Tet:
        oddsSuccess = round(2 + .2 * failstack, 2)
        print("Softcap Unknown")
# Pen Armor Stack
    elif levelAttempted == enhanceLevel.Pen:
        oddsSuccess = round(.3 + .03 * failstack, 2)
        print("Softcap Unknown")


elif itemType == enhanceType.Accessory:

   #Pri Accessory Stack
    if levelAttempted == enhanceLevel.Pri:
        if failstack < 18:
            oddsSuccess = round(25 + 2.5 * failstack)
        else:
            oddsSuccess = round(70 + (failstack - 18) * .5)
        print("Softcap is 18")
    #Duo Accessory Stack
    elif levelAttempted == enhanceLevel.Duo:
        if failstack < 40:
            oddsSuccess = round(10 + 1 * failstack, 2)
        else:
            oddsSuccess = round(50 + (failstack - 40) * .2, 2)
        print("Softcap is 40")
    #Tri Accessory Stack
    elif levelAttempted == enhanceLevel.Tri:
        if failstack < 44:
            oddsSuccess = round(7.5 + .75 * failstack, 2)
        else:
            oddsSuccess = round(40.5 + (failstack - 44) * .15, 2)
        print("Softcap is 44")
    elif levelAttempted == enhanceLevel.Tet:
        if failstack < 110:
            oddsSuccess = round(2.5 + .25 * failstack, 2)
        else:
            oddsSuccess = round(30 + (failstack - 110) * 0.05, 2)
        print("Softcap is 110")
    elif levelAttempted == enhanceLevel.Pen:
        oddsSuccess = round(.5 + failstack * .05, 2)
        print("Softcap unknown")

#Horse Attempts, softcap and levels don't exist so math is pretty simple
elif itemType == enhanceType.Horse:
    oddsSuccess = round(1 + .2 * failstack, 2)

#Blackstar Weapon, there is no softcap so math is simple. I don't have a tet to test for pen attempts, so that might be incorrect.
elif itemType == enhanceType.BlackstarWeapon:
    if levelAttempted == enhanceLevel.Pri:
        oddsSuccess = round(13.08 + failstack * 1.308, 2)
    elif levelAttempted == enhanceLevel.Duo:
        oddsSuccess = round(10.63 + 1.063 * failstack, 2)
    elif levelAttempted == enhanceLevel.Tri:
        oddsSuccess = round(3.4 + .34 * failstack, 2)
    elif levelAttempted == enhanceLevel.Tet:
        oddsSuccess = round(0.51 + .051 * failstack,2)
    elif levelAttempted == enhanceLevel.Pen:
        oddsSuccess = round(.2 + .02 * failstack, 2)
        print("Uncertain of actual odds")

#Max odds can be is 100%
if oddsSuccess > 100:
    oddsSuccess = 100
print("Odds of Success:", oddsSuccess)

#Function to find expected number of attempts to succeed half the time and 90% of the time
#Percentages are weird, we have to use exponents to determine how many attempts it will take
#You have to take into account the times where you succeed twice in a row
#So it's not as simple as 5% chance means that it takes 20 attempts on average
#Essentially the odds of at least one success (odds that it won't happen) ^ (number of attempts)
#We iterate through on number of attempts to find asymptotes at 50% and 90% chance of at least one success
#Crons checks at .1 because at that point there's a 10% chance you haven't succeeded
#Therefore a 90% chance you've succeeded at least once
if itemType !=enhanceType.Horse:
    crons = 1
    percentOdds = oddsSuccess * .01
    inverseOdds = 1 - percentOdds
    index = 1
    while crons > 0.5:
        crons = inverseOdds ** index
        index += 1
    #Because of how the loop works, need to subtract one to get the number of iterations before success
    index -= 1
    print("Number of attempts to get a 50% chance of succeeding using crons: ", index)
    #Reset to check 90%
    crons = 1
    index = 1
    while crons > 0.1:
        crons = inverseOdds ** index
        index += 1
    #Because of how the loop works, need to subtract one to get the number of iterations before success
    index -= 1
    print("Number of attempts to get a 90% chance of succeeding using crons: ", index)

#Horse attempts can't be cronned in the same way, the failstack still goes up.
#In order to determine odds of success we need to account for this
#The odds of a horse attempt are 1% + .2% per failed attempt
#As such, our floating variable needs to go up by .2% per attempts
else:
    crons = 1
    percentOdds = oddsSuccess * .01
    inverseOdds = 1 - percentOdds
    index = 1

    while crons > .5:
        crons = (inverseOdds - (.002 * index)) ** index
        index += 1
    #Because of how the loop works, need to subtract one to get the number of iterations before success
    index -= 1
    print("Number of attempts to get a 50% chance of success: ", index)
    #Reset to check 90%
    crons = 1
    index = 1
    while crons > .1:
        crons = (inverseOdds - (.002 * index)) ** index
        index += 1
    #Because of how the loop works, need to subtract one to get the number of iterations before success
    index -= 1
    print("Number of attempts to get a 90% chance of success: ", index)

#Generate a single attmempt on the given odds
#Annoyingly random.range returns an int, so random.random() * 100 is required
chanceSucceeded = random.random() * 100
if oddsSuccess > chanceSucceeded:
    print("If you tried to succeed with this stack, you would have successfully enhanced.")
else:
    print("If you tried to succeed with this stack, you would have failed.")

