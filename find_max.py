def find_max(s, n, mx):
    if n == 1:
        if mx > s[0]:
            return mx
        else:
            return s[0]
    if mx < s[0]:
        mx = s[0]
    s.pop(0)
    return find_max(s, n-1, mx)


s = [9, 7, 1, 2, 5, 8, 4, 3, 100, 50, 42, 99]
n = len(s)
x = find_max(s, n, 0)
print(x)