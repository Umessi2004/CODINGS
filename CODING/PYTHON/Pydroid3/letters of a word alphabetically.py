l=[]
w=input("enter a word:")
for i in w:
    n=ord(i)
    l.append(n)
l.sort()
m=[]
for j in l:
    n=chr(j)
    m.append(n)
print(m)        