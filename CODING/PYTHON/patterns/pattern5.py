n=int(input("enter a number: "))
for i in range(n):
    for j in range(i+1):
        if(i+j)%2==0:
            print(1, end='')
        else:
            print(0, end='')
    print("\n")