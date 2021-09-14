lst=list(map(int,input().strip().split()))[:4]
total=max(lst)

for num in lst:
    if(num!=total):
        print(total-num)