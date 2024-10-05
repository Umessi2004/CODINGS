a=0; b=1
t=()
t=t+(a,b)
n=int(input("enter the range of fibonacci no.:")) #fibonacci series
for i in range(n-2):
    c=a+b
    t=t+(c,)
    a=b
    b=c
print(t)    

        