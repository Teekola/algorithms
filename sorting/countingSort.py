def countingSort(A: list, k: int) -> list:

    # Fill frequency array with equal amount of zeroes as there are numbers
    # in number range k
    F = []
    for i in range(k):
        F.append(0)
    
    # Iterate through array A and count frequencies of its items to the frequency array
    # at the matching indexes with the item's value
    for a in A:
        F[a] += 1

    # Sum the frequencies of the frequency array from left to right
    for i in range(1, k):
        F[i] += F[i-1]
    
    # Create a result array
    S = A.copy()
    
    # Iterate through array A from right to left,
    # find the last index where the item can go from the cumulated array F,
    # and decrease the last index where the item can go by one in the cumulative array F
    for i in range(len(A)-1, -1, -1):
        S[F[A[i]]-1] = A[i]
        F[A[i]] -= 1

    # Return the sorted array
    return S