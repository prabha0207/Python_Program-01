n1=input()
n2=[]
for i in n1:
    n2.append(i)
n2[0]=n2[0].upper()
for i in range(1,len(n2)):
    if n2[i]==" ":
        n2[i+1]=n2[i+1].upper()
        continue
    elif n2[i].isupper() and n2[i-1]!=" ":
        n2[i]=n2[i].lower()
n3=''
for i in range(len(n2)):
    n3+=n2[i]
print(n3)
