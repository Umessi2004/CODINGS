def question1():
    ran=int(input("enter the size of the list: "))
    l=list()
    for i in range(ran):
        li=int(input(f"INDEX {i}: "))
        l.append(li)
    n=int(input("enter a number to check: "))
    for i in range(len(l)):
        if n==l[i]:
            print(f"the number found at index {i}\n")
    
def question2():
    str=input("enter a string:")
    substr=input("enter a sub-string: ")
    for i in range(len(str)-len(substr)+1):
        if((str[i:i+len(substr)]==substr)):
            print(f" the {substr} is present in {str}")    
            
def question3():
    list=input("enter a commma separated list: ")
    list=[i.strip() for i in list.split(',')]
    res=[]
    for i in list:
        if i not in res:
            res.append(i)
    print(res)
        
def question4():
    n=int(input("enter the size of the list: "))
    l=[]
    for i in range(n):
        ni=int(input(f"enter the {i} number:"))
        l.append(ni)
    num=int(input("enter a number: "))
    l.sort()
    if (num<=n):
        print(f"the {num} largest number  is:", l[num-1])
    else:
        print("out of index!!")
 
def main():
    print("ASSIGNMENT 5")
    print("1.qustion 1\n2.question 2\n3.question 3\n4.question 4\n")
    n=int(input("enter a question number to run:"))
    if n==1:
        print("Find if a number is present in a list. \n")
        question1()
    elif n==2:
        print("Find if the sub-string exists in the string without using in operator.\n")
        question2()
    elif n==3:
        print("Input a comma separated list from console. Write a program to print this list after removing all duplicate values with original order reserved.\n")
        question3()
    elif n==4:
        print("Given a list A and a number n, find the n’th largest number. Example: If the input list is [5, 2, 1, 7, 4] and n is 3. The 3rd largest number is 4.\n")
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