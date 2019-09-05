from collections import deque

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

def rotting(g):
    t = 0
    i = 0
    j = 0
    q = deque()
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] == 2:
                q.append([i, j])
                break
        if len(q)>0:
            break
    while len(q) > 0:
        v = q.popleft()
        t += 1
        try:
            if g[v[0]][v[1]+1] == 1:
                g[v[0]][v[1]+1] = 2
        except IndexError:
            pass
        try:
            if g[v[0]+1][v[1]] == 1:
                g[v[0]+1][v[1]] = 2
        except IndexError:
            pass

    return grid




print(rotting(grid))

