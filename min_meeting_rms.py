import heapq
ls = [[1,5],[8,9],[8,9]]
print(sorted(ls))

def minMeetingRooms(intervals):
    temp = sorted(intervals)
    i = 0
    et = [x[1] for x in intervals]
    heapq.heapify(et)
    count = 0
    while i < len(intervals):
        if et[0] > temp[i][0]:
            count += 1
            heapq.heappop(et)
        i+=1
    return count

print(minMeetingRooms(ls))