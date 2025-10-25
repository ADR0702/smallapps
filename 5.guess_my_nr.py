import random

while True:
    user=int(input("Please guess a number from 1 to 10:\n"))
    computer_no= random.randint(1,10)
    if user == computer_no:
        print("Congrats! the number is correct ")
        break
    else:
        print("WRONG!Try Again\n")
    
