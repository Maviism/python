import random

class Player:
    name = ""
    point = 0
    
    def __init__(self, n):
        self.name = n
    
    def pointCounter(self):
        counter = random.randint(1,6)
        self.point += counter
        return counter

    def kararOyuncu(self, i):
        switcher = {
            0 : self.pointCounter(),
            1 : "tamam"
        }
        return switcher.get(i, "Invalid input")
    
player1 = Player("player 1")
bot = Player("Bot")
b = True

onGame = player1
while b:
    if onGame.point >= 50:
        print(onGame.name, " WIN")
        b = False
    else :
        if onGame == player1 :
            print(onGame.name, " is playing")
            print (onGame.name, " point is ", onGame.point)
            i = eval (input("Choose 0 for devam 1 for tamam "))
            print("")
            if i == 0 :
                temp = onGame.pointCounter()
                print(temp)
                if temp == 1 :
                    if onGame == player1:
                        onGame.point = 0
                        onGame = bot
                    else :
                        onGame.point = 0
                        onGame = player1
                else :
                    pass
            elif i == 1 :
                if onGame == player1:
                    onGame = bot
                else :
                    onGame = player1
            else :
                print("input undefinied")
        
        else :
            print(onGame.name, " is playing")
            print (onGame.name, " point is ", onGame.point)
            temp = onGame.pointCounter()
            print(temp)
            if temp == 1 :
                if onGame == player1:
                    onGame = bot
                else :
                    onGame = player1
            else :
                pass

        
    # if onGame.point >= 20 :
    #     print (onGame.name, " is win")
    #     b = False
    
    # if p != 1 :
    #     print (p)
    #     print (onGame.point)
    #     if(onGame != bot):
    #         onGame = bot
    #     else:
    #         onGame = player1
    # #else :
        
        

    


print("welcome to dice game")

