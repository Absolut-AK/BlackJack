import random

playerSum = 0
compSum = 0
cardPoints = [
2, 2, 2, 2,
3, 3, 3 ,3,
4, 4, 4, 4,
5, 5, 5, 5, 
6, 6, 6, 6,
7, 7, 7, 7,
8, 8, 8, 8,
9, 9, 9, 9,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
'a', 'a', 'a', 'a']
playerCards = []
compCards = []
#sums of player and computer
def count():
    global playerSum
    global compSum
    p = 0
    c = 0
    for p in range(0, len(playerCards)):
        try:
            playerSum += playerCards[p]
        except TypeError:
            pass
    for c in range(0, len(compCards)):
        try:
            compSum += compCards[c]
        except TypeError:
            pass
# win or lose
def loseOrWin():
    global playerSum
    global compSum
    count()
    if playerSum > 21:
        print("You lose")
    elif compSum > 21:
        print("You win")
    elif playerSum == compSum:
        print("It's a tie")

    goAgain = input("You want to try again? y/n: \n")
    if goAgain == 'y':
        gameRestart()
    elif goAgain == 'n':
        print("Thank you for playing")
    else:
        print("I am guessing that is a no :(")

def hit():
    global playerSum, cardPoints
    hitCards = random.choice(cardPoints)
    playerCards.append(hitCards)
    cardPoints.remove(hitCards)
    print(f"You hitted, your cards are {playerCards}")
    count()
    for i in playerCards:
        if i == 'a':
            if playerSum + 11 > 21:
                playerSum += 1
            else:
                playerSum += 11
    count()
    if playerSum < 21:
        hitAgain = input("Do you want to hit again? y/n \n")
        if hitAgain == 'y':
            hit()
        elif hitAgain == 'n':
            stay()
    elif playerSum > 21:
        count()
        loseOrWin()

def stay():
    computerTurn()

# computerTurns
def computerTurn():
    global compSum, cardPoints
    global playerSum
    compHitCards = random.choice(cardPoints)
    compCards.append(compHitCards)
    cardPoints.remove(compHitCards)
    count()
    for i in compCards:
        if i == 'a':
            if compSum + 11 > 21:
                compSum += 1
            else:
                compSum += 11
    print(f"Dealer Card is {compCards}")
    if compSum < playerSum:
        computerTurn()
    elif compSum > 21:
        loseOrWin()
    count()

def hitOrPass():
    hitOrPass = input("Do you want to hit? y/n: \n")

    if hitOrPass == 'y':
        hit()
    elif hitOrPass == 'n':
        stay()
    else:
        hitOrPass = input("You have to say y or n nothing other...(idiot) y/n?: \n")
    count()
# Start and restarts
def gameRestart():
    global playerSum, playerCards, compCards, cardPoints
    global compSum
    cardPoints = [
2, 2, 2, 2,
3, 3, 3 ,3,
4, 4, 4, 4,
5, 5, 5, 5, 
6, 6, 6, 6,
7, 7, 7, 7,
8, 8, 8, 8,
9, 9, 9, 9,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
10, 10, 10, 10,
'a', 'a', 'a', 'a']
    playerCards = []
    compCards = []
    compSum = 0
    playerSum = 0
    # First 2 player cards
    firstPcard = random.choice(cardPoints)
    playerCards.append(firstPcard)
    cardPoints.remove(firstPcard)

    secondPcard = random.choice(cardPoints)
    playerCards.append(secondPcard)
    cardPoints.remove(secondPcard)
    
    # First 2 computer/dealer cards
    firstCcard = random.choice(cardPoints)
    compCards.append(firstCcard)
    cardPoints.remove(firstCcard)

    secondCcard = random.choice(cardPoints)
    compCards.append(secondCcard)
    cardPoints.remove(secondCcard)
    count()
    print(f"Dealer cards are x & {compCards[1]} \n Your cards are {playerCards[0]} & {playerCards[1]}")
    hitOrPass()
gameRestart()