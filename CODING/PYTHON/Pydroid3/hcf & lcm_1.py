def lcm(a,b):#LCM 
	for i in range(a*b, 1, -1):
		if i%a==0 and i%b==0:#
			l=i
	return l
def hcf(a,b):#HCF
	for i in range(1, a+1):
		if a%i==0 and b%i==0:#
			h=i 
	return h			
a=int(input("enter first number:"))
b=int(input("enter 2nd number:"))
print(lcm(a,b), hcf(a,b))
