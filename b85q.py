value=input()
l=[]
l1=[]
for i in range(0,len(value),2):
    l.append(value[i])

for i in range(1,len(value),2):
    l1.append(value[i])
print(''.join(map(str,l)),''.join(map(str,l1)))
