s=0
t=eval(input("enter a tuple of integers:"))
l=list(t)
for i in range(len(l)):
    x=l[i]
    s=s+x**2
print("sum of the squares of the integers:", s)

    