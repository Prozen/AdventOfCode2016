import hashlib
from itertools import count

def md5(s):
    for i in range(2017):
        s =hashlib.md5(s.encode()).hexdigest().lower()
    return s


def get_keys(hashes):
    counter = 0
    potentials = {}
    for hash in hashes:
        counter = counter +1
        for v in potentials.values():
            v[1].append(hash)
        for k,v in potentials.items():
            if len(v[1]) > 999:
                del potentials[k]
                if any(v[0] in x for x in v[1]):
                    print(v[2])
                    yield(k)
                break
        triplet = get_triplet(hash)
        if triplet: potentials[hash] = (triplet,[], counter)

def get_triplet(hash):
    if len(hash) < 3: return None
    if hash[0]== hash[1] and hash[1] == hash[2]: return hash[0]*5
    return get_triplet(hash[1:])
salt = "ihaygndm"
gen = get_keys((md5(salt + str(i)) for i in count(1)))
for i in range(64):
    next(gen)
