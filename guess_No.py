import random

def guess():
        while True:    
            number = random.randint(1,10)
            attempt = 0
            max_attempt = 3
            while attempt < max_attempt:
                try:    
                    choice = int(input("Guess the Number from 1 to 10: "))

                    if(number < choice):
                        print(f"{choice} is too High.")
                    elif(number > choice):
                        print(f"{choice} is too Low.")
                    else:
                        print("You guessed the right Number,congrats...!")
                        break

                    attempt += 1
                    if attempt < max_attempt:
                        print("try again...\n")
                    else:
                        print("you've reached to the limit...")
                        print(f"The correct Number was: {number} \n")

                except ValueError:
                    print("Invalid Value, Please Enter Number only...")
                    
            again = input("Do you want to play again(Y/N): ").lower()
            if again != 'y':
                print("thanks for playing...\n")
                break      

guess()