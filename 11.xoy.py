x0=10
y0=10
width=20
height=20

userx=int(input("please ad an x value:\n"))
usery=int(input("please ad an y value:\n"))

if userx > x0 and userx < x0 + width and usery > y0 and usery < y0 + height:
    print("it's in the zone")
       
else:
    print("it's not in the zone")