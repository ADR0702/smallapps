while True:
    user=input("Please Add a number:\n")
    if user.isnumeric():
        user=int(user)

        if user % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
    else:
        print("you didn't add a number")