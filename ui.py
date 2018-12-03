from controller.controller import Game
class UI:
    def __init__(self):
        '''
        Constructor for UI class
        '''
        self.__game = Game()
    
    def gameUI(self):
        
        s,st = self.__game.computerMove()
        print(str(st))
        scor = 0
        for i in range(0,len(st)):
            if st[i] != ' ':
                scor = scor + 1
        print("YOUR SCORE: " + str(scor))
        while st != s and scor != 0:
            try:
                cmd = input(">>> ")
                print("\n")
                cmd = cmd.strip().split(' ')
                if len(cmd) != 6:
                    raise Exception("Invalid command!")
                x1 = cmd[1]
                y1 = int(x1)
                x2 = cmd[2]
                y2 = int(x2)
                x4 = cmd[4]
                y4 = int(x4)
                x5 = cmd[5]
                y5 = int(x5)
                if cmd[0] != "swap":
                    raise Exception("Invalid command!")
                if cmd[3] != "-":
                    raise Exception("Invalid command")
                st,scor = self.__game.playerMove(y1,y2,y4,y5,st,scor)
            except Exception as e:
                print(e)
            print(str(st))
            print("YOUR SCORE: " + str(scor))
            #print("\n")
            
        if st == s and scor != 0:
            print("\n")
            print("YOU WON!!!")
        else:
            print("\n")
            print("YOU LOST :(")
            
ui = UI()
ui.gameUI()