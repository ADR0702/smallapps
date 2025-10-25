brutwage=int(input("Please type your wage before taxes:\n "))

taxes= 0.45


employee=input("Are you working in IT field? Yes/No answer:\n")
employee2=input("Are you working part time? Yes/No answer:\n")

if employee=="yes":
    taxes-=0.10
if employee2=="yes":
    taxes-=0.05

net_worth= brutwage*(1-taxes)
print(f"Your Networth Monthly Paycheck is {net_worth}")