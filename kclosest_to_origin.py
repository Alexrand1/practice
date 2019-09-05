import math
points = [[3, 3], [5, -1], [-2, 4]]
def kclosest(points, K):
    euclid = {(math.sqrt(((x[0]-0)**2) + ((x[1]-0)**2))): x for x in points}
    ans = []
    print(euclid)
    if len(euclid) < K:
        return points
    for _ in range(K):
        ans.append(euclid.pop(min(euclid)))
    return ans



print(kclosest(points, 2))
d = {}