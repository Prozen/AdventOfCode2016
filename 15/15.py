from itertools import count

print(next(i for i in count(0) if (12+i)%13 ==0 and (2+i)%5==0 and (14+i)%17==0 and (4+i)%3==0 and (7+i)%7==0 and (23+i)%19==0 and (7+i)%11==0))
