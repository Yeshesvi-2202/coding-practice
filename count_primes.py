n=int(input())
p=[-1]*n
for i in range(2,n):
    if p[i]==-1:
        for j in range(i*i,n,i):
            p[j]=1
ans=[]
for i in range(2,n):
    if p[i]==-1:
        ans.append(i)
print(ans)
