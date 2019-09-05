from collections import Counter
def subarraySum(nums, k):
    count = Counter()
    count[0] = 1
    ans = su = 0
    for x in nums:
        su += x
        ans += count[su-k]
        count[su] += 1
    return ans
print(subarraySum([-1,-1,1], 0))