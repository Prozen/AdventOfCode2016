visited =  set()
visited.add((1,1))

def is_wall(pos):
    return sum(1 for x in bin(pos[0]*pos[0] + 3* pos[0] + 2*pos[0]*pos[1] + pos[1] + pos[1]*pos[1] +1350) if x=='1') %2

def next_pos(pos):
    nexts=[]
    x = pos[1][0]
    y = pos[1][1]
    for (i,j) in [(x+1,y),(x-1,y), (x,y+1), (x,y-1)]:
        if not is_wall((i,j)) and i > 0 and j > 0 and (i,j) not in visited:
            visited.add((i,j))
            nexts.append((pos[0]+1,(i,j)))
    return nexts

to_visit=[(0,(1,1))]
current = to_visit[0]
while current[0] < 55:
    print(len(visited))
    current = to_visit[0]
    to_visit = to_visit[1:] + next_pos(current)
print(visited)
