keyboard= ["qwertyuiop", "asdfghjkl;", "zxcvbnm,./"]
ch=input()
str=list(input())
result=""
for i in range(len(str)):
    for row in keyboard:
        if row.find(str[i])!=-1:
            if ch=='R':
                if row.find(str[i])!=0:
                    str[i]=row[row.find(str[i])-1]
            else:
                if row.find(str[i])!=9:
                    str[i]=row[row.find(str[i])+1]
            break
print(result.join(str))