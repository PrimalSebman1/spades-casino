"""
Just a remake of my other casino game (unreleased and will stay that way), but this one will work
Don't really feel like trying to debug the other one
"""
#Imports

import random
import numpy as np
from dice import gotOne
from dice import gotTwo
from dice import gotThree
from dice import gotFour
from dice import gotFive
from dice import gotSix
from slotImage import slotImage
from pachinkoImage import pachinkoImage
from pachinkoRound import rounder

#Important variables
money = 1000
leave = False
totalPlays = 0
dicePlays = 0
roulettePlays = 0
slotsPlays = 0
pachinkoPlays = 0
carPlays = 0
coinFlipPlays = 0
kenoPlays = 0
blackjackPlays = 0
warPlays = 0
#Yes I looked it up and this is how the numbers are arranged on a roulette wheel
rouletteSpaces = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
numBet = 1
colBet = 2
slotIcons = ["!","@","#","$","%"]
suits = ["Diamonds", "Clubs", "Spades", "Hearts"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
fool = True

#Some functions
def stats():
  print("-------STATS-------")
  print("Total plays: "+str(totalPlays))
  print("Slot car plays: "+str(carPlays))
  print("Keno plays: "+str(kenoPlays))
  print("21 game plays: "+str(blackjackPlays))
  print("War game plays: "+str(warPlays))
  print("Dice game plays: "+str(dicePlays))
  print("Slots plays: "+str(slotsPlays))
  print("Roulette plays: "+str(roulettePlays))
  print("Pachinko plays: "+str(pachinkoPlays))
  print("Coin flip plays: "+str(coinFlipPlays))
  print("Ending money: $"+str(money))
  if (money < 1000):
    print("Total loss: $"+str(1000-money))
  elif (money > 1000):
    print("Total profit: $"+str(money - 1000))
  else:
    print("Net change: $0")
  print()
  print("I hope you enjoyed your time!\n")
def elevator():
  print("FLOORS\n")
  print("10| Slot Car Racing")
  print("09| Keno")
  print("08| 21")
  print("07| War (Coming soon)")
  print("06| Dice game")
  print("05| Slots")
  print("04| Roulette ")
  print("03| Pachinko")
  print("02| Coin Flip")
  print("01| Lobby (YOU ARE HERE)")

#Functions for cards
def printHand(hand, house):
  print("Your hand is:\n")
  for i in range(len(hand) - 1):
    print(hand[i], end = ", ")
  print(hand[len(hand) -1])
  print()
  print("The House's hand is:\n")
  for i in range(len(house) - 1):
    print(house[i], end = ", ")
  print(house[len(house) - 1])

#This one's got a lot of comments bc I wanted to make sure I understood it myself
def getValue(cards):
  #Reset values (return) and allVals (for keeping track of, specifically, aces)
  values = 0
  allVals = []
  #For every card in the hand
  for i in range(len(cards)):
    #Split element at i into its parts
    theVals = cards[i].split()
    #Since the actual value is always first, only look at index 0
    theVals = theVals[0]
    #Special cases and values
    if theVals == "Ace":
      values += 11
    elif theVals == "King" or theVals == "Queen" or theVals == "Jack":
      values += 10
    else:
      values += int(theVals)
    #Adds string value to allVals
    allVals.append(theVals)
  #Special case: Aces can be either 11 or 1
  if values > 21 and "Ace" in allVals:
    #Can happen for as many aces as in the hand
    for i in range(allVals.count("Ace")):
      #Auto adjusts score
      if values > 21:
        values -= 10
  #Returns int of the score
  return values

def getCardVal(card):
  values = 0
  theVals = card.split()
  theVals = theVals[0]
  if theVals == "Ace":
    values += 12
  elif theVals == "King" or theVals == "Queen" or theVals == "Jack":
    values += 11
  else:
    values += int(theVals)
  return values

def drawCard(f,o):
  s = random.randint(0, len(suits) - 1)
  v = random.randint(0,len(values) - 1)
  n = values[v] + " of " + suits[s]
  while n in o or n in f:
    s = random.randint(0, len(suits) - 1)
    v = random.randint(0,len(values) - 1)
    n = values[v] + " of " + suits[s]
  f.append(n)

#Introductions and whatnot
print("Hello there, esteemed guest! Thank you for your visit.\n")
print("Before we admit you to our facility, first, a question:\n")
name = input("What is your name?\n")
print("Ah, welcome, "+name+". We hope you enjoy your time here.\n")
enter = input("Press Enter to enter the casino.\n")

while (money > 0):
  if totalPlays == 0:
    print("Hey! How're you doing? I'm Spades, the owner of this casino.\n")
    print("It looks like this is your first time here.\n")
    print("We're finished with the Casino! We have everything we could ever want.\n")
    print("We've added War now!\n")
  else:
    print("Welcome back to the lobby, "+name)
    print("You have $"+str(money)+".\n")
  bufferer = input("Press ENTER to continue")
  print("What floor will you go to? Type \"leave\" to leave.\n")
  #Getting floor to take player
  #Do this for all int inputs, basically ensures that the program won't crash
  #For a wrong input
  while fool:
    try:
      elevator()
      floor = input()
      if (floor == "leave"):
        leave = True
        break
      else:
        floor = int(floor)
        if (floor == 1):
          print("You are already here.\n")
          continue
        while (floor > 10) or (floor <= 0):
          print("Sorry, that floor doesn't exist (yet)\n")
          elevator()
          floor = int(input())
        break
    except ValueError:
      print("Please enter the floor you wish to go to.\n")
  if (leave == True):
    break
  if (floor == 6):
    print("Welcome to the dice game!\n")
    print("Get above 7 or doubles to win!\n")
    print("You have $"+str(money)+" left.\n")
    #Getting bet, ensuring it's both greater than 0 and less than or equal to current money
    while fool:
      try:
        bet = int(input("How much do you want to bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("I'm sorry, that's an invalid input.\n")
          bet = int(input("How much do you want to bet?\n"))
        break
      except ValueError:
        print("You must enter a number for your bet.\n")
    money -= bet
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    #Checks what to print for first die
    if (d1 == 1):
        gotOne()
    elif (d1 == 2):
        gotTwo()
    elif (d1 == 3):
        gotThree()
    elif (d1 == 4):
        gotFour()
    elif (d1 == 5):
        gotFive()
    else:
        gotSix()
    #Checks what to print for second die
    if (d2 == 1):
        gotOne()
    elif (d2 == 2):
        gotTwo()
    elif (d2 == 3):
        gotThree()
    elif (d2 == 4):
        gotFour()
    elif (d2 == 5):
        gotFive()
    else:
        gotSix()
    #Prints something based on roll, then gives out winnings if applicable
    if (d1 == d2):
        print("Congrats, you win!")
        money += (3*bet)
        money = int(money)
    elif (d1 + d2 > 7):
        print("Good win, jolly good show!\n")
        money += (2*bet)   
    else:
        print("Tough luck!")
    dicePlays += 1
    totalPlays += 1
    buffererer = input("Press ENTER to continue")
  elif (floor == 4):
    print("Welcome to roulette!\n")
    print("Choose a color or number and spin the wheel.\n")
    print("You have $"+str(money)+" dollars left.\n")
    while fool:
      try:
        bet = int(input("How much do you wanna bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("Sorry, that's not a valid bet.\n")
          bet = int(input("How much do you wanna bet?\n"))
        break
      except ValueError:
        print("I need a number value for bet, please.\n")
    money -= bet
    #Options for betting: Color and number
    #Will add more in the future
    print("There'll be more options in the future,\n")
    print("but for now, you can only bet on a color or number.\n")
    numOrCol = input("Are you betting on a color or number?\n")
    while ((numOrCol != "number") and (numOrCol != "color")):
      print("You have to choose one, color or number.\n")
      numOrCol = input("Are you betting on a color or number?\n")
    #Choosing a number
    if (numOrCol == "number"):
      while fool:
        try:
          numBet = int(input("What number do you want to bet on?\n"))
          while ((numBet < 0) or (numBet > 36)):
            print("That's... not a number on the wheel. What're you on? I want some.\n")
            numBet = int(input("What number do you want to bet on?\n"))
          break
        except ValueError:
          print("That ain't even on the wheel. Try again.\n")
      print("So your bet's "+str(numBet)+". Ok, let's spin the wheel!\n")
      #Setting colBet to 0 to identify what user chose later
      #Will change when new bets added
      colBet = 0
    else:
      #Choosing color
      colBet = input("What color are you betting on?\n")
      while ((colBet != "green") and (colBet != "red") and (colBet != "black")):
        print("Sorry, there's only so many colors. We got green, red, and black.\n")
        colBet = input("What color are you betting on?\n")
        #To fit in with what I wrote earlier, capitalizes color
      colBet = colBet.capitalize()
      print("So you bet on "+colBet+". Let's see if it's a good choice, spin the wheel!\n")
      numBet = 0
    #Small buffer to add suspense and so I don't overload user with words
    spin = input("Press ENTER to spin!\n")
    num = random.randint(0,len(rouletteSpaces) - 1)
    num = rouletteSpaces[num]
    #Do the spin, get the number, and then find the color based on the number
    #0 is a special case
    if (num == 0):
      col = "Green"
    #Even numbers
    elif (num % 2 == 0):
      if (num <= 10):
        col = "Black"
      elif (num <= 18):
        col = "Red"
      elif (num <= 28):
        col = "Black"
      else:
        col = "Red"
    #Only odds are left, so I can use else
    else:
      if (num <= 10):
        col = "Red"
      elif (num <= 18):
        col = "Black"
      elif (num <= 28):
        col = "Red"
      else:
        col = "Black"
    #Display the color and number
    print("\\")
    print(" \\")
    print("  \\")
    print(col+" ---- "+str(num))
    print("  /")
    print(" /")
    print("/")
    #Comparing bet if they chose a color
    if (numBet == 0):
      print("You bet on "+colBet+", and the wheel landed on "+col+".\n")
      if (colBet == col):
        if (colBet != "Green"):
          print("Congrats! You picked the right color.\n")
          money += (2 * bet)
        else:
          print("Wow! Great guess!")
          money += (36 * bet)
      else:
        print("Oof, wrong choice. Sorry, you lost.\n")
    #Comparing num to numBet if they bet on a number
    else:
      print("You bet on "+str(numBet)+", and the wheel landed on "+str(num))
      if (numBet == num):
        print("Wow! Exellent guess! Looks like we got us a big winner.\n")
        money += (36 * bet)
      else:
        print("I'm not surprised, but between you and me I think you should've won.\n")
    roulettePlays += 1
    totalPlays += 1
    buffererer = input("Press ENTER to continue\n")
  elif (floor == 5):
    print("Welcome to slots! Here, you need three of a kind to win big!\n")
    #Same as others, making sure bet is a number
    while fool:
      try:
        bet = int(input("What is your bet?\n"))
        while (bet <= 0) or (bet > money):
          print("Sorry, that is not a valid bet.\n")
          bet = int(input("What is your bet?\n"))
        break
      except ValueError:
        print("Sorry, but I need a number.\n")
    print("Your bet is "+str(bet)+". Let's see what happens!\n")
    money -= bet
    #Getting the random numbers for the slots
    s1 = random.randint(0,4)
    s2 = random.randint(0,4)
    s3 = random.randint(0,4)
    #Turning the numbers into symbols
    s1 = slotIcons[s1]
    s2 = slotIcons[s2]
    s3 = slotIcons[s3]
    slotImage(s1,s2,s3)
    bufferererer = input("Press ENTER to continue")
    #Win condition: All three are the same
    #Only need two checks (thanks transitive prop)
    if (s1 == s2) and (s2 == s3):
      print("Jackpot! Big score for you, congratulations!\n")
      money += (101 * bet)
    else:
      print("Nope, not even close. Sorry!\n")
    slotsPlays += 1
    totalPlays += 1
    bufferererer = input("Press ENTER to continue\n")
  elif (floor == 3):
    print("You've arrived at the pachinko floor!\n")
    print("You might not know this game by name, but you know it nonetheless!\n")
    while fool:
      try:
        bet = int(input("How much do you wanna bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("Sorry, that's not a valid bet.\n")
          bet = int(input("How much do you wanna bet?\n"))
        break
      except ValueError:
        print("I need a number value for bet, please.\n")
    print("So you're betting $"+str(bet)+", eh? Let's see what happens!\n")
    money -= bet
    #Using normal distribution, get a single number
    #Mean = 4, std = 1
    r = np.random.normal(loc = 4, scale = 1)
    #Function that checks if the decimal is above or below .5 (hopefully)
    #If at or above .5, round up. Otherwise, round down
    r = rounder(r)
    #Very rare case, but if it's somehow more than 3.5 std's from mean
    if (r <= 0):
      r = 1
    elif (r >= 8):
      r = 7
    r = int(r)
    #Prints image based on position
    pachinkoImage(r)
    print("It landed in space "+str(r))
    if (r == 1) or (r == 7):
      print("Wow! You just hit the jackpot!\n")
      money += (21 * bet)
    elif (r == 2) or (r == 6):
      print("Good result, you made some money!\n")
      money += (6 * bet)
    elif (r == 3) or (r == 5):
      print("Better then nothing, I guess...\n")
      money += (bet * 0.5)
      money = int(money)
    else:
      print("Better luck next time!\n")
    pachinkoPlays += 1
    totalPlays += 1
    buffererererer = input("Press ENTER to continue\n")
  elif (floor == 10):
    print("Welcome to the roof! Ready to race?\n")
    carName = input("First, you get to name you car.\n")
    while fool:
      try:
        bet = int(input("How much do you wanna bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("Sorry, that's not a valid bet.\n")
          bet = int(input("How much do you wanna bet?\n"))
        break
      except ValueError:
        print("I need a number value for bet, please.\n")
    money -= bet
    print("Looks like you're putting down $"+str(bet)+" that you're gonna win.\n")
    print("All right, let's rock this!\n")
    bufferererererer = input("Press ENTER to continue\n")
    #Set initial distances to 0, and add plays
    d1 = 0
    d2 = 0
    carPlays += 1
    totalPlays += 1
    #Execute until one car finishes
    while (d1 < 20) and (d2 < 20):
      #Set up initial distances, I chose to reset them every time for convenience
      sep1 = ""
      sep2 = ""
      sep3 = ""
      sep4 = ""
      #Moving forward, house goes 1-5 per turn, player 1-4 (unfair I know, but what do you expect?)
      r1 = random.randint(1,5)
      if (r1 == 1):
        print("The House moved forward 1 space!\n")
      else:
        print("The House moved forward "+str(r1)+" spaces!\n")
      r2 = random.randint(1,4)
      if (r2 == 1):
        print(carName+" moved forward 1 space!\n")
      else:
        print(carName+" moved forward "+str(r2)+" spaces!\n")
      #Add distances and make sure it's 20 or below
      d1 += r1
      d2 += r2
      if (d1 > 20):
        d1 = 20
      if (d2 > 20):
        d2 = 20
      #For use with the image
      for i in range(d1):
        sep1 += " "
      for x in range(20-d1):
        sep3 += " "
      for c in range(d2):
        sep2 += " "
      for b in range(20-d2):
        sep4 += " "
      #Print image of race, using the spaces designated
      #There's definitely a better way to do this, but oh well
      print("|---------------------|")
      print("|"+sep1+"*"+sep3+"|")
      print("|---------------------|")
      print("|"+sep2+"*"+sep4+"|")
      print("|---------------------|")
      #House WC
      if (d1 == 20):
        print("The House wins! Be faster next time!\n")
        buffererererererer = input("Press ENTER to return to lobby.\n")
      #Player WC
      elif (d2 == 20):
        print("Nice going, hotshot! Congrats.\n")
        money += (6 * bet)
        bufferererererererer = input("Press ENTER to continue to lobby\n")
      #If no WC reached, reset turn and go again
      else:
        print("It's a close race!\n")
        print("The House is at "+str(d1)+" spaces out of 20, and \n")
        print(carName+" is at "+str(d2)+" spaces.\n")
        buffererererer = input("Press ENTER to continue\n")
  elif (floor == 2):
    print("Hey! This is the coin flip floor.\n")
    print("Guess whether the coin will flip heads or tails!\n")
    print("Get 6 in a row to win the jackpot.\n")
    while fool:
      try:
        bet = int(input("How much do you want to bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("I'm sorry, that's an invalid input.\n")
          bet = int(input("How much do you want to bet?\n"))
        break
      except ValueError:
        print("You must enter a number for your bet.\n")
    money -= bet
    #Get 6 binomial numbers
    #Tbh prob could've just used regular random numbers but
    #I wanted to learn how to use this, sue me
    flips = np.random.binomial(1,.5,size = 6)
    wins = 0
    for i in range(6):
      guess = input("Heads or tails?\n")
      guess = guess.capitalize()
      #Taking guess, changing it to format for binomial
      while (guess != "Heads") and (guess != "Tails"):
        print("You gotta choose one.\n")
        guess = input("Heads or tails?\n")
        guess = guess.capitalize()
      if (guess == "Heads"):
        guess = 1
      else:
        guess = 0
      #Checking for correct guess
      if (guess == flips[i]):
        wins += 1
        print("Congrats! You guessed right.\n")
        #Player WC
        if wins == 6:
          break
      else:
        print("Unfortunately, that's incorrect.\n")
        break
    #Give out money based on correct guesses
    if (wins == 0):
      print("Too bad!\n")
    elif (wins == 1):
      print("Well, it's better than losing, right?\n")
      money += (.5 * bet)
      money = int(money)
    elif (wins == 2):
      print("Pretty good, pretty good.\n")
      money += (3 * bet)
    elif (wins == 3):
      print("Really good, nice win!\n")
      money += (6 * bet)
    elif (wins == 4):
      print("Excellent job!\n")
      money += (11 * bet)
    elif (wins == 5):
      print("Awesome! But not yet the jackpot.\n")
      money += (26 * bet)
    else:
      print("Incredible! You hit the jackpot!\n")
      money += (51 * bet)
    coinFlipPlays += 1
    totalPlays += 1
    buffererererererererer = input("Press ENTER to continue\n")
  elif (floor == 9):
    print("Welcome to Keno!\n")
    print("You guess 10 numbers from 1-100, and get money\n")
    print("based on how many you get right.\n")
    print("Here you can find some of our biggest jackpots.\n")
    #Reset all variables and lists
    kenoWins = 0
    nums = []
    userNums = []
    while fool:
      try:
        bet = int(input("How much do you want to bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("I'm sorry, that's an invalid input.\n")
          bet = int(input("How much do you want to bet?\n"))
        break
      except ValueError:
        print("You must enter a number for your bet.\n")
    money -= bet
    #Create lists of random numbers and user numbers
    for i in range(10):
      x = random.randint(1,100)
      while x in nums:
        x = random.randint(1,100)
      nums.append(x)
      #Keep this going until user enters a valid number
      while (len(userNums) == i):
        try:
          print("You have entered "+str(len(userNums))+" number(s)\n")
          u = int(input("Please enter a number.\n"))
          while (u < 1) or (u > 100):
            print("Sorry, that's not a valid number.\n")
            u = int(input("Please enter a number.\n"))
          while u in userNums:
            print("You've already guessed that.\n")
            u = int(input("Please enter a number.\n"))
          userNums.append(u)
        except ValueError:
          print("Sorry, that's not a number.\n")
    #Checking how many wins the user gets
    for x in range(10):
      if (userNums[x] in nums):
        kenoWins += 1
    #Since so many WCs, lots of if statements
    if kenoWins == 0:
      print("No matches? Almost impressive.\n")
      money += (.5 * bet)
      money = int(money)
    elif kenoWins == 1:
      print("Sorry, one win won't cut it here.\n")
    elif kenoWins == 2:
      print("Two wins. Meh.\n")
      money += (bet)
    elif kenoWins == 3:
      print("Getting better, 3 wins.\n")
      money += (bet * 2)
    elif kenoWins == 4:
      print("Not bad, not bad, 4 wins.\n")
      money += (bet * 6)
    elif kenoWins == 5:
      print("Really good! 5 wins!\n")
      money += (11 * bet)
    elif kenoWins == 6:
      print("Dang, 6? Quite excellent.\n")
      money += (26 * bet)
    elif kenoWins == 7:
      print("That's seriously impressive, 7 wins?\n")
      money += (51 * bet)
    elif kenoWins == 8:
      print("Incredible. Simply incredible, 8 wins.\n")
      money += (101 * bet)
    elif kenoWins == 9:
      print("Almost to the jackpot! 9 wins!\n")
      money += (251 * bet)
    else:
      print("This is crazy. You won the jackpot!\n")
      money = (501 * bet)
    bufferererererererererer = input("Press ENTER to continue\n")
    totalPlays += 1
    kenoPlays += 1
  elif (floor == 8):
    print("Welcome to blackjack!\n")
    print("Here you get two cards to start, and you can draw more if you want.\n")
    print("The goal is to get as close to 21 as possible without going over.\n")
    #Reset/ initialize list of cards for player and house
    hand = []
    house = []
    handVal = 0
    houseVal = 0
    while fool:
      try:
        bet = int(input("How much do you want to bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("I'm sorry, that's an invalid input.\n")
          bet = int(input("How much do you want to bet?\n"))
        break
      except ValueError:
        print("You must enter a number for your bet.\n")
    totalPlays += 1
    blackjackPlays += 1
    #Draw cards, two at first
    for i in range(2):
      drawCard(hand, house)
      drawCard(house, hand)
    #Let player draw new cards until their score is above 21
    while handVal <= 21:
      printHand(hand, house)
      #Checks for 21
      if handVal == 21:
        print("21! You win!\n")
        bet *= 2
        break
      else:
        #Asks them if they want a new card
        newCard = input("Would you like another card? (y or n)\n")
        while (newCard != "y" and newCard != "n"):
          print("Please enter either \"y\" or \"n\".\n")
          newCard = input("Would you like another card? (y or n)\n")
        if newCard == "y":
          drawCard(hand, house)
          print("You drew the "+hand[len(hand) - 1])
        else:
          #Moves on if they don't want a new one
          print("Then your final score for this round is "+str(getValue(hand))+"\n")
          handVal = getValue(hand)
          break
      handVal = getValue(hand)
    if handVal > 21:
      print("Too bad!\n")
      bet *= -1
      print("Your score was too high.\n")
    #There's a better way to do this im sure, but only do this if handVal <= 21
    else:
      #House only draws until score above 15
      #Could play with this a little
      while getValue(house) < 16:
        print("The House draws a card!\n")
        drawCard(house, hand)
        houseVal = getValue(house)
        if houseVal > 21:
          print("House overdraws!\n")
    print("Both sides have their scores, now comparing...\n")
    thing = input("Press ENTER to continue\n")
    #Ensure correct values for final checks
    handVal = getValue(hand)
    houseVal = getValue(house)
    #Making sure both scores are 21 or lower
    if handVal <= 21 and houseVal <= 21:
      if handVal > houseVal:
        print("Your score is higher, you win!\n")
      elif houseVal > handVal:
        print("The House's score is higher, you lost.\n")
        bet *= -1
      else:
        print("You tied! No winner.\n")
        bet *= 0
    #If player overdraws
    elif handVal > 21:
      print("Sorry, you lost.\n")
    #If house overdraws
    else:
      print("Congrats, you won!\n")
    money += bet
    buffererererererererererer = input("Press ENTER to continue\n") 
  else:
    #Final floor!
    print("Welcome to the War table!\n")
    print("Draw a card, and whoever is higher wins!\n")
    print("But if we tie, the stakes are raised and we go to war!\n")
    #Reset everything
    hand = []
    house = []
    handVal = 0
    houseVal = 0
    while fool:
      try:
        bet = int(input("How much do you want to bet?\n"))
        while ((bet <= 0) or (bet > money)):
          print("I'm sorry, that's an invalid input.\n")
          bet = int(input("How much do you want to bet?\n"))
        break
      except ValueError:
        print("You must enter a number for your bet.\n")
    warPlays += 1
    totalPlays += 1
    #Draw one card and compare them
    drawCard(hand, house)
    drawCard(house, hand)
    print("Your card is: "+hand[0]+"\n")
    print("The House's card is: "+house[0]+"\n")
    handVal = getCardVal(hand[0])
    houseVal = getCardVal(house[0])
    bufferererererererer = input("Press ENTER to continue:\n")
    if handVal > houseVal:
      print("Congrats, you win!\n")
      money += bet
    elif houseVal > handVal:
      print("Tough, you lost.\n")
      money -= bet
    else:
      #Looked it up, this is how war works in real casinos
      print("Now it's time for things to heat up!\n")
      print("You have two options here: Either (s)urrender or (i)ncrease the stakes to go to war.\n")
      print("Surrendering means you lost half your bet, increasing the stakes doubles your bet.\n")
      choice = input("So, what'll it be? (s or i)\n")
      while choice != "s" and choice != "i":
        print("Choose one. Either (s)urrender or (i)ncrease.\n")
        choice = input("So, what'll it be? (s or i)\n")
      if choice == "s":
        print("If that's your choice, so be it.\n")
        money -= (.5 * bet)
        money = int(money)
      else:
        print("Oh yeah, let's do this!\n")
        bet *= 2
        #In the unlikely scenario that a tie plays out more than twice, use while loop
        while handVal == houseVal:
          #Draw 3 cards, compare the last one drawn
          #Technically there's a possibility that we run out of cards. But, the odds of that are so low that idrc
          for i in range(3):
            drawCard(hand, house)
            drawCard(house, hand)
          handVal = getCardVal(hand[len(hand) - 1])
          houseVal = getCardVal(house[len(house) - 1])
          print("Your card is: "+hand[len(hand) - 1])
          print("The House's card is: "+house[len(house) - 1])
          if handVal > houseVal:
            print("Nice win, great war!\n")
            money += bet
          elif houseVal > handVal:
            print("Oof, terrible war for you.\n")
            money -= bet
          else:
            print("Tensions rise once more! It's time for war!\n")
            buffererererererererer = input("Press ENTER to continue\n")
    buffererererererer = input("Press ENTER to continue\n")
#Display stats after they either leave or lose all their money
stats()
