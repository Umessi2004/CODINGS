n=int(input("enter a number: "))
for i in range(n):
    print('*'*i+' '*(n-i)*2+'*'*i)
for i in range(n, -1, -1):
    print('*'*i+' '*(n-i)*2+'*'*i)
