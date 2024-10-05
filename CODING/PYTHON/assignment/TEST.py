# # # # # # # # # print("hello world")
# # # # # # # # # a=7.89
# # # # # # # # # b=56
# # # # # # # # # print(a,b)
# # # # # # # # # x="jai mata di"
# # # # # # # # # print(x)
# # # # # # # # # a=int(input("enter a value"))
# # # # # # # # # print(a)
# # # # # # # # # x="hello"
# # # # # # # # # print(x)
# # # # # # # # x="umesh"
# # # # # # # # y="45.66789022"
# # # # # # # # print("hello i am {} and i have {}".format(x,y))#placeholder
# # # # # # # # z="this is {name:} and i have scored {cgpa:.2f} cgpa and rollnumber as{roll:}"
# # # # # # # # print(z.format(name="umesh", cgpa=8.94678))#it takes the round off value of the no.: 8.9468 to 8.95
# # # # # # # # # print(type(x))
# # # # # # # # import datetime
# # # # # # # # t=datetime.datetime.today()
# # # # # # # # print(f"{t:%B %d %Y}")
# # # # # # # # print(f"{{{{{{Hello, Geek}}}}}}")
# # # # # # # # n=5
# # # # # # # # s=f"n*n"
# # # # # # # # print(type(s))
# # # # # # # # print (type(n*n))\
# # # # # # # print("helo", end=" ") #printing in the same line
# # # # # # # print("india")
# # # # # # # print("1", "2", "3", "4")
# # # # # # # print("my marks in 1 st sem is: %3d" %(5189))
# # # # # # # s="umesh"
# # # # # # # print(s.center,(10,'-'))
# # # # # # # print(s.ljust(5,'-'))
# # # # # # # print(s.rjust(5,'-'))
# # # # # # #STRING slicing and concatenating and joining
# # # # # # x='umesh satpathi'
# # # # # # print(x[::-1])
# # # # # # print(x[-2:4])#will show no error 
# # # # # # print(x[2:39])# if the stop number is greater than the size of the string then it prints up to the end
# # # # # # print(" ".join(reversed(x)))#a new way of adding two strings
# # # # # # str1="umesh"
# # # # # # print(str1[0:4])#it slices the string from 0 to 3 and not 4!!!
# # # # # # str2="satpathi"
# # # # # # str3=str1+' '+str2 #adding 2 strings
# # # # # # print(str3)
# # # # # # print(str1[0:3]+str1[3:])#removing a char from a string by adding from 0 to 2 where 2 will be ignored and then 3 to last
# # # # # # String="{0:e}".format(123.4580967)#gives a exponential representation
# # # # # # print(String)  #centre               #left              #0           #1  
# # # # # # String1 = "\n{0:^16} was founded in {1:<10}!".format("GeeksforGeeks",2009)
# # # # # # print(String1)
# # # # # s="umesh"
# # # # # def reverse(s):
# # # # #     if len(s)==0:
# # # # #         return s
# # # # #     else:
# # # # #         return reverse(s[1:])+s[0]
# # # # # print(reverse(s))
# # # # # n=[1,2,3,4,5,6,7,8]
# # # # # i=0
# # # # # while i<=7:
# # # # #     if n[i]%2==0:
# # # # #         i+=1
# # # # #         print("even", end="")
# # # # #         print(i)
# # # # #     else:
# # # # #         i+=1
# # # # #         pass
# # # # # #using of map function
# # # # # def add(n):
# # # # #  return n**n
# # # # # num=[1,2,3,4,5,6,7,8]
# # # # # result=map(add, num)#can be done for list tuple and dictionary
# # # # # print(list(result))#we have to convert because the var: result is a single datatype not a sequence
# # # # # l=[1,2,3,4,5,6,7,8,9,0]
# # # # # print(l[0:6]) #last index is ignored
# # # x=[1,2,3]
# # # y=[1,2,3]
# # # listf=[(i,j) for i in x for j in y if i!=j]#using list comprehension
# # # print(listf)
# # # def com(x,y):
# # #     # if x!=y:
# # #     return (x,y)
# # # res=map(com, x,y)
# # # print(list(res))# in map function you can add the element of same index so the output is [(1,1),(2,2),(3,3)]
# # coordinates=(1,2,3)
# # x,y,z=coordinates #this is called unpacking 
# # print(x,y,z)
# # str='hello'
# # substr='ll'
# # print(str[2:2+len(substr):])
# # n=input("enter a number: ")
# # print(f"the multiplication table of {n} is: ")
# # try:
# #     for i in range(1, 11):
# #         print(f"{n}x{i}={int(n)*i}")
# # except Exception as v: #using try and except in python to handle with errors butifuly :)
# #     print(v)
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)