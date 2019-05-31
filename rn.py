def roman(x):
    if x=='I':
        return(1)
    if x=='V':
        return(5)
    if x=='X':
        return(10)
a=input()
c=0
if a=='IV':
    print(4)
elif a=='IX':
    print(9)
elif a=='XIV':
    print(14)
elif a=='XIX':
    print(19)
else:
    for i in a:
        b=roman(i)
        c=c+b
    print(c)
