x0=10
y0=10
width=20
height=20

"""userx=int(input("please ad an x value:\n"))
usery=int(input("please ad an y value:\n"))

if userx > x0 and userx < x0 + width and usery > y0 and usery < y0 + height:
    print("it's in the zone")
       
else:
    print("it's not in the zone")
"""
for x in range(0, 40, 2):
    for y in range(0, 40, 2):
        print(f"x: {x:>2}, y: {y:>2}", end=" -- ")
        if x > x0 and x < x0 + width and y > y0 and y < y0 + height:
            print("it's in the zone")
        else:
            print("it's not in the zone")


            