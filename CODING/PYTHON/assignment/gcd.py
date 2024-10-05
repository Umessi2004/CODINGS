a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
for i in range(1, a+1):
		if a%i==0 and b%i==0:
			h=i
print("the gcd of", a, "and", b," is: ",h)