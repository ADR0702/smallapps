user=int(input("please ad the total value of money:\n"))


tens=user//10
rest=user%10

fives=rest//5
rest=rest%5

twos=rest//2
rest=rest%2

ones=rest//1



print(f"the are {tens} of ten bills, {fives} of five bills, {twos} of two's and {ones} bills of ones")