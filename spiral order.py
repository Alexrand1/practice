class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return [] # if the matrix is empty return an empty list
        R, C = len(matrix), len(matrix[0]) # R, C denote the length of the row and the column length in Matrix
        seen = [[False] * C for _ in matrix] # this will generate an identical matrix filled with booleans to denote
        # if we have already seen a value at a specific index
        ans = [] # output array
        dr = [0, 1, 0, -1] # row directions
        dc = [1, 0, -1, 0] # column directions
        r = c = di = 0 # starting index for row, column, and direction index
        for _ in range(R * C): # total range of the matrix
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di] # cr and cc denote next candidates row direction = 0 col direction = 1
            # i.e moving 1 to the right
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]: # if candidate coordinates are greater than zero but
                # less than R and C and if they are not yet seen then set r and c = to the candidate coordinates
                r, c = cr, cc
            else:
                # if the above conditions aren't met then move the directional index by taking di + 1 modulo 4
                # this will in the first iteration, keep the column fixed while increasing the row by 1 each iteration
                # i.e. traversing the right edge of the matrix
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
s = Solution()
print(s.spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],[61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],[81,82,83,84,85,86,87,88,89,90],[91,92,93,94,95,96,97,98,99,100]]))