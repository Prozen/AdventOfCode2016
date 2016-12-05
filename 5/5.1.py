import hashlib
from itertools import count

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()
startString = "ugkcyxxp"
password= list("________")
gen = (a for a in (md5(startString+ str(i)) for i in count(1)) if a.startswith("00000") and a[5] in "01234567")
while '_' in password:
    key = next(gen)
    if password[int(key[5])] =='_':
        password[int(key[5])] = key[6]
print("".join(password))
