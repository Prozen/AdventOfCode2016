import itertools
def rows(row):
    while True:
        yield row
        next_row = [None]*len(row)
        for i in range(len(row)):
            if i ==0:
                next_row[i]= '^' if row[i+1]=='^' else '.'
            elif i==len(row)-1:
                next_row[i]= '^' if row[i-1]=='^' else '.'
            else:
                next_row[i]= '^' if row[i+1] != row[i-1] else '.'
        row = next_row

start="...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^"
print(sum(1 for y in itertools.islice(rows(start), 400000) for x in y if x =='.'))
