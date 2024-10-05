def question1():
    products = [{'name': 'orange', 'price': 20},{'name': 'apple', 'price': 8},{'name': 'banana', 'price': 10},{'name': 'kiwi', 'price': 30}]
    print(f"the name of product higher than 10 is:")
    for i in products:
        if i['price']>10:
            print(f"{i['name']}")
            
def question2():
    product_quantities=[13, 5, 6, 10, 11]
    prices=[1.2, 6.5, 1.0, 4.8, 5.0]
    total=[product_quantities[i]*prices[j] for i in range(len(product_quantities)) for j in range(len(prices)) if i==j]
    sum=0.00
    print(total)
    for i in range(len(total)):
        sum=sum+total[i]
    print(f"Total price is {sum}")
    
def question3():
    votes=[]
    while True:
        vote=input("Vote a person: [a,b,c]")
        votes.append(vote)
        i=input("continue??[y/n] : ")
        if i=='y' or i=='Y':
            continue
        else:
            break
    print(f"The resultant vote is: {votes}")
    freq={}
    for i in votes:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    print(f"The resultant poll is: {freq}")
    max=0
    for i in freq:
        if max< freq[i]:
            max=freq[i]
    for i in freq:
        if freq[i]==max:
            print(f"The winner candidate is: {i}")
            
def main():
    print("ASSIGNMENT 8")
    print("1.qustion 1\n2.question 2\n3.question 3\n")
    n=int(input("enter a question number to run:"))
    if n==1:
        print("Given a list of products, print out the name of all the products with a price higher than 10.\n")
        question1()
    elif n==2:
        print("Take two list of numbers the products quantities and the prices. Calculate total price per product. (Use list comprehension)\n")
        question2()
    elif n==3:
        print("Write a function which takes a list of votes for candidates, find out who is the winner.\n")
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