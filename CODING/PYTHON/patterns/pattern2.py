n=int(input("enter a number: "))
for i in range(0, n):
    #for space
    for j in range(0, n-i-1):
        print(" ", end='')
    for j in range(0, i*2+1):
        print("*", end='')
    for j in range(0, n-i-1):
        print(" ", end='')
    print("\n")

