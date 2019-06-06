x1,x2=input().split()
f=0
for i in range(int(x1),int(x2)+1):
    s=1
    u=0
    while s<=i:
        if i%s==0:
            u+=1
        s+=1
    if u==2:
        f+=1
print(f)
