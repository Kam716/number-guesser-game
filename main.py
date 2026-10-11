import random #Imports random folder, allows machine to choose a random number 

playing = True

while playing: 
    computer = random.randint(1,100)
    print('Computer has chosen a number between 1-100, try to guess it and we will tell you if its lower or higher!')
    user = int(input('Choose a number:'))

    while user != computer:
        if user < computer:
            print("Higher!")
        elif user > computer:
            print("Lower!")
        user = int(input('Choose a number:')) #User chooses a new number 

    print("You got it right! The number was " + str(computer)) 

    again = input('Play again? (y/n): ')
    if again != 'y':
        playing = False

print("Thanks for playing!")

