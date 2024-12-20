import random

def guess_the_number():
    random_number = random.randint(1, 100)
    guess_count = 0  

    print("I have selected a random number between 1 and 100. Can you guess what it is?")

    while True:  
            user_guess = int(input("Enter your guess: "))
            guess_count += 1  

            if user_guess < random_number:
                print("Too low! Try guessing a bigger number.")
            elif user_guess > random_number:
                print("Too high! Try guessing a smaller number.")
            else:
                print(f"Congratulations! You guessed the number in {guess_count} tries.")
                break 
            print("Please enter a valid integer.")

guess_the_number()