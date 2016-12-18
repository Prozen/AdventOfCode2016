instructions = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 14 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5
""".splitlines()
registers = {'a':0,'b':0,'c':1,'d':0}

def to_int(a):
    return int(a) if a.isdigit() else registers[a]


i = 0
while i < len(instructions):
    parts = instructions[i].split()
    if parts[0] == 'cpy':
        registers[parts[2]] = to_int(parts[1])
        i = i+1
    elif parts[0] == 'inc':
        registers[parts[1]] = registers[parts[1]] +1
        i = i+1
    elif parts[0] == 'dec':
        registers[parts[1]] = registers[parts[1]] -1
        i = i+1
    elif parts[0] == 'jnz':
        if to_int(parts[1])!=0:
            i = i + int(parts[2])
        else :
            i=i+1
    print(registers)
