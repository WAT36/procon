n,k,m=map(int,input().split())
a=list(map(int,input().split()))
min_an=(m*n)-sum(a)
if(min_an<0):
    print(0)
elif(min_an>k):
    print(-1)
else:
    print(min_an)