username=input()
distinct=set(username)
if(len(distinct)%2):
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')