def find_minmax(s, n, mx, mn):
    if n == 1:
        if mx > s[0]:
            return mx, mn
        else:
            mx = s[0]
            return mx, mn
    if n == 1:
        if mn < s[0]:
            return mx, mn
        else:
            mn = s[0]
            return mx, mn
    if mx < s[0]:
        mx = s[0]
    if mn > s[0]:
        mn = s[0]
    s.pop(0)
    return find_minmax(s, n-1, mx, mn)


arr = [9, 1, 2, 4, 5, 8, 7, 0]
print(find_minmax(arr, len(arr), 0, 100000000))