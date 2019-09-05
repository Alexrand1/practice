def puzzle_solve(k, S, U):
    ans = False
    for e in U:
        if e not in S:
            S.append(U.pop(0))
        if S == ['c', 'b', 'a']:
            ans =  True
        else:
            puzzle_solve(k-1, S, U)
        if S[len(S)-1] not in U:
            U.append(S.pop())
        return ans



perms = []
s = []
u = ['a', 'b', 'c']
k = 3
print(puzzle_solve(k, s, u))
