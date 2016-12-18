import hashlib
pass_code = "udskfozm"

def md5(s):
    return hashlib.md5(s.encode()).hexdigest().lower()
def next_steps(state):
    my_hash = md5(pass_code+state[2])[:4]
    positions = "UDLR"
    next_steps =[]
    for i in range(len(positions)):
        if my_hash[i] in "bcdef":
            if positions[i]=="U":
                next_steps.append((state[0], state[1]-1, state[2]+"U", state[3]+1))
            elif positions[i]=="D":
                next_steps.append((state[0], state[1]+1, state[2]+"D", state[3]+1))
            elif positions[i]=="L":
                next_steps.append((state[0]-1, state[1], state[2]+"L", state[3]+1))
            elif positions[i]=="R":
                next_steps.append((state[0]+1, state[1], state[2]+"R", state[3]+1))
    return [x for x  in next_steps if x[0] > -1 and x[1] > -1 and x[0] < 4 and x[1] < 4]

states=[(0,0,"",0)]
longest =[]
while states:
    if states[0][:2]==(3,3):
        longest.append(states[0][3])
        states = states[1:]
    else:
        states=states[1:]+next_steps(states[0])
print(max(longest))
