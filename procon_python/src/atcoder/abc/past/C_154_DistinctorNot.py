n=int(input())
a=list(map(int,input().split()))
len_lista=len(a)
set_a=set(a)
len_seta=len(set_a)
if(len_lista==len_seta):
    print("YES")
else:
    print("NO")