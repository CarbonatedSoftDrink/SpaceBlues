def mainMenu():
    playerInput = 0
    loop = 1
    while loop == 1:
        print("Welcome to Space Blues!")
        print("1. Play Game\n2. How to Play\n3. Exit")
        playerInput = input()

        try:
            playerInput = int(playerInput)
        except:
            print("ouch!\n")
        else:
            if playerInput == 1:
                print("nice!")
                loop = 0
            elif playerInput == 2:
                print("i'll fill this out later.")
                loop = 0
            elif playerInput == 3:
                print("bye!")
                loop = 0
            else:
                print("i couldn't understand that answer, try again please!\n")

mainMenu()

