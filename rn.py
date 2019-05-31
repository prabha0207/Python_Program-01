def roman(y):
    if y=='I':
        return(1)
    if y=='V':
        return(5)
    if y=='X':
        return(10)
i=input()
c=0
if i=='IV':
    print(4)
elif i=='IX':
    print(9)
elif i=='XIV':
    print(14)
elif i=='XIX':
    print(19)
else:
    for i in a:
        b=roman(i)
        c=c+b
    print(c)
