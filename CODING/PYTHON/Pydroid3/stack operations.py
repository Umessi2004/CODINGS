def push(l,e):
	l.append(e)
	print("ELEMENT ADDED SUCCESSFULLY😃")
def isempty(l):
	if len(l)==0:
		return True
	else:
		return False
def pop(l):
	if isempty(l):
		print("STACK UNDERFLOW ERROR😬😬")
	else:
		l.pop()
		print(l)
def peek(l):
	if isempty(l):
		print("STACK UNDERFLOW😮‍💨")
	else:
		print("THE PEEK EELEMENT OF THE STACK:", l[-1])
def display(l):
	a=l[::-1]
	print(a)
l=[]
print("------🙏WELCOME TO STACK OPERATIONS🙏----")
while True:
	print("1.PUSH")
	print("2.POP")
	print("3.PEEK")
	print("4.DISPLAY")
	print("5.EXIT")
	ch=int(input("ENTER OPTIONS FROM 1 TO 5"))
	if ch==1:
		e=int(input("ENTER AN ELEMENT🤔"))
		push(l,e)
	elif ch==2:
		pop(l)
	elif ch==3:
		peek(l)
	elif ch==4:
		display(l)
	elif ch==5:
		print("EXITING OPERATION🐷")
		break
	else:
		print("THE ENTERED NO. IS OUT OF CONTEXT🤥")
																
													
												