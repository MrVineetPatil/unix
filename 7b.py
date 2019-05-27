def remove(l,r):
    k=[]
    k+=l
    if r in l:
        k.remove(r)
    return k

def subsetsum(l,t):
    k=[ (x,y,z) for x in l for y in remove(l,x) for z in remove(remove(l,x),y) if
            x+y+z==t]
    if len(k):
        return True
    return False
print("Enter the list elements:",end='')
l=[int(x) for x in input().split()]
t=int(input("Enter the target\n"))
print(subsetsum(l,t))