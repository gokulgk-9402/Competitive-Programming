sumStrength=0

n=int(input())
listHeroes=list(map(int,input().strip().split()))[:n]
listHeroes.sort()

for i in range(n):
    sumStrength+=listHeroes[i]

m=int(input())

for i in range(m):
    listDragon=list(map(int,input().strip().split()))[:2]
    coinsC1=0
    coinsC2=0
    tempSum=sumStrength
    for j in range (n):
        if listHeroes[j]>=listDragon[0]:
            tempSum-=listHeroes[j]
            if j!=0:
                temp=listHeroes[j-1]
            break
    if tempSum==sumStrength:
        tempSum-=listHeroes[-1]
        coinsC1+=listDragon[0]-listHeroes[-1]
    
    if tempSum<listDragon[1]:
        coinsC1+=listDragon[1]-tempSum

    if listDragon[0]>temp:
        coinsC2+=listDragon[0]-temp

    tempSum=sumStrength-temp
    if tempSum<listDragon[1]:
        coinsC2+=listDragon[1]-tempSum

    if coinsC1<coinsC2:
        print(coinsC1)
    else:
        print(coinsC2) 