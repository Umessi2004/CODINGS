n=int(input("enter a number:"))
for i in range(1, n+1):
    #for number
    for j in range(1,i+1):
        print(j, end='')
    #for space
    print(' '*((n-i)*2), end='')
    #for number
    for j in range(i, 0, -1):
        print(j, end='')
    print("\n")