import random

options = ["R", "P", "S"]
def startGame():
    # prompt user for to select an option 
    user_selection =  input('Select an option from the list: R,P,S\n')


    # validate user option 
    while user_selection not in options:
        user_selection =  input('Please select a valid option: R,P,S\n')
    


    # generate random index 
    random_index = random.randint(0,2)


    # get computer selection
    computer_selection = options[random_index]



    # print player selection
    # HUMAN 
    if user_selection == "R":
        print("Player (Rock)")
    elif user_selection == "P":
            print("Player (Paper)")
    elif user_selection == "S":
        print("Player (Scsissors)")

    # COMPUTER 
    if computer_selection == "R":
        print("CPU (Rock)")
    elif computer_selection == "P":
            print("CPU (Paper)")
    elif computer_selection == "S":
        print("CPU (Scsissors)")



    # check if game is tie 
    if user_selection == computer_selection:
        print("Tie")
        startGame() # restart the game after game is tie 
    elif user_selection != computer_selection:
        #find and announce winner the winner after the is not tie
        if user_selection == "R" and computer_selection == "S":
            print("Human Wins")
        elif user_selection == "S" and computer_selection == "R":
            print("Computer wins")
        elif user_selection == "P" and computer_selection == "S":
            print("Computer wins")
        elif user_selection == "S" and computer_selection == "P":
            print("Computer wins")
        elif user_selection == "P" and computer_selection == "R":
            print("Computer wins")
        elif user_selection == "R" and computer_selection == "P":
            print("Computer wins")
        elif user_selection == computer_selection:
            print("game tie")



# invoke the fnx 
startGame()










































































