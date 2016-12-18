from itertools import combinations
state = (0, 1,{1:['SG','SM','PM','PG','EG','EM','DG','DM'], 2:['TG','RG','RM','CG','CM'], 3:['TM'], 4:[]})
states = [state]
visited = set()

def state_to_tuple(state):
    positions = []
    for l in "SPEDTRC":
        gfloor = 0
        mfloor = 0
        for k,v in state[2].items():
            if l+"G" in v: gfloor = k
            if l+"M" in v: mfloor =k
        positions.append((gfloor,mfloor))
    return (state[1], tuple(sorted(positions)))

def is_not_visited(state):
    return state_to_tuple(state) not in visited

def is_safe(state):
    for floor_stuff in state[2].values():
        for e in floor_stuff:
            if 'M' in e and e[0] + 'G' not in floor_stuff and any('G' in x for x in floor_stuff):
                return False
    return True

def next_states(state):
    next_states = []
    current_floor =state[1]
    next_floors =  list(filter(lambda x : x > 0 and x < 5, [current_floor-1, current_floor+1]))
    stuff_on_floor = state[2][current_floor]
    for pair in combinations(stuff_on_floor, 2):
        for floor in next_floors:
            new_positions =  {k:v for (k,v) in state[2].items() if k != floor and k!= current_floor}
            new_positions[current_floor] =[x for x in stuff_on_floor if x not in pair]
            new_positions[floor] = state[2][floor] + list(pair)
            next_states.append((state[0]+1, floor, new_positions))
    for i in stuff_on_floor:
        for floor in next_floors:
            new_positions =  {k:v for (k,v) in state[2].items() if k != floor and k!= current_floor}
            new_positions[current_floor] =[x for x in stuff_on_floor if x != i]
            new_positions[floor] = state[2][floor] + [i]
            next_states.append((state[0]+1, floor, new_positions))
    nexts = list(filter(is_not_visited, filter(is_safe,next_states)))
    for x in nexts:
        visited.add(state_to_tuple(x))
    return nexts



visited.add(state_to_tuple(state))
while len(states[0][2][4])!=14:
    states = states[1:] + next_states(states[0])
print(states[0])
