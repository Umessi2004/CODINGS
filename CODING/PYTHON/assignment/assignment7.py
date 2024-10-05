def question1():
    str1=input("enter a string:")
    str2=input("enter a string:")
    res=[]
    if len(str1)<len(str2):
        for i in range(len(str1)):
            if str1[i]==str2[i]:
                res.append(str1[i])
            else:
                break
    else:
        for i in range(len(str2)):
            if str1[i]==str2[i]:
                res.append(str2[i])
            else:
                break
    res=str(res)
    print(f"{res}")
    
def question2():
    dist=[10,20,30,40,50]
    time=[1,5,3,2,4]
    speed=[dist[i]/time[i] for i in range(len(dist))]
    print(speed)
    
def question3():
    a=float(input("enter the 1st side of triangle: "))
    b=float(input("enter the 2nd side of triangle: "))
    c=float(input("enter the 3rd side of triangle: "))
    a1=a**2
    b1=b**2
    c1=c**2
    def circumcenter(a,b,c):
        if a>b and b>c:
            return a/2
        elif b>c and c>a:
            return b/2
        else:
            return c/2
        
    def triangletype(a,b,c): 
        if a==b!=c or b==c!=a or c==a!=b:
            print("Isosceles triangle")
        elif a==b==c:
            print("Equilateral triangle")
        elif a1+b1==c1 or a1+c1==b1 or b1+c1==a1:
            print("the Triangle is Right-angled")
            radius=circumcenter(a,b,c)
            print(f"the radius of circumcenter of this Triangle is: {radius}")
        else:
            print("Scalen triangle")
    if a+b>c and b+c>a and a+c>b:
        print("the triangle is valid!\n")
        triangletype(a,b,c)
        
    else:
        print("the triangle is not valid\n")
        
def main():
    print("ASSIGNMENT 7")
    print("1.qustion 1\n2.question 2\n3.question 3\n")
    n=int(input("enter a question number to run:"))
    if n==1:
        print("Given a two strings find the longest common prefix for them.\n")
        question1()
    elif n==2:
        print("Accept two sequence of number, one for list of distance another forlist of time and return a list of speeds for respective distance and time values (use comprehension).\n")
        question2()
    elif n==3:
        print("Take an input for the 3 sides of a triangle from the user\na. check for a valid triangle sides\nb. Classify the triangle as Equilateral, Right-angled,Isosceles, Scalene (Default). Provided the given sides are valid\nc. Provided the triangle is valid and Right angled print the radius of circumcentre else return -1\n")
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