t=int(input())
while(t):
    sus=0
    n=int(input())
    str=list(input())
    for i in range(len(str)-1):
        if str[i+1]!=str[i]:
            for j in range(i+1,len(str)):
                if str[j]==str[i]:
                    sus=1
                    break
    if(sus==1):
        print("NO")
    else:
        print("YES")            
    t-=1