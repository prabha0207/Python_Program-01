n1,n2=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in a:
    if i%2!=0:
        ans.append(i)
for i in range(1,len(ans)+1):
    if i==n2:
        print(ans[i-1])
