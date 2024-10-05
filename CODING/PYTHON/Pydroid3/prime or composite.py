f=1
n=int(input("enter"))
for i in  range(2,n):
	if  n%i==0:
		f=f+1
if f==1:
	print ("prime")
else:
	print("composite")
														