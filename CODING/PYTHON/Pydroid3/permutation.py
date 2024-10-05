size=int(input("enter the size of the list:"))
nl=[]
rl=[]
for i in range(size):
              n=int(input("enter value of n:"))
              r=int(input("enter value of r:"))
              nl.append(n)
              rl.append(r)
for i in range(size):              
              n=nl[i]
              r=rl[i]
              nf=1
              for j in range(1,n+1):
                  nf=nf*j
              rf=1
              for j in range(1,n-r+1):
                  rf=rf*j
              p=nf/rf
              print("permutation:", p)
                      
              
                   