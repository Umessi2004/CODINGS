import pickle
print("-------------🙏SHOE MANAGEMENT🙏‐--------")
while True:
	print("1.add new record")
	print("2.Display all the record")
	print("3.search  a record")
	print("4.exit from the record")
	ch=int(input("enter your choice from 1 to 4 "))
	if ch==4:
		print("यह तो शुरू होने से पहले ही ख़तम होगया")
		break
	elif ch==1:
			f=open("shoes.dat", 'ab')
			name=input("ENTER YOUR NAME:")
			s_id=input("ENTER SHOE ID:")
			brand=input("ENTER BRAND NAME:")
			type=input("SHOE TYPE:")
			price=input("ENTER PRICE:")
			rec=[name, s_id, brand, type, price]
			pickle.dump(rec,f)
			f.close()
	elif ch==2:
			 f=open("shoes.dat", "rb")
			 try:
			 	while True:
			 		x=pickle.load(f)
			 		print(x)
			 except EOFError:
			 	print("Reached to the end of the file:")
			 	f.close()
	elif ch==3:
			 f=open('shoes.dat', 'rb')
			 rn=input("ENTER ID OF THE SHOES TO SEARCH-->")
			 try:
			 	while True:
			 		x=pickle.load(f)
			 		if x[1]==rn:
			 			print("SHOE DETAILS FOUND🤩")
			 			print(x)
			 			break		
			 except EOFError:
			 	print("SHOE DETAILS NOT FOUND😶‍🌫🥲")
			 	f.close()
	else:
		print("stfu🍑")
		break
					 									