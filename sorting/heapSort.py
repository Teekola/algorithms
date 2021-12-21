def swap(A: list, i: int, j: int) -> list:
    temp = A[i]         # Store item at i to temp
    A[i] = A[j]         # Put item at j to index i
    A[j] = temp         # Put the value stored in temp to index j
    return A            # Return resulting array

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*i + 2

def parent(i):
    return i // 2

def maxHeapify(A, i):
    # Get indexes of left and right child
    left = leftChild(i)
    right = rightChild(i)

    # If the left child is in the heap and bigger than the parent,
    # set the left child as the biggest. Otherwise set the parent as biggest
    if left < len(A) and A[left] > A[i]:
        biggest = left
    else:
        biggest = i
    
    # If the right child is in the heap and bigger than current biggest
    # set the right child as the biggest
    if right < len(A) and A[right] > A[biggest]:
        biggest = right

    # If either of the children are biggest, swap the parent with the biggest
    # and fix the heap at the index of the old biggest
    if biggest != i:
        A = swap(A, biggest, i)
        A = maxHeapify(A, biggest)
    
    # Return the fixed heap
    return A


def buildMaxHeap(A):
    # i goes from the last inner node to the root
    for i in range(len(A) // 2 - 1, -1, -1):
        # Fix the heap property (recursively) at every inner node
        A = maxHeapify(A, i)

        # Leaf nodes are maxheaps of size 1. When we fix all inner nodes from
        # last to first inner node, we bubble down the smaller values and eventually
        # get the max value to the root with every node below having the max heap property.
    
    # Return the max heap
    return A


def heapSort(A):
    # Build a max heap from the array
    A = buildMaxHeap(A)

    # Initialize sorted array
    B = []

    # While there are items in the heap,
    # swap the root with the last item
    # remove the last item and add it to the start
    # of the sorted array
    while len(A) > 0:
        A = swap(A, 0, len(A)-1)
        biggest = A.pop()
        B.insert(0, biggest)
        A = maxHeapify(A, 0)
    
    # Return the sorted array
    return B