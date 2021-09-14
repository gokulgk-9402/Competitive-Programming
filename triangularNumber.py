tn=0
n=int(input())
if(n==0):
    print('YES')
for i in range(n):
    tn+=i+1
    if(tn==n):
        print('YES')
        break
    elif (tn>n):
        print('NO')
        break