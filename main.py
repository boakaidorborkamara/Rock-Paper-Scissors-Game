import random

options = ["R", "P", "S"]
def startGame():
    # prompt user for to select an option 
    user_selection =  input('Select an option from the list: R,P,S\n')
    # print(user_selection)


    # validate user option 
    while user_selection not in options:
        user_selection =  input('Please select a valid option: R,P,S\n')


    # generate random index 
    random_index = random.randint(0,2)


    # get computer selection
    computer_selection = options[random_index]
    print(computer_selection)


    # check if game is tie 
    if user_selection == computer_selection:
        print("Tie")
        startGame()
    elif user_selection != computer_selection: #find and announce winner
        
        print("winner announcement")
        print("value not the same")
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










































































