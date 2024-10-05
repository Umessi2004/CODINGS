def question1():
    def check(l):
        max=min=l[0]
        sum=0
        for i in range(len(l)):
            if min>l[i]:
                min=l[i]
            if max<l[i]:
                max=l[i]
            sum+=l[i]
        avg=sum/len(l)
        return min,max,avg
    n=int(input("enter the size of the list: "))
    l=[]
    for i in range(n):
        ni=int(input(f"enter no.{i+1}: "))
        l.append(ni)
    print(f"the list is: {l}")
    min,max,avg=check(l)
    print(f"{min}\t{max}\t{avg}")
    
def question2():
    def check(str, matrix, r,c):
        f=0
        for i in range(r):
            for j in range(c):
                if str==matrix[i][j]:
                    print(f"The matrix found at index: ROW={i} COLUMN={j}")
                    f+=1
        else:
            if f==0:
                print("the character is not found!")
    row=int(input("enter the row size: "))
    col=int(input("enter the col size: "))
    matrix=[[0 for i in range(col)]for j in range(row)]
    for i in range(row):
        for j in range(col):
            matrix[i][j]=input(f"Enter the string.{i}.{j}: ")
    print(f"the Matrix is :{matrix}")
    str=input("enter a string to SEARCH...:")
    check(str, matrix, row, col)
    
def question3():
    def calculate(p,d):
        discount_price=p-((p*d)/100)
        return discount_price
    original_price=float(input("enter the original price of a product: "))
    while True:
        discount=int(input("enter the discount: "))
        if discount<=100:
            break
        else:
            print("The discount can't be more than 100!!")
            continue
    print(f"The discounted price is: {calculate(original_price, discount)}")
    
def question4():
    def dictionary(sen):
        words=sen.split()
        length=[len(i) for i in words]
        d={w:l for w,l in zip(words, length)}
        print(d)
    sen=input("enter a sentence: ")
    dictionary(sen)
    
def main():
    print("ASSIGNMENT 9")
    print("1.qustion 1\n2.question 2\n3.question 3\n4.question 4")
    n=int(input("enter a question number to run:"))
    if n==1:
        print(" Create an function that is agnostic to number of inputs and calculate minimum, maximum and average of the numbers. \n")
        question1()
    elif n==2:
        print("Write a function that takes input a matrix and a character. Print the row index and column index if the character is found else print Not found\n")
        question2()
    elif n==3:
        print("Write a function that calculates the discounted price of a product given its original price and the discount offered as a percentage. The function should: Take two arguments: \na. original_price: The original price of the product (floating-point number).\nb. discount_percent: The discount offered as a percentage (integer). \n")
        question3()
    elif n==4:
        print("write a function that takes a sentence as input and output a dictionary with word as the key and number of characters in the word as value. Use dictionary comprehension.\n")
        question4()
    else:
        print("enter a valid option\n")  
while True:
    main()
    c=input("Do you want to Continue[y/n]: ")
    if c=='y' or c=='Y':
        continue
    else:
         break