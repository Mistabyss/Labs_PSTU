from itertools import*
from itertools import groupby
n=int(input('Введите трехзначное число:'))
if len(str(n))!=3:
    print('Число не трёхзначное.')
    while len(str(n))!=3:
        n=int(input('Введите трехзначное число:'))
s=[]
sp=[]
num=permutations(str(n))
for a in num:
    s.append(a)
for a in range(len(s)):
    sp.append(int(s[a][0]+s[a][1]+s[a][2]))
print(list(set(sp)))
print(max(sp))
