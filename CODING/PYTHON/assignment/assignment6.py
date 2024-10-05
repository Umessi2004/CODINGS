def question1():
    heads=35
    legs=94
    for chicken in range(heads+1):
        rabbit=heads-chicken
        if rabbit*4 + chicken*2 == legs:
            print(f"the no. of chicken is: {chicken} and rabbit is :{rabbit}")
            break
        
def question2():
    n1=int(input("enter size of the 1st list: "))
    n2=int(input("enter size of the 2nd list: "))
    l1=[]
    l2=[]
    for i in range(n1):
        l1.append(int(input(f"enter index {i} no. for 1st list: ")))
    print("\n")
    for i in range(n2):
        l2.append(int(input(f"enter index {i} no. for 2nd list: ")))
    l3=[(i,j) for i in l1 for j in l2 if i!=j]
    print(f"the Unique list is: {l3}")
    
def question3():
    str=input("enter a sentence: ")
    words=str.split(' ')
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=freq[word]
        else:
            freq[word]=1
    print(f"{freq}")
       
def main():
    print("ASSIGNMENT 6")
    print("1.qustion 1\n2.question 2\n3.question 3\n")
    n=int(input("enter a question number to run:"))
    if n==1:
        print("Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?\n")
        question1()
    elif n==2:
        print("Take two list of numbers and generate a list of tuples that are combo of the n such that two numbers in the pair are not equal Use list comprehension.\n")
        question2()
    elif n==3:
        print("Take a sentence and output the frequency of words in the sentence take a sentence as input \n")
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