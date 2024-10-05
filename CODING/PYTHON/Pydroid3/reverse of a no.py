def palindrome(a):
	rev=0
	while a!=0:
		n=a%10
		rev=rev*10+n
		a=a//10
	return rev	
a=int(input("enter:"))
print(palindrome(a))
				
		
		