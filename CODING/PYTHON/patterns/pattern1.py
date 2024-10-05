n=int(input("enter a number:"))
def pattern1(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print('*', end='')
        print("\n")
# def pattern2(n):
for i in range(n+1, 1, -1):
    for j in range(i, 1, -1):
        print("*", end="")
    print("\n")
# pattern2(n)