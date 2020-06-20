#Calculator to try and determine how useful a failstack is for a certain level of enhancement
#Includes estimated number of attempts when cronning an item
#Todo includes Dead God, and RNG calculator for attempts in app

itemType = int(input("Enter 1 for Weapon, 2 for Armor, 3 for accessory, 4 for Horse or 5 for Blackstar Weapons: "))

#Horses don't have different levels you can enhance to, you can only go from tier 8 to tier 9.
if itemType != 4:
    levelAttempted = int(input("Enter what level you're trying to enhance to in number form(eg: pri = 1) "))

failstack = float(input("Enter your Failstack: "))

if itemType == 1:
    if levelAttempted == 1:
#Pri Weapon stack
        if failstack < 50:
            oddsSuccess = round(11.77 + 1.176 * failstack, 2)

        else:
            oddsSuccess = round(70.56 + (failstack - 50) * .235, 2)

        print("Softcap FS is 50")

#Duo Weapon Stack
    elif levelAttempted == 2:
        if failstack < 82:
            oddsSuccess = round(7.69 + 0.769 * failstack, 2)
        else:
            oddsSuccess = round(70.75 + (failstack - 82) * .15, 2)
        print("Softcap FS is 82")
#Tri Weapon Stack
    elif levelAttempted == 3:
        if failstack < 102:
            oddsSuccess = round(6.25 + .625 * failstack, 2)
        else:
            oddsSuccess = round(70 + (failstack - 102) * .125, 2)
        print("Softcap FS is 102")
#Tet Weapon Stack
    elif levelAttempted == 4:
        oddsSuccess = round(2 + .2 * failstack, 2)
        print("Softcap Unknown")
#Pen Weapon Stack
    elif levelAttempted == 5:
        oddsSuccess = round(.3 + .03 * failstack, 2)
        print("No softcap known")

    else:
        print("Bad Level Attempted")

if itemType == 2:
# Pri Armor stack
    if levelAttempted == 1:
        if failstack < 50:
            oddsSuccess = round(11.77 + 1.176 * failstack, 2)
        else:
            oddsSuccess = round(70.56 + (failstack - 50) * .235, 2)
        print("Softcap FS is 50")
    # Duo Armor Stack
    elif levelAttempted == 2:
        if failstack < 82:
            oddsSuccess = round(7.69 + 0.769 * failstack, 2)
        else:
            oddsSuccess = round(70.75 + (failstack - 82) * .15, 2)
        print("Softcap FS is 82")
# Tri Armor Stack
    elif levelAttempted == 3:
        if failstack < 102:
            oddsSuccess = round(6.25 + .625 * failstack, 2)
        else:
            oddsSuccess = round(70 + (failstack - 102) * .125, 2)
        print("Softcap FS is 102")
# Tet Weapon Stack
    elif levelAttempted == 4:
        oddsSuccess = round(2 + .2 * failstack, 2)
        print("Softcap Unknown")
# Pen Weapon Stack
    elif levelAttempted == 5:
        oddsSuccess = round(.3 + .03 * failstack, 2)
        print("No softcap known")
    else:
        print("Bad Level Attempted")

if itemType == 3:

   #Pri Accessory Stack
    if levelAttempted == 1:
        if failstack < 18:
            oddsSuccess = round(25 + 2.5 * failstack)
        else:
            oddsSuccess = round(70 + (failstack - 18) * .5)
        print("Softcap = 18")

    #Duo Accessory Stack
    elif levelAttempted == 2:
        if failstack < 40:
            oddsSuccess = round(10 + 1 * failstack, 2)
        else:
            oddsSuccess = round(50 + (failstack - 40) * .2, 2)
        print("Softcap = 40")
    #Tri Accessory Stack
    elif levelAttempted == 3:
        if failstack < 44:
            oddsSuccess = round(7.5 + .75 * failstack, 2)
        else:
            oddsSuccess = round(40.5 + (failstack - 44) * .15, 2)
        print("Softcap = 44")
    elif levelAttempted == 4:
        if failstack < 110:
            oddsSuccess = round(2.5 + .25 * failstack, 2)
        else:
            oddsSuccess = round(30 + (failstack - 110) * 0.05, 2)
        print("Softcap is 110")
    elif levelAttempted == 5:
        oddsSuccess = round(.5 + failstack * .05, 2)
        print("Softcap unknown")
    else:
        print("Bad Level Attempted")

#Horse Attempts
if itemType == 4:
    oddsSuccess = 1 + .2 * failstack

#Blackstar Weapon
if itemType == 5:
    if levelAttempted == 1:
        oddsSuccess = 13.08 + failstack * 1.308
    elif levelAttempted == 2:
        oddsSuccess = 10.63 + 1.063 * failstack
    elif levelAttempted == 3:
        oddsSuccess = 3.4 + .34 * failstack
    elif levelAttempted == 4:
        oddsSuccess = 0.51 + .051 * failstack
    elif levelAttempted == 5:
        oddsSuccess = .2 + .02 * failstack
        print("Uncertain of actual odds")

print("Odds of Success:")
print(oddsSuccess)

#Function to find expected number of attempts to succeed half the time and 90% of the time
#Percentages are weird, we have to use exponents to determine how many attempts it will take
#You have to take into account the times where you succeed twice in a row, so it's not as simple as 5% chance means that it takes 20 attempts on average
#Essentially the odds of at least one success (odds that it won't happen) ^ (number of attempts)
#We iterate through on number of attempts to find asymptotes at 50% and 90% chance of at least one success
#Crons checks at .1 because at that point there's a 10% chance you haven't succeeded, and therefore a 90% chance you've succeeded at least once
if itemType !=4:
    crons = 1
    percentOdds = oddsSuccess * .01
    inverseOdds = 1 - percentOdds
    index = 1
    while crons > 0.5:
        crons = inverseOdds ** index
        index += 1

    print("Number of attempts to get a 50% chance of succeeding using crons: ")
    print(index)
    crons = 1
    index = 1
    while crons > 0.1:
        crons = inverseOdds ** index
        index += 1
    print("Number of attempts to get a 90% chance of succeeding using crons: ")
    print(index)

#Horse attempts can't be cronned in the same way, the failstack still goes up. In order to determine odds of success we need to account for this
#The odds of a horse attempt are 1% + .2% per failed attempt
#As such, our floating variable needs to go up by .2% per attempts
else:
    crons = 1
    percentOdds = oddsSuccess * .01
    inverseOdds = 1 - percentOdds
    index = 0

    while crons > .5:
        crons = (inverseOdds - (.002 * index)) ** index
        index += 1
    print("Number of attempts to get a 50% chance of success: ")
    print(index)
    crons = 1
    index = 0
    while crons > .1:
        crons = (inverseOdds - (.002 * index)) ** index
        index += 1
    print("Number of attempts to get a 90% chance of success: ")
    print(index)

