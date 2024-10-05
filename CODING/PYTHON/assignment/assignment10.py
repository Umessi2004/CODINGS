def question1():
    str=input("enter a string: ")
    def pal(str):
        if len(str)<=1:
            return True
        if str[0]==str[-1]:
            return pal(str[1:-1])
        return False
    s=pal(str)
    print(s)
    
def question2():
    def max_size(items, capacity):
        items=[(value, weight, value/weight) for value, weight in items]
        items.sort(key=lambda x:x[2], reverse=True)
        max_item=0.0
        for value, weight, ratio in items:
            if capacity>0:
                if capacity>=weight:
                    max_item+=value   
                    capacity-=weight
                else:
                    max_item+=ratio*capacity
            else:
                break
        return max_item
    items = [(60, 10), (100, 20), (120, 30)] 
    capacity = 50
    print("the maximum item that can be stored is: ")
    val=max_size(items, capacity)
    print(val)
def question3():
    num=int(input("Enter a number:"))
    def add(num):
        if num%10==0:
            return num
        else:
            return num%10 + add(num//10)
    print(f"the sum of every digit of {num} is: ")
    sum=add(num)
    print(sum)
def main():
    print("ASSIGNMENT 10")
    print("1.qustion 1\n2.question 2\n3.question 3\n")
    n=int(input("enter a question number to run:"))
    if n==1:
        print("Write a recursive function that takes a string word as input and check if the given word is palindrome. Return True if string is palindrome else return False.\n")
        question1()
    elif n==2:
        print("Given a list of tuples contains weight (w) and value (v) pair for items and the capacity of a bag. Write a function that calculate the maximum item value that can be carried in the bag.\n")
        question2()
    elif n==3:
        print("Write a recursive function that takes an integer number (num) as input and add all the digits of the number. \n")
        question3()
    else:
        print("enter a valid option\n")  
while True:
    main()
    c=input("Do you want to Continue[y/n]: ")
    if c=='y' or c=='Y':
        continue
    else:
         break