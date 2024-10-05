n=int(input("enter a number: "))
j=1
for i in range(1, n+1):
    count=1
    while count<=i:
        print(j, end=' ')
        count+=1
        j+=1
    print("\n")
    