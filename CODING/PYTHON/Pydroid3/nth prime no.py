def prime(n):
	c=0
	for i in range(1, n+1):
		if n%i==0:
			c+=1
	if c==2:
		return True
	else:
		return False
def nthprime(w):
	l=[]
	n=0
	m=2
	while True:
		if prime(m):
			l.append(m)
			n+=1
		m=m+1
		if n==w:
			break
	print(l[-1])
N=int(input("enter:"))
nthprime(N)
			