ls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
max_area = max(ls) * (len(ls)-1)
wall_area = sum(ls)
i = 0
j = 1
mx = 0
ans = 0
while j < len(ls)-2:
    if ls[i] > mx:
        mx = ls[i]
    if ls[i] < mx:
        ans += (mx - ls[i])
    i += 1
    j += 1

print(ans)