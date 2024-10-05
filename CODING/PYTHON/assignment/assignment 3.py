str1=input("enter 1st string: ")
str2=input("enter 2nd string: ")
l1=len(str1)
l2=len(str2)
count1=0
for i in str1:
    if i.isalpha():
        count1+=1
print("number of alphabets in 1st string: ", count1)#question 1
# print("lenght of 2nd string: ", l2)

#question 2
def larger(l1,l2):
    if(l1>l2):
        print(str1, "is the largest")
    elif(l2>l1):
        print(str2, "is the largest")
    else:
        print("both the strings are of same length")#question 2
larger(l1,l2)


#question 4
sen=input("enter a sentence:")
letters=0
digits=0
for i in sen:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
    else:
        continue
print("the no. of letters in this sentence is: ", letters)#question 4
print("the no. of digits in this sentence is: ", digits)#question 4

#question 3
while True:
    year=int(input("ENTER A YEAR TO CHECK: "))
    if (year%4==0 and year%100!=0) or year%400==0:
        print("its a leap year")
    else:
        print("its not a leap year")
    x=input("do you want to continue[y/n]: ")
    if x=='n' or x=='N':
        break
    else:
        continue