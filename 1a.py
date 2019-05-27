f=open('example.txt','w')
print('File Opened in write mode:\n Enter input and press -1 to exit')
t=input()
while t!='-1':
    f.write(t+'\n')
    t=input()
f.close()
print("File opened in read mode:")
f=open('example.txt','r')
num_words=0
for line in f:
    words=line.split()
    num_words+=len(words)

f.close()
print('The no of words in file is:',num_words)