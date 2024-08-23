import random

def guess_number():
    random_num = random.randint(1, 100)
    attempts = 0

    while True:
        guessed_num = int(input("Enter a number between 1 and 100: "))
        attempts += 1

        if guessed_num < random_num:
            print("That's too low. Try again")
        elif guessed_num > random_num:
            print("That's too high. Try again")   
        else:
            print("Yay! You got it! That's a correct number in ", attempts, " attempts")  
            break


guess_number()           
