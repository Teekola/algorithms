def swap(A: list, i: int, j: int) -> list:
    temp = A[i]         # Store item at i to temp
    A[i] = A[j]         # Put item at j to index i
    A[j] = temp         # Put the value stored in temp to index j
    return A            # Return resulting array


def partition(A: list, p: int, r: int) -> tuple[list, int]:

    x = A[r]            # Make the last item the pivot
    i = p-1             # Counter i increases when we find an item smaller than the pivot

    # Counter j goes from left index to the right index
    for j in range(p, r):

        # If the item at j is smaller or equal to the pivot. To sort in decreasing order, just swap the <= to >=
        if A[j] <= x:
            i += 1              # incerase counter i
            A = swap(A, i, j)   # Swap items at i and j
    
    # Swap the pivot to its correct position
    A = swap(A, r, i + 1)

    # Return the partitioned array and the pivot's index
    return A, i + 1


def quickSelect(A, p, r, i):
    # If we have only one item left, return it
    if p == r:
        return A[p]

    # Partition the array
    A, q = partition(A, p, r)

    # Get the index of the pivot in current subarray
    k = q - p + 1

    # If the pivot is the ith smallest item => return pivot
    # Else if the pivot is bigger than i => search from the left subarray
    # Otherwise the pivot is smaller than => search from the right subarray
    if k == i:
        return A[q]
    elif i < k:
        return quickSelect(A, p, q-1, i)
    else:
        return quickSelect(A, q+1, r, i-k)