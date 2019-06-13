value=input()
value=list(value)
ans=0
for i in value:
      if(value.count(i)==2):
          ans=ans+1
if(ans==0):
     print("Yes")
else:
     print("No")

