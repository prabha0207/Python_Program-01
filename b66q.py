x=int(input())
a1=0
for i in range(1,x):
    if(x%i==0):
        a1+=1
    else:
        continue
if(a1==1):
    print("yes")
else:
    print("no")
