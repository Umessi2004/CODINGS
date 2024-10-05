#question 1
str=input("enter a string: ")
def palindrome(str):
    revstr=''
    for i in str:
        revstr=i+revstr
    if revstr==str:
        print("the string is palindrome :)")
    else:
        print("the string is not palindrome :(")
palindrome(str)
#question 3
def vowel(str):
    vow='aeiouAEIOU'
    for i in str:
        if i in vow:
            continue
        else:
            print(i, "is consonant\n")
vowel(str)
#question 2
r1=int(input("enter row of the 1st matrix: "))
c1=int(input("enter column of the 1st matrix: "))
r2=int(input("enter row of the 2nd matrix: "))
c2=int(input("enter column of the 2nd matrix: "))
#matrix definition:
if r1==r2 and c1==c2:
    matrix1=[[0 for i in range (c1)] for j in range(r1)]
    matrix2=[[0 for i in range (c2)] for j in range(r2)]
for i in range(r1):
    for j in range(c1):
        matrix1[i][j]=int(input(f"enter the number for the {i}{j} index for 1st matrix: "))
for i in range(r2):
    for j in range(c2):
        matrix2[i][j]=int(input(f"enter the number for the {i}{j} index for 2nd matrix: "))
print("The 1st matrix is: \n", matrix1)
print("The 2nd matrix is: \n", matrix2)
def summation(matrix1, matrix2):
    matrix3=[[0 for i in range(c1)] for j in range(r1)]
    for i in range(r1):
        for j in range(c1):
            matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
    print("the resultant matrix is: \n")
    print(matrix3)
summation(matrix1, matrix2)


#question4
n=int(input("Enter a number to check if it's perfect square: "))
sqrt=n**0.5
if sqrt%1==0:
    print(f"the number {n} is a perfect square\n")
else:
    print(f"the number {n} is not a perfect square\n")
    
        