import random
min_val = 1
max_val = 6
roll_again = "Y"
while roll_again == "Yes" or roll_again == "Y" or roll_again == "yes" or roll_again == "y":
    print("Rolling Dice Again...")
    print("The Value are: ")
    # Generating random numbers from 1 to 6
    print(random.randint(min_val, max_val))

    roll_again = input("Roll the dice again?")
