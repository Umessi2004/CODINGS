str1=input("enter 1st string: ")
str2=input("enter 2nd string: ")

ns1=int(input("enter 1st index for the 1st string: "))
ns2=int(input("enter 2nd index for the 1st string: "))#the condition is that index 
#should be smaller or equal to the size of string

print(str1[ns1])#question 1
print(str1[::-1])#question 2 about slicing
print(str1+' '+str2)#question 3
if (ns1>ns2):
    temp=ns1
    ns1=ns2
    ns2=temp
    print(str1[ns1:ns2])#question 4
else:
    print(str1[ns1:ns2])