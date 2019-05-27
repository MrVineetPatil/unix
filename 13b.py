def rotatelist(l,n):
    if n==0:
        return l
    k=[l[-1]]
    for i in range(len(l)-1):
        k.append(l[i])
    return rotatelist(k,n-1)
print('Enter the list of elements:',end='')
lst=[int(x) for x in input().split()]
i=int(input("Enter no of rotations to be done:"))
print(rotatelist(lst,i))