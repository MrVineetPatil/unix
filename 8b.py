from Area import *

while(1):
    c = int(input(
        "Enter 1 to find Area for circle\nEnter 2 to find Area for Rectangle\nEnter 3 to find Area for triangle\nEnter 4 to exit\n"))
    print()
    if c==1:
        r=int(input("Enter radius:"))
        print(area_cirle(r))
    elif c==2:
        x=int(input("Enter length:"))
        y=int(input("Enter Breadth:"))
        print(area_rectangle(x,y))
    elif c==3:
        a=int(input("Enter side lengths:"))
        b=int(input())
        c=int(input())
        print(area_triangle(a,b,c))
    elif c==4:
        break