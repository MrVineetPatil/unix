try:
    l={}
    print("Accessing l[1] from l={}")
    q=l[1]
except KeyError:
    print("KEY ERROR!!!!!")

try:
    a=1
    print("\na=1 and changing value to a=int('dog')")
    a=int('dog')
except ValueError:
    print("VALUE ERROR!!!!")

try:
    p=[1,2]
    print("\nAccessing p[3] from p=[1,2]")
    s=p[3]
except IndexError:
    print("INDEX ERROR!!!!")