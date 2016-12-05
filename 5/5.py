import hashlib
from itertools import count

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()
startString = "abc"#"ugkcyxxp"
gen = (a[5] for a in (md5(startString+ str(i)) for i in count(1)) if a.startswith("00000"))
print("".join(next(gen) for _ in range(8)))
#md5("abc3231929"))
