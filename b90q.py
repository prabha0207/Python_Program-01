number=list(input())
value=[]
for i in number:
    if(i.isdigit()):
        value.append(i)
print(''.join(value))
