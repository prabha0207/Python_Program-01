x1,x2=input().split()
x3=[]
if(len(x1)!=len(x2)):
    print("no")
else:
    for i in range(len(x1)):
        if x1[i] in x3:
            continue
        else:
            x2=x2.replace(x2[i],x1[i])
            x3.append(x1[i])
    if x2==x1:
        print("yes")
    else:
        print("no")
