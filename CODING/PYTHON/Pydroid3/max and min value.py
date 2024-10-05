import random 
l=[]
for I in range(1,31):
    n=random.randrange(30)
    l.append(n)
print(l)   
max=0
min=30
for i in l:
    if min>=l[i]:
        min=l[i]
    if max<=l[i]:
        max=l[i]
print(max)
print(min)             