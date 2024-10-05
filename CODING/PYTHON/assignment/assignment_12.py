# 1. Assume a fair dice rolled using a similar random integer generation 
# code. Rolled it for 500 times and print the number of times 1 to 6 
# has appeared
import random
dic={i:0 for i in range(1,7)}
for i in range (500):
    item=random.randint(1,6)
    if item in dic:
        dic[item]=dic[item]+1
    else:
        dic[item]=1
print("1st question")
print(" the number of times 1 to 6  has appeared")
print(dic)
print("\n")
# 2. Write a Python function to generate a random 
# a. alphabetical character.
# b. alphabetical string of arbitrary length and
# c. alphabetical string of a fixed length.
# list of letter 
print("2nd question")
list=[chr(i)for i in range(ord('a'),ord('z'))]

print(f"the random char is {random.choice(list)}")

# alphabetic string pf arbitary character

def arbitarycharcter(list):

    str=''.join(random.sample(list,random.randrange(len(list))))
    return str

r1=arbitarycharcter(list)
print(f"string of arbitary character is  {r1}")

# fixed string of 5 character

def fixedcharacter(list,k):
    str=''.join(random.sample(list,k))
    return str
r2=fixedcharacter(list,5)
print(f"string of fixed character is {r2}")
print("\n")

# 3. Write a Python function to create a list containing random integers
# and randomly select k items from the generated list
print("3rd question")
list2=[]
for i in range(random.randint(1,10)):
    item=random.randint(0,200)
    list2.append(item)
def randominteger(list2):
    return(random.sample(list2,random.randrange(1,len(list2))))

result=randominteger(list2)
print(f"randomly selected integer is \n{result}")
print("\n")

# 4. Write a function that takes a 2X2 square matrix as input. Calculate
# and return the determinant of the matrix.
# import numpy
row=2
col=2
matrix=[]
def creatematrix():
    for i in range(row):
        rows=[]
        for j in range (col):
            num=int(input("enetr the number"))
            rows.append(num)
        matrix.append(rows)
    return matrix
print("enter the numbers of the matrix ")
matrix=creatematrix()
for i in range(2):
    for j in range(2):
        print(matrix[i][j],end=" ")
    print()
det=matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
print(f"determinant is {det}")

