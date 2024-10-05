def question1():
    def leftmost(n, target):
        left,right=0,len(n)-1
        first_pos =-1
        while left<=right:
            mid=(left+right)//2
            if n[mid]==target:
                first_pos= mid
                right=mid - 1
            elif n[mid] < target:
                left=mid + 1
            else:
                right = mid - 1
        return first_pos
    def rightmost(n, target):
        left,right=0,len(n)-1
        last_pos =-1
        while left<=right:
            mid=(left+right)//2
            if n[mid]==target:
                last_pos= mid
                left=mid+1
            elif n[mid] < target:
                left=mid + 1
            else:
                right = mid - 1
        return last_pos
    n=int(input("enter the size of the list: "))
    l=[]
    for i in range(n):
        xi=int(input("enter the no."))
        l.append(xi)
    x=int(input("enter the target value: "))
    start=leftmost(l,x)
    end=rightmost(l,x)
    print([start, end])
def question2():
    def search(l,target):
        ele={}
        for i in l:
            if i in ele:
                ele[i]+=1
            else:
                ele[i]=1
        if target in l:
            return ele.get(target)
        else:
            return 0
    n=int(input("enter the size of the list: "))
    l=[]
    for i in range(n):
        xi=int(input("enter the no."))
        l.append(xi)
    l.sort()
    target=int(input("enter the value to search: "))
    val=search(l,target)
    if val==0:
        print("The element is not found")
    else:
        print(f"the ele found {val} times")
def question3():
    s1=input("enter first string: ")
    s2=input("enter second string: ")
    s1.lower()
    s2.lower()
    s1.replace(" ", "")
    s2.replace(" ", "")
    if sorted(s1)==sorted(s2):
        print("Both are Anagram")
    else:
        print("No anagram")
def question4():
    def isprime(n):
        c=0
        for i in range(2, n+1):
            if n%i==0:
                c+=1
        if c==1:
            return n
    def primecount(n):
        c=0
        for i in range(1, n+1):
            if isprime(i):
                c+=1
        return c
    n=int(input("enter a number: "))
    print("the prime numbers upto the nth number is: ")
    print(primecount(n))
def main():
    print("ASSIGNMENT 11")
    print("1.qustion 1\n2.question 2\n3.question 3\n4.question4\n")
    n=int(input("enter a question number to run:"))
    if n==1:
        print("Given an array of integers sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found, return [-1, -1]. \n")
        question1()
    elif n==2:
        print("Given an array of integers sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found, return [-1, -1]. \n")
        question2()
    elif n==3:
        print("Write a function to check if two strings are anagrams of each others\n")
        question3()
    elif n==4:
        print("Write a function that takes a integer n as input and calculate the number of prime numbers appears from 1 to n. \n")
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