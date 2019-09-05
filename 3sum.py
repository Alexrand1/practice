def threeSum(a):
    temp = sorted(a)
    s = []
    ans = []
    i = 0
    j = len(a) - 1
    while 0 < j:
        if len(s) == 0:
            s.append(temp[i])
            s.append(temp[j])
        else:
            i += 1
        s.append(temp[i])
        if sum(s) == 0 and sorted(s) not in ans:
            ans.append(sorted(s))
            s = []
            j -= 1
        else:
            s.pop()
        if i == j:
            s = []
            i = 0
            j -= 1


    return ans








nums = [-1, 0, 1, 2, -1, 5, -5]
print(threeSum(nums))