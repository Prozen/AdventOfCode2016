def stringToInstruction(s):
    return s[:1], int(s[1:])
startPos = ('N', 0, 0)
instructionsDirty = "R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2"
instructions = [ stringToInstruction(x.strip()) for x in instructionsDirty.split(",")]

def moveState(pos, instruction):
    (direction, x, y) = pos
    (turn, steps) = instruction
    if direction == 'N':
        if turn == 'R':
            return 'E', x + steps, y
        elif turn == 'L':
            return 'W', x - steps, y
    elif direction == 'S':
        if turn == 'L':
            return 'E', x + steps, y
        elif turn == 'R':
            return 'W', x - steps, y
    elif direction == 'E':
        if turn == 'L' :
            return 'N', x, y +steps
        if turn == 'R' :
            return 'S', x, y -steps
    elif direction == 'W':
        if turn == 'R' :
            return 'N', x, y +steps
        if turn == 'L' :
            return 'S', x, y -steps

pos = startPos
for instruction in instructions:
    pos = moveState(pos, instruction)
print(pos)
