import random

options = ["R", "P", "S"]

# prompt user for to select an option 
user_option =  input('Select an option from the list: R,P,S\n')
print(user_option)


# validate user option 
while user_option not in options:
    user_option =  input('Please select a valid option: R,P,S\n')


# generate random index 
random_number = random.randint(0,2)
print(random_number)












































































