def merge(A: list, p: int, q: int, r: int) -> list:
    # Initialize lists B and C
    B, C = [], []
    
    # Add items of the left half
    for i in range(p, q+1):
        B.append(A[i])
    
    # Add items of the right half
    for j in range(q+1, r+1):
        C.append(A[j])

    # Add infinity to end of both lists
    B.append(float('inf'))
    C.append(float('inf'))

    # Iterate through the merge range and always
    # add the smaller item from the lists
    i, j = 0, 0
    for k in range(p, r+1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1

    # Return the array with merged subarrays
    return A
    


def mergeSort(A, p, r):

    # Continue while left index is smaller than right index
    if p < r:
        q = (p + r) // 2            # Get the middle point
        A = mergeSort(A, p, q)      # Sort left subarray recursively
        A = mergeSort(A, q+1, r)    # Sort right subarray recursively
        A = merge(A, p, q, r)       # Merge left and right subarrays
    
    # Return sorted array
    return A