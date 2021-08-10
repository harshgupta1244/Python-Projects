low = 1
high = 1000

print("Think about a number between {} and {}... ".format(low, high))


input("Press any key to start...")
guesses = 1
while True:
    print("\t\t Guess the number in the range of {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input(
        "My guess is {}. should i guess higher or lower? . Enter 'H' , 'L' , 'C' if my guess was correct : ".format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess + 1
    elif high_low == "c":
        print("i got the answer in {} guesses".format(guesses))
        break
    else:
        print("Please enter 'H' , 'L' , 'C'")
    guesses = guesses + 1
