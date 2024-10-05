n=int(input("enter a  number: "))
for i in range(n):
    #for space
    for j in range(0, n-i-1):
        print(" ", end='')
    #for stars
    for j in range(0, i*2+1):
        if j==0 or j==2*i:
            print("*", end='')
        else:
            print(' ', end='')#for spaces inside triangle
    print(' '*i, end='')
    print("\n")
    if i==n-1:
        print('*'*(2*i+1))#for last row