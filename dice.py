import random
import time

DiceScore = (1, 2, 3, 4, 5, 6)
YourScore = 0
BotScore = 0

PlayDice = input("Do you want to play 'Roll the Dice'? [Y/N] ")
if PlayDice == "Y" or PlayDice == "y":
    while True:
        pTurn = True
        botTurn = False
        while pTurn:
            if YourScore >= 20:
                print("---------------")
                print("  YOU WIN  ")
                print("---------------")
                quit()    
            print(" ")
            print("Now it's you turn")
            RollDice = input("Press [ENTER] to roll your dice...")
            if RollDice == "":
                print("is rolling the dice")
                print(" ")
                time.sleep(3)
                yourDice = random.choice(DiceScore)
                if yourDice == 1:
                    yourPoint = 0
                    pTurn = False
                    botTurn = True
                    YourScore = YourScore + yourPoint
                    print("Your dice number = " +str(yourDice))
                    print("You get point = " +str(yourPoint))
                    print("Your Score = " +str(YourScore))
                    print(" ")
                else :
                    yourPoint = yourDice
                    YourScore = YourScore + yourPoint
                    print("Your dice number = " +str(yourDice))
                    print("You get point = " +str(yourPoint))
                    print("Your Score = " +str(YourScore))
                    print(" ")
                    option = input("Y for continue N for stop and switch to bot :")
                    if option == "y" or option =="Y":
                        pTurn = True
                        botTurn = False
                    elif option == "n" or option == "N":
                        pTurn = False
                        botTurn = True
                    else:
                        print("Invalid input")
                        option = input("Y for continue N for stop and switch to bot :")
                        
            
            time.sleep(1)
            print(" ")
            
        while botTurn:        
                if BotScore >= 20:
                    print("----------------")
                    print("   YOU LOSE   ")
                    print("----------------")
                    quit()
                print(" ")
                time.sleep(3)
                print("wait for the bot turn")
                botDice = random.choice(DiceScore)
                if botDice == 1:
                    botPoint = 0
                    pTurn = True
                    botTurn = False
                else :
                    botPoint = botDice
                    pTurn = False
                    botTurn = True
                BotScore = BotScore + botPoint
                print("Bot dice number = " +str(botDice))
                print("Bot get score = " +str(botPoint))
                print("Bot Score = " +str(BotScore))
                print(" ")
        
                
if PlayDice == "N" or PlayDice == "n":
        print("Goodbye...")
else:
        print("Wrong Input")

#Author by Salma sonia
#edited by Maviism
