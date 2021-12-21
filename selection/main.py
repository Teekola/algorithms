from quickSelect import *

if __name__ == '__main__':
    print("QUICKSELECT")
    A = [43, 5, 72, 83, 16, 55, 2, 59, 33, 30]
    print("GET 5th biggest item from", A)
    fifth = quickSelect(A, 0, 9, 5)
    print("5th biggest item is", fifth)