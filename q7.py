x=input()
y=[]
z=''
for i in x:
    y.append(i)
for i in range(0,len(x),1):
    if i%2==0:
        y[i]=x[i+1]
    if i%2==1:
        y[i]=x[i-1]
for i in range(len(y)):
    z+=y[i]
print(z)
