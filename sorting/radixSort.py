def countingSortByDigit(A: list, k: int, d: int) -> list:

    # Fill frequency array with equal amount of zeroes as there are numbers
    # in number range k
    F = []
    for i in range(k):
        F.append(0)
    
    # Iterate through array A and count frequencies of its items at specified digit index to the frequency array
    # at the matching indexes with the item's value
    for a in A:
        F[int(a[d])] += 1

    # Sum the frequencies of the frequency array from left to right
    for i in range(1, k):
        F[i] += F[i-1]
    
    # Create a result array
    S = A.copy()
    
    # Iterate through array A from right to left,
    # find the last index where the item can go from the cumulated array F,
    # and decrease the last index where the item can go by one in the cumulative array F
    for i in range(len(A)-1, -1, -1):
        S[F[int(A[i][d])]-1] = A[i]
        F[int(A[i][d])] -= 1

    # Return the sorted array
    return S

# A = list of integers to be sorted
# b = base of the numbers to be sorted
# d = number of digits in the numbers
def radixSort(A: list, b: int, d: int):

    # Pad numbers with leading zeroes so that each number has length d
    for i in range(len(A)):
        A[i] = str.zfill(str(A[i]), d)

    # Go through each digit in the number from the least significant to the most significant
    # and sort the numbers of base b using stable countingSort algorithm
    for i in range(d-1, -1, -1):
        A = countingSortByDigit(A, b, i)
    
    # Return the sorted array
    return [int(x) for x in A]