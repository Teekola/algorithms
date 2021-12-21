def swap(A: list, i: int, j: int) -> list:
    temp = A[i]         # Store item at i to temp
    A[i] = A[j]         # Put item at j to index i
    A[j] = temp         # Put the value stored in temp to index j
    return A            # Return resulting array


def partition(A: list, p: int, r: int) -> tuple(list, int):

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


def quickSort(A: list, p: int, r: int) -> list:

    # While the left and right index bound a list of length 2 or higher
    if p < r:
        A, q = partition(A, p, r)   # Partition the array and get the pivot index
        A = quickSort(A, p, q - 1)  # Sort the left subarray recursively
        A = quickSort(A, q + 1, r)  # Sort the right subarray recursively

    # Return the sorted array
    return A