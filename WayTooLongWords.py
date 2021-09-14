t=int(input())
while(t):
    word=input()
    if(len(word)>10):
        print("{}{}{}".format(word[0],len(word)-2,word[-1]))
    else:
        print(word)
    t-=1