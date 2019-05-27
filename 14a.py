from re import *
while(1):
    n,s=input("Enter Name and a phone no").split(':')
    r=search(r'\(\d{3}\)\ \d{3}\.\d{4}\ \#\d{4}',s)
    if r:
        print('Validated Correctly!!!')
        break
    else:
        print('please enter a valid phone no.')