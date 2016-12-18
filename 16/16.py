import itertools
a ="00111101111101000"
while len(a) < 35651584:
    a = a+"0"+"".join("0" if x =="1" else "1" for x in a[::-1])

a= a[:35651584]
while len(a)%2 ==0:
    a = "".join("1" if a[x] ==a[x+1] else "0" for x in range(0,len(a), 2))
print(a)
