from time import perf_counter as pfc
from insertionSort import *
from quickSort import *
from mergeSort import *
from heapSort import *
from countingSort import *
from radixSort import *

# Run tests
if __name__ == '__main__':

    # Insertion Sort          
    print("INSERTION SORT")
    # Test array 
    A = [460, 4, 207, 97, 345, 221, 109, 59, 468, 247, 192, 193, 304, 217, 491, 208, 291, 403, 65, 80, 369, 256, 14, 187, 326, 449]   
    print("BEFORE:", A)         # Print the list before sorting
    start_time = pfc()          # Get the start time
    A = insertionSort(A)        # Run the algorithm
    print(pfc() - start_time)   # Print the time
    print("AFTER:", A)          # Print the list after sorting

    # Merge Sort          
    print("\nMERGE SORT")
    # Test array 
    A = [460, 4, 207, 97, 345, 221, 109, 59, 468, 247, 192, 193, 304, 217, 491, 208, 291, 403, 65, 80, 369, 256, 14, 187, 326, 449]   
    print("BEFORE:", A)             # Print the list before sorting
    start_time = pfc()              # Get the start time
    A = mergeSort(A, 0, len(A)-1)   # Run the algorithm
    print(pfc() - start_time)       # Print the time
    print("AFTER:", A)              # Print the list after sorting

    # Heap Sort        
    print("\nHEAP SORT")
    # Test array 
    A = [460, 4, 207, 97, 345, 221, 109, 59, 468, 247, 192, 193, 304, 217, 491, 208, 291, 403, 65, 80, 369, 256, 14, 187, 326, 449]   
    print("BEFORE:", A)             # Print the list before sorting
    start_time = pfc()              # Get the start time
    A = heapSort(A)                 # Run the algorithm
    print(pfc() - start_time)       # Print the time
    print("AFTER:", A)              # Print the list after sorting

    # Quick Sort
    print("\nQUICK SORT")
    # Test array
    A = [460, 4, 207, 97, 345, 221, 109, 59, 468, 247, 192, 193, 304, 217, 491, 208, 291, 403, 65, 80, 369, 256, 14, 187, 326, 449]       
    print("BEFORE:", A)             # Print the list before sorting
    start_time = pfc()              # Get the start time
    A = quickSort(A, 0, len(A)-1)   # Run the algorithm
    print(pfc() - start_time)       # Print the time
    print("AFTER:", A)              # Print the list after sorting

    # Counting Sort
    print("\nCOUNTING SORT")
    # Test array
    A = [460, 4, 207, 97, 345, 221, 109, 59, 468, 247, 192, 193, 304, 217, 491, 208, 291, 403, 65, 80, 369, 256, 14, 187, 326, 449]       
    print("BEFORE:", A)             # Print the list before sorting
    start_time = pfc()              # Get the start time
    A = countingSort(A, 500)        # Run the algorithm
    print(pfc() - start_time)       # Print the time
    print("AFTER:", A)              # Print the list after sorting

    # Radix Sort
    print("\nRADIX SORT")
    # Test array
    A = [460, 4, 207, 97, 345, 221, 109, 59, 468, 247, 192, 193, 304, 217, 491, 208, 291, 403, 65, 80, 369, 256, 14, 187, 326, 449]       
    print("BEFORE:", A)             # Print the list before sorting
    start_time = pfc()              # Get the start time
    A = radixSort(A, 10, 3)         # Run the algorithm
    print(pfc() - start_time)       # Print the time
    print("AFTER:", A)              # Print the list after sorting