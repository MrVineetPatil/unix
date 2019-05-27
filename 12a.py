def partition(l):
    for i in l:
        if i.upper()>='A' and i.upper()<='M':
            print(i)
print("Enter the name of soccer players:",end='')
l=[x for x in input().split()]
partition(l)