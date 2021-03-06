def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur

arr = [9, 8, 7, 6, 5, 4, 3, 1, 2]
insertion_sort(arr)
print(arr)