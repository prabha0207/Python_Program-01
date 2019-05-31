def roman(a):
    if a=='I':
        return(1)
    if a=='V':
        return(5)
    if a=='X':
        return(10)
x=input()
c=0
if x=='IV':
    print(4)
elif x=='IX':
    print(9)
elif x=='XIV':
    print(14)
elif x=='XIX':
    print(19)
else:
    for i in x:
        b=roman(i)
        c=c+b
    print(c)
