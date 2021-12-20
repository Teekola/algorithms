def insertionSort(array: list):
    # Copy the array to prevent unwanted side-effects
    A = array.copy()

    # i steps from 2nd index to last index
    for i in range(1, len(A)):
        # Store the item at index i to temp
        temp = A[i]

        # Move items in the sorted portion of the list with higher value than temp one step to the right
        while A[i-1] > temp and i > 0:
            A[i] = A[i-1]
            i -= 1
        
        # Place temp to the correct position in the sorted portion
        A[i] = temp

    # Return the sorted array
    return A