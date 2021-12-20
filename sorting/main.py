from time import perf_counter as pfc
from insertionSort import insertionSort;

# Run tests
if __name__ == '__main__':

    # Insertion sort          
    print("INSERTION SORT")     
    A = [9, 7, 1, 5, 2, 6, 4]   # Test array
    print("BEFORE:", A)         # Print the list before sorting
    start_time = pfc()          # Get the start time
    A = insertionSort(A)        # Run the algorithm
    print(pfc() - start_time)   # Print the time
    print("AFTER:", A)          # Print the list after sorting