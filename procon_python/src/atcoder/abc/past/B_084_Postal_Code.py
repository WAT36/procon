a,b=map(int,input().split())
s=input()
try:
    if(s[a]=="-"):
        num=s[:a]+s[a+1:]
        x=int(num)
        print("Yes")
    else:
        print("No")
except:
    print("No")