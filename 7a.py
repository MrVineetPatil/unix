d={}
def new(w,m):
    d[w]=m

def retrieve(w):
    if w not in d:
        return -1
    return d[w]

def same_meaning(m):
    l=[]
    for i,j in d.items():
        if j==m:
            l.append(i)
    if len(l)==0:
        return -1
    return l

def remove(w):
    if w not in d:
        return -1
    d.pop(w)
    return 1

def display_sorted():
    print('DICTIONARY')
    for i in sorted(d.keys()):
        print(i,':',d[i])

while(1):
    print('DICTIONARY MENU'.center(25,'*'))
    c=int(input("Press 1 to add new word and meaning\n"
            "Press 2 to retrieve meaning of the word\n"
            "Press 3 to find words with the same meaning\n"
            "Press 4 to remove a word and its meaning\n"
            "Press 5 to display dictionary in a sorted way\n"
            "Press 6 to exit\n"))
    if c==1:
        w,m=input("Enter new Word and its meaning as(word:meaning)").split(' : ')
        new(w,m)
        print('new entry added\n')
    if c==2:
        w=input("Enter word whose meaning is to be retrieved\n")
        k=retrieve(w)
        if k==-1:
            print("No meaning found for the word in the dictionary\n ")
        print('Meaning:',k)
    if c==3:
        m=input('Enter the meaning for which words with same meaning are to be found\n')
        k=same_meaning(m)
        if k==-1:
            print("No word with same meaning is found\n")
        for i in k:
            print(i,end=" ")
        print("These are the words with the same meaning\n")
    if c==4:
        w=input("Enter the word which is to be removed\n")
        k=remove(w)
        if k==-1:
            print("Word doesn't exist in dictionary\n")
        else:
            print("Word popped\n")
    if c==5:
        display_sorted()
    if c==6:
        break
